#!/usr/bin/env python3
"""M5C training-only calibrated adaptive routing.
Threshold is selected solely from synthetic perturbations of training waveforms.
Real holdout/ID/OOD labels are never used for calibration. Exploratory; not canonical NS-MDS.
"""
from pathlib import Path
import json, urllib.request
import numpy as np, pandas as pd
ROOT=Path(__file__).resolve().parent; OUT=ROOT/'results_adaptive_calibrated'; OUT.mkdir(exist_ok=True)
BASE='https://raw.githubusercontent.com/imakafanxy/UltrasonicData_Bristol/main/UltraSonic%20guided-wave%20sig'
FILES={'noise_free':BASE+'/OOD%20ultrasonic%20guided-wave%20signals/Noise-free%20normalized%20delamination%20damage%20position%20at%200%20to%201.csv','id10':BASE+'/ID%20ultrasonic%20guided-wave%20signals/Averaged%2010dB%20normalized%20delamination%20damage%20position%20at%200%20to%201.csv','ood':BASE+'/OOD%20ultrasonic%20guided-wave%20signals/10dB%20normalized%20delamination%20damage%20position%20at%200.2%20to%200.3%20and%205dB%20at%200.7%20to%200.8.csv'}
def load(k):
 p=ROOT/(k+'.csv')
 if not p.exists(): urllib.request.urlretrieve(FILES[k],p)
 d=pd.read_csv(p); return d.drop(columns=['position']).to_numpy(float),d.position.to_numpy(float)
def mm(v): return 300+400*np.asarray(v)
def normfit(X): return X.mean(),X.std()+1e-12
def pred(A,y,B,thr):
 out=[]; routes=[]; us=[]; order=np.argsort(y); ys=y[order]; AA=A[order]
 for z in B:
  d=np.mean((A-z)**2,1); ix=np.argsort(d)[:2]; ds=np.maximum(d[ix],1e-15); w=1/ds**2; pk=float(np.sum(w*y[ix])/np.sum(w))
  do=np.mean((AA-z)**2,1); j=int(np.argmin(do)); c={j};
  if j>0:c.add(j-1)
  if j+1<len(ys):c.add(j+1)
  ci=np.array(sorted(c)); cds=np.maximum(do[ci],1e-15); pb=float(np.sum((1/cds)*ys[ci])/np.sum(1/cds)); u=float(np.min(d)); use=u>thr
  out.append(pb if use else pk); routes.append('bracket' if use else 'knn2'); us.append(u)
 return np.array(out),np.array(routes),np.array(us)
def metrics(y,p):
 e=np.abs(mm(p)-mm(y)); return dict(n=len(e),mae_mm=float(e.mean()),median_mm=float(np.median(e)),p90_mm=float(np.quantile(e,.9)),within_5mm=float(np.mean(e<=5)),within_10mm=float(np.mean(e<=10)),max_mm=float(e.max()))
X,y=load('noise_free'); Xi,yi=load('id10'); Xo,yo=load('ood'); tr=np.arange(len(y))%2==0; te=~tr; mu,sd=normfit(X[tr]); A=(X[tr]-mu)/sd
# Synthetic calibration from training only: deterministic Gaussian perturbations at several amplitudes.
rng=np.random.default_rng(20260827); Z=[]; Y=[]
base_scale=float(np.std(A))
for sigma in (0.02,0.05,0.10,0.20,0.35):
 for i in range(len(A)):
  Z.append(A[i]+rng.normal(0,sigma*base_scale,size=A.shape[1])); Y.append(y[tr][i])
Z=np.asarray(Z); Y=np.asarray(Y)
# Candidate thresholds from training LOO distance quantiles; choose synthetic MAE minimum, tie -> highest threshold.
D=np.mean((A[:,None,:]-A[None,:,:])**2,2); np.fill_diagonal(D,np.inf); loo=np.min(D,1); candidates=np.unique(np.quantile(loo,[.50,.60,.70,.80,.85,.90,.925,.95,.975,.99]))
cal=[]
for t in candidates:
 p,r,u=pred(A,y[tr],Z,float(t)); cal.append((float(np.mean(np.abs(mm(p)-mm(Y)))),float(t),float(np.mean(r=='bracket'))))
cal.sort(key=lambda q:(q[0],-q[1])); best_mae,thr,cal_rate=cal[0]
pd.DataFrame(cal,columns=['synthetic_mae_mm','threshold','bracket_rate']).to_csv(OUT/'calibration.csv',index=False)
rows=[]; allp=[]
for ds,Zraw,Yraw,mask in [('noise_free_holdout',X,y,te),('id10_all',Xi,yi,np.ones(len(yi),bool)),('ood_10_5db',Xo,yo,np.ones(len(yo),bool))]:
 B=(Zraw[mask]-mu)/sd; p,r,u=pred(A,y[tr],B,thr); rows.append({'dataset':ds,'model':'adaptive_traincal','threshold':thr,'bracket_rate':float(np.mean(r=='bracket')),**metrics(Yraw[mask],p)})
 for yt,yp,rr,uu in zip(Yraw[mask],p,r,u): allp.append({'dataset':ds,'route':rr,'uncertainty':float(uu),'true_mm':float(mm(yt)),'pred_mm':float(mm(yp)),'abs_err_mm':float(abs(mm(yt)-mm(yp)))})
pd.DataFrame(rows).to_csv(OUT/'metrics.csv',index=False); pd.DataFrame(allp).to_csv(OUT/'predictions.csv',index=False)
manifest={'gate':'M5C training-only calibrated routing','calibration':'synthetic perturbations of training waveforms only','candidate_thresholds':'training LOO distance quantiles','selected_threshold':thr,'synthetic_calibration_mae_mm':best_mae,'synthetic_bracket_rate':cal_rate,'real_test_labels_used_for_calibration':False,'reference_mae_mm':15.0,'status':'exploratory adaptive baseline; not canonical NS-MDS'}; (OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)); print(pd.DataFrame(rows).to_string(index=False)); print(pd.DataFrame(cal,columns=['synthetic_mae_mm','threshold','bracket_rate']).to_string(index=False)); print(json.dumps(manifest,indent=2))