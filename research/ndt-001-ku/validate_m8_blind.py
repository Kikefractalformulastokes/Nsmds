#!/usr/bin/env python3
"""M8 corrected internal blind validation for NDT-001 KU.

Uses the exact public CSV schema, physical position mapping, waveform
normalization and two-neighbour inverse-square interpolation convention used
by the frozen M4-M7 chain. A deterministic 20% subset is held out before
prediction. This remains internal blind validation, not third-party or
industrial validation, and does not establish canonical NS-MDS attribution.
"""
from pathlib import Path
import json, urllib.request
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results_m8'; OUT.mkdir(parents=True,exist_ok=True)
URL='https://raw.githubusercontent.com/imakafanxy/UltrasonicData_Bristol/main/UltraSonic%20guided-wave%20sig/OOD%20ultrasonic%20guided-wave%20signals/Noise-free%20normalized%20delamination%20damage%20position%20at%200%20to%201.csv'
SEED=20260827

def load():
    p=ROOT/'noise_free.csv'
    if not p.exists(): urllib.request.urlretrieve(URL,p)
    d=pd.read_csv(p)
    return d.drop(columns=['position']).to_numpy(float), d['position'].to_numpy(float)

def mm(v): return 300.0+400.0*np.asarray(v)

def normalize(train,test):
    mu=train.mean(); sd=train.std()+1e-12
    return (train-mu)/sd,(test-mu)/sd

def nearest(A,y,z):
    d=np.mean((A-z)**2,axis=1)
    return float(y[int(np.argmin(d))])

def cont2(A,y,z):
    d=np.mean((A-z)**2,axis=1); ix=np.argsort(d)[:2]
    ds=np.maximum(d[ix],1e-15); w=1/(ds**2)
    return float(np.sum(w*y[ix])/np.sum(w))

def main():
    X,y=load(); n=len(y)
    rng=np.random.default_rng(SEED)
    blind=np.sort(rng.choice(n,size=max(1,n//5),replace=False))
    train=np.setdiff1d(np.arange(n),blind)
    A,B=normalize(X[train],X[blind]); yt=y[blind]; ytr=y[train]
    pb=np.array([nearest(A,ytr,z) for z in B]); pc=np.array([cont2(A,ytr,z) for z in B])
    berr=np.abs(mm(pb)-mm(yt)); cerr=np.abs(mm(pc)-mm(yt))
    result={
      'gate':'M8 corrected internal blind validation',
      'seed':SEED,'n_total':int(n),'n_blind':int(len(blind)),
      'physical_mapping':'position_mm = 300 + 400 * normalized_position',
      'baseline_mae_mm':float(berr.mean()),'challenger_mae_mm':float(cerr.mean()),
      'relative_mae_reduction_pct':float(100*(berr.mean()-cerr.mean())/berr.mean()) if berr.mean() else None,
      'challenger_median_mm':float(np.median(cerr)),'challenger_p90_mm':float(np.quantile(cerr,.9)),
      'challenger_max_mm':float(cerr.max()),'challenger_better_count':int(np.sum(cerr<berr)),
      'tie_count':int(np.sum(cerr==berr)),'challenger_worse_count':int(np.sum(cerr>berr)),
      'pass_rule':'challenger MAE < nearest-neighbour MAE on deterministic blind subset',
      'pass':bool(cerr.mean()<berr.mean()),'tuning_on_blind_labels':False,
      'guardrail':'internal blind re-split only; not independent third-party/industrial validation; not canonical NS-MDS attribution'
    }
    pd.DataFrame({'index':blind,'true_norm':yt,'true_mm':mm(yt),'baseline_mm':mm(pb),'challenger_mm':mm(pc),'baseline_error_mm':berr,'challenger_error_mm':cerr}).to_csv(OUT/'blind_predictions.csv',index=False)
    (OUT/'summary.json').write_text(json.dumps(result,indent=2)); print(json.dumps(result,indent=2))
if __name__=='__main__': main()
