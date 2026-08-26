#!/usr/bin/env python3
"""M5 continuous localization gate. Same KU/Bristol data and alternating split.
Exploratory benchmark; not canonical NS-MDS.
"""
from pathlib import Path
import json, urllib.request
import numpy as np, pandas as pd
ROOT=Path(__file__).resolve().parent; OUT=ROOT/'results_continuous'; OUT.mkdir(exist_ok=True)
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
def knn_cont(Xtr,ytr,Xte,k=2,power=2):
 A,B=norm(Xtr,Xte); out=[]
 for z in B:
  d=np.mean((A-z)**2,axis=1); ix=np.argsort(d)[:k]; ds=np.maximum(d[ix],1e-15); w=1/(ds**power); out.append(float(np.sum(w*ytr[ix])/np.sum(w)))
 return np.array(out)
def bracket_interp(Xtr,ytr,Xte):
 # Continuous baseline: nearest waveform plus its nearest training point on each side when available.
 A,B=norm(Xtr,Xte); out=[]
 order=np.argsort(ytr); ys=ytr[order]; AA=A[order]
 for z in B:
  d=np.mean((AA-z)**2,axis=1); j=int(np.argmin(d)); cand={j}
  if j>0:cand.add(j-1)
  if j+1<len(ys):cand.add(j+1)
  ix=np.array(sorted(cand)); ds=np.maximum(d[ix],1e-15); w=1/ds; out.append(float(np.sum(w*ys[ix])/np.sum(w)))
 return np.array(out)
X,y=load('noise_free'); Xi,yi=load('id10'); Xo,yo=load('ood'); tr=np.arange(len(y))%2==0; te=~tr
rows=[]; preds=[]
for ds,Z,Y,mask in [('noise_free_holdout',X,y,te),('id10_all',Xi,yi,np.ones(len(yi),bool)),('ood_10_5db',Xo,yo,np.ones(len(yo),bool))]:
 for name,p in [('knn2_cont',knn_cont(X[tr],y[tr],Z[mask],2,2)),('bracket_cont',bracket_interp(X[tr],y[tr],Z[mask]))]:
  rows.append({'dataset':ds,'model':name,**met(Y[mask],p)})
  for yt,yp in zip(Y[mask],p):preds.append({'dataset':ds,'model':name,'true_mm':float(mm(yt)),'pred_mm':float(mm(yp)),'abs_err_mm':float(abs(mm(yt)-mm(yp)))})
pd.DataFrame(rows).to_csv(OUT/'metrics.csv',index=False); pd.DataFrame(preds).to_csv(OUT/'predictions.csv',index=False)
rng=np.random.default_rng(20260826); boots=[]
P=pd.DataFrame(preds)
for name in P.model.unique():
 e=P[(P.dataset=='noise_free_holdout')&(P.model==name)].abs_err_mm.to_numpy(); v=[np.mean(rng.choice(e,len(e),replace=True)) for _ in range(5000)]; boots.append({'model':name,'mae_boot_mean':float(np.mean(v)),'ci_low':float(np.quantile(v,.025)),'ci_high':float(np.quantile(v,.975))})
pd.DataFrame(boots).to_csv(OUT/'bootstrap.csv',index=False)
manifest={'gate':'M5 continuous localization','frozen_reference_mae_mm':15.0,'pass_rule':'noise_free MAE < 15.0 mm; noise/OOD reported without post-hoc tuning','split':'alternating positions unchanged','status':'exploratory continuous baselines; not canonical NS-MDS'}
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)); print(pd.DataFrame(rows).to_string(index=False)); print(pd.DataFrame(boots).to_string(index=False)); print(json.dumps(manifest,indent=2))