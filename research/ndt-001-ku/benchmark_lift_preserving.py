#!/usr/bin/env python3
"""Exploratory lift-preserving NDT challenger.
Frozen dataset/split/metrics from benchmark_ku.py. This is a reconstruction
inspired by the documented NS-MDS architectural rule, NOT canonical NS-MDS.
"""
import json, urllib.request
from pathlib import Path
import numpy as np, pandas as pd
from scipy.ndimage import gaussian_filter1d

ROOT=Path(__file__).resolve().parent; OUT=ROOT/'results_lift'; OUT.mkdir(exist_ok=True)
BASE='https://raw.githubusercontent.com/imakafanxy/UltrasonicData_Bristol/main/UltraSonic%20guided-wave%20sig'
FILES={
'noise_free':BASE+'/OOD%20ultrasonic%20guided-wave%20signals/Noise-free%20normalized%20delamination%20damage%20position%20at%200%20to%201.csv',
'id10':BASE+'/ID%20ultrasonic%20guided-wave%20signals/Averaged%2010dB%20normalized%20delamination%20damage%20position%20at%200%20to%201.csv',
'ood':BASE+'/OOD%20ultrasonic%20guided-wave%20signals/10dB%20normalized%20delamination%20damage%20position%20at%200.2%20to%200.3%20and%205dB%20at%200.7%20to%200.8.csv'}
def load(k):
 p=ROOT/(k+'.csv');
 if not p.exists(): urllib.request.urlretrieve(FILES[k],p)
 d=pd.read_csv(p); return d.drop(columns=['position']).to_numpy(float),d.position.to_numpy(float)
def mm(v): return 300+400*np.asarray(v)
def met(y,p):
 e=np.abs(mm(p)-mm(y)); return dict(n=len(e),mae_mm=e.mean(),median_mm=np.median(e),p90_mm=np.quantile(e,.9),within_5mm=np.mean(e<=5),within_10mm=np.mean(e<=10),max_mm=e.max())
def raw_dist(a,b): return np.mean((a-b)**2,axis=1)
def local_signature(X):
 # Preserve waveform globally; derive a local residual only where multiscale curvature is high.
 sm=gaussian_filter1d(X,3,axis=1); res=X-sm
 cur=np.abs(np.diff(sm,n=2,axis=1,prepend=sm[:,:1],append=sm[:,-1:]))
 q=np.quantile(cur,.90,axis=1,keepdims=True); mask=cur>=q
 return res*mask

def predict(Xtr,ytr,Xte,alpha):
 mu=Xtr.mean(); sd=Xtr.std()+1e-12; A=(Xtr-mu)/sd; B=(Xte-mu)/sd
 LA=local_signature(A); LB=local_signature(B); out=[]
 for z,lz in zip(B,LB):
  d0=raw_dist(A,z)
  # Local correction augments rather than replaces the strong raw baseline.
  dl=np.mean((LA-lz)**2,axis=1)
  d=d0+alpha*dl
  out.append(ytr[np.argmin(d)])
 return np.asarray(out)
X,y=load('noise_free'); Xi,yi=load('id10'); Xo,yo=load('ood'); tr=np.arange(len(y))%2==0; te=~tr
# alpha chosen WITHOUT holdout labels: fixed architectural sweep reported in full; primary alpha=0.25 predeclared.
alphas=[0.0,0.05,0.1,0.25,0.5,1.0,2.0]; rows=[]; preds=[]
for a in alphas:
 for ds,Z,Y,mask in [('noise_free_holdout',X,y,te),('id10_all',Xi,yi,np.ones(len(yi),bool)),('ood_10_5db',Xo,yo,np.ones(len(yo),bool))]:
  p=predict(X[tr],y[tr],Z[mask],a); m=met(Y[mask],p); rows.append({'alpha':a,'dataset':ds,**m})
  if a in (0.0,0.25):
   for yt,yp in zip(Y[mask],p): preds.append({'alpha':a,'dataset':ds,'true_mm':float(mm(yt)),'pred_mm':float(mm(yp)),'abs_err_mm':float(abs(mm(yt)-mm(yp)))})
pd.DataFrame(rows).to_csv(OUT/'metrics_sweep.csv',index=False); pd.DataFrame(preds).to_csv(OUT/'predictions_primary.csv',index=False)
# bootstrap primary alpha vs frozen alpha=0 baseline on noise-free holdout
rng=np.random.default_rng(20260826); boot=[]
for a in [0.0,0.25]:
 s=pd.DataFrame(preds); e=s[(s.alpha==a)&(s.dataset=='noise_free_holdout')].abs_err_mm.to_numpy(); vals=[np.mean(rng.choice(e,len(e),replace=True)) for _ in range(2000)]
 boot.append({'alpha':a,'mean':float(np.mean(vals)),'lo':float(np.quantile(vals,.025)),'hi':float(np.quantile(vals,.975))})
pd.DataFrame(boot).to_csv(OUT/'bootstrap.csv',index=False)
manifest={'status':'exploratory reconstruction; not canonical NS-MDS','architectural_rule':'preserve strong raw baseline; add correction only on high-curvature local waveform regions','primary_alpha':0.25,'split':'same alternating-position split as frozen benchmark','metrics':'unchanged'}
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)); print(pd.DataFrame(rows).to_string(index=False)); print(json.dumps(manifest,indent=2))