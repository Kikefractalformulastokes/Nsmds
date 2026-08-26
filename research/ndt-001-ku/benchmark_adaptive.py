#!/usr/bin/env python3
"""M5B adaptive continuous localization.
Selector uses only distance-based uncertainty calibrated on training waveforms.
No test labels are used for routing. Exploratory; not canonical NS-MDS.
"""
from pathlib import Path
import json, urllib.request
import numpy as np, pandas as pd
ROOT=Path(__file__).resolve().parent; OUT=ROOT/'results_adaptive'; OUT.mkdir(exist_ok=True)
BASE='https://raw.githubusercontent.com/imakafanxy/UltrasonicData_Bristol/main/UltraSonic%20guided-wave%20sig'
FILES={'noise_free':BASE+'/OOD%20ultrasonic%20guided-wave%20signals/Noise-free%20normalized%20delamination%20damage%20position%20at%200%20to%201.csv','id10':BASE+'/ID%20ultrasonic%20guided-wave%20signals/Averaged%2010dB%20normalized%20delamination%20damage%20position%20at%200%20to%201.csv','ood':BASE+'/OOD%20ultrasonic%20guided-wave%20signals/10dB%20normalized%20delamination%20damage%20position%20at%200.2%20to%200.3%20and%205dB%20at%200.7%20to%200.8.csv'}
def load(k):
 p=ROOT/(k+'.csv')
 if not p.exists(): urllib.request.urlretrieve(FILES[k],p)
 d=pd.read_csv(p); return d.drop(columns=['position']).to_numpy(float),d.position.to_numpy(float)
def mm(v): return 300+400*np.asarray(v)
def met(y,p):
 e=np.abs(mm(p)-mm(y)); return {'n':len(e),'mae_mm':float(e.mean()),'median_mm':float(np.median(e)),'p90_mm':float(np.quantile(e,.9)),'within_5mm':float(np.mean(e<=5)),'within_10mm':float(np.mean(e<=10)),'max_mm':float(e.max())}
def norm(train,test):
 mu=train.mean(); sd=train.std()+1e-12; return (train-mu)/sd,(test-mu)/sd
def distmat(A,B): return np.mean((B[:,None,:]-A[None,:,:])**2,axis=2)
def predict_all(Xtr,ytr,Xte,threshold):
 A,B=norm(Xtr,Xte); D=distmat(A,B); order=np.argsort(ytr); ys=ytr[order]; AA=A[order]; out=[]; routes=[]; uncert=[]
 for z,drow in zip(B,D):
  ix=np.argsort(drow)[:2]; ds=np.maximum(drow[ix],1e-15); w=1/(ds**2); knn=float(np.sum(w*ytr[ix])/np.sum(w))
  dord=np.mean((AA-z)**2,axis=1); j=int(np.argmin(dord)); cand={j}
  if j>0:cand.add(j-1)
  if j+1<len(ys):cand.add(j+1)
  ci=np.array(sorted(cand)); cds=np.maximum(dord[ci],1e-15); cw=1/cds; bracket=float(np.sum(cw*ys[ci])/np.sum(cw))
  u=float(np.min(drow)); use_bracket=u>threshold
  out.append(bracket if use_bracket else knn); routes.append('bracket' if use_bracket else 'knn2'); uncert.append(u)
 return np.array(out),routes,np.array(uncert)
X,y=load('noise_free'); Xi,yi=load('id10'); Xo,yo=load('ood'); tr=np.arange(len(y))%2==0; te=~tr
# Calibrate novelty threshold from training only: leave-one-out nearest-neighbor distances, q95.
A,_=norm(X[tr],X[tr]); D=distmat(A,A); np.fill_diagonal(D,np.inf); loo=np.min(D,axis=1); threshold=float(np.quantile(loo,.95))
rows=[]; preds=[]
for ds,Z,Y,mask in [('noise_free_holdout',X,y,te),('id10_all',Xi,yi,np.ones(len(yi),bool)),('ood_10_5db',Xo,yo,np.ones(len(yo),bool))]:
 p,r,u=predict_all(X[tr],y[tr],Z[mask],threshold); rows.append({'dataset':ds,'model':'adaptive_q95','threshold':threshold,'bracket_rate':float(np.mean(np.array(r)=='bracket')),**met(Y[mask],p)})
 for yt,yp,rr,uu in zip(Y[mask],p,r,u): preds.append({'dataset':ds,'route':rr,'uncertainty':float(uu),'true_mm':float(mm(yt)),'pred_mm':float(mm(yp)),'abs_err_mm':float(abs(mm(yt)-mm(yp)))})
pd.DataFrame(rows).to_csv(OUT/'metrics.csv',index=False); pd.DataFrame(preds).to_csv(OUT/'predictions.csv',index=False)
rng=np.random.default_rng(20260826); P=pd.DataFrame(preds); e=P[P.dataset=='noise_free_holdout'].abs_err_mm.to_numpy(); vals=[np.mean(rng.choice(e,len(e),replace=True)) for _ in range(5000)]; boot={'mae_boot_mean':float(np.mean(vals)),'ci_low':float(np.quantile(vals,.025)),'ci_high':float(np.quantile(vals,.975))}; (OUT/'bootstrap.json').write_text(json.dumps(boot,indent=2))
manifest={'gate':'M5B adaptive continuous localization','selector':'route to bracket if min waveform distance exceeds q95 leave-one-out training distance; else knn2','threshold_calibration':'training only, no test labels','frozen_reference_mae_mm':15.0,'targets':'retain noise-free improvement; reduce OOD failure vs KNN2; all datasets reported','status':'exploratory adaptive baseline; not canonical NS-MDS'}; (OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)); print(pd.DataFrame(rows).to_string(index=False)); print(json.dumps(boot,indent=2)); print(json.dumps(manifest,indent=2))