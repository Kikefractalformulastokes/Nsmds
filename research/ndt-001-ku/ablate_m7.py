#!/usr/bin/env python3
"""M7 attribution/failure-mode ablation for NDT-001.
Tests simple continuous localization variants and pre-outcome confidence observables.
No NS-MDS attribution is made by this script.
"""
from pathlib import Path
import json, urllib.request
import numpy as np, pandas as pd
ROOT=Path(__file__).resolve().parent; OUT=ROOT/'results_m7'; OUT.mkdir(exist_ok=True)
URL='https://raw.githubusercontent.com/imakafanxy/UltrasonicData_Bristol/main/UltraSonic%20guided-wave%20sig/OOD%20ultrasonic%20guided-wave%20signals/Noise-free%20normalized%20delamination%20damage%20position%20at%200%20to%201.csv'
p=ROOT/'noise_free.csv'
if not p.exists(): urllib.request.urlretrieve(URL,p)
df=pd.read_csv(p); X=df.drop(columns=['position']).to_numpy(float); y=df.position.to_numpy(float)
tr=np.arange(len(y))%2==0; te=~tr; Xtr=X[tr]; ytr=y[tr]; Xte=X[te]; yte=y[te]
mu=Xtr.mean(); sd=Xtr.std()+1e-12; A=(Xtr-mu)/sd; B=(Xte-mu)/sd
rows=[]; preds={k:[] for k in ['nn','knn2_uniform','knn2_inv','knn2_inv2','knn3_inv2']}; conf=[]
for z in B:
 d=np.mean((A-z)**2,axis=1); order=np.argsort(d); d1,d2=d[order[0]],d[order[1]]
 conf.append({'d1':float(d1),'d2':float(d2),'margin':float(d2-d1),'ratio':float(d2/(d1+1e-15))})
 preds['nn'].append(ytr[order[0]])
 for name,k,powr in [('knn2_uniform',2,0),('knn2_inv',2,1),('knn2_inv2',2,2),('knn3_inv2',3,2)]:
  ix=order[:k]
  if powr==0: w=np.ones(k)
  else: w=1/np.maximum(d[ix],1e-15)**powr
  preds[name].append(float(np.sum(w*ytr[ix])/np.sum(w)))
true=300+400*yte
for name,v in preds.items():
 pr=300+400*np.asarray(v); e=np.abs(pr-true)
 rows.append({'model':name,'n':len(e),'mae_mm':float(e.mean()),'median_mm':float(np.median(e)),'p90_mm':float(np.quantile(e,.9)),'max_mm':float(e.max()),'better_than_15_count':int(np.sum(e<15)),'errors_gt_30mm':int(np.sum(e>30))})
 if name=='knn2_inv2': target=e
c=pd.DataFrame(conf); c['error_mm']=target; c['failure_gt15']=target>15; c['failure_gt30']=target>30
# descriptive separability only: report rank correlation and best threshold chosen on this same holdout as diagnostic, NOT deployable calibration
for col in ['d1','d2','margin','ratio']:
 c[col+'_rank']=c[col].rank(); c['err_rank']=c.error_mm.rank()
 corr=float(c[[col+'_rank','err_rank']].corr().iloc[0,1])
 vals=np.unique(c[col]); best=None
 for direction in ['high','low']:
  for t in vals:
   flag=(c[col]>=t) if direction=='high' else (c[col]<=t)
   tp=int(np.sum(flag & c.failure_gt15)); fp=int(np.sum(flag & ~c.failure_gt15)); fn=int(np.sum(~flag & c.failure_gt15))
   score=(2*tp)/(2*tp+fp+fn) if 2*tp+fp+fn else 0
   cand=(score,tp,-fp,direction,float(t))
   if best is None or cand[:3]>best[:3]: best=cand
 rows.append({'model':'diagnostic_'+col,'rank_corr_abs_error':corr,'best_same_holdout_f1':best[0],'detected_failures':best[1],'false_flags':-best[2],'direction':best[3],'threshold':best[4]})
pd.DataFrame(rows).to_csv(OUT/'ablation.csv',index=False); c.to_csv(OUT/'case_diagnostics.csv',index=False)
summary={'gate':'M7 attribution/failure-mode ablation','status':'diagnostic only','key_guardrail':'same-holdout confidence thresholds are diagnostic and must not be used as validated routing rules','attribution':'continuous interpolation variants are generic baselines; this gate does not establish canonical NS-MDS causality','models':[r for r in rows if not r['model'].startswith('diagnostic_')],'confidence_diagnostics':[r for r in rows if r['model'].startswith('diagnostic_')]}
(OUT/'summary.json').write_text(json.dumps(summary,indent=2)); print(json.dumps(summary,indent=2))