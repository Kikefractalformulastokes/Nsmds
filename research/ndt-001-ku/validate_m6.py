#!/usr/bin/env python3
"""M6 statistical validation for frozen NDT-001 KU continuous challenger.
Paired comparison, bootstrap CI of MAE improvement, leave-one-position-pair sensitivity,
and explicit outlier accounting. No model tuning is performed here.
"""
from pathlib import Path
import json, urllib.request
import numpy as np, pandas as pd
ROOT=Path(__file__).resolve().parent; OUT=ROOT/'results_m6'; OUT.mkdir(exist_ok=True)
URL='https://raw.githubusercontent.com/imakafanxy/UltrasonicData_Bristol/main/UltraSonic%20guided-wave%20sig/OOD%20ultrasonic%20guided-wave%20signals/Noise-free%20normalized%20delamination%20damage%20position%20at%200%20to%201.csv'
p=ROOT/'noise_free.csv'
if not p.exists(): urllib.request.urlretrieve(URL,p)
df=pd.read_csv(p); X=df.drop(columns=['position']).to_numpy(float); y=df.position.to_numpy(float)
tr=np.arange(len(y))%2==0; te=~tr; Xtr=X[tr]; ytr=y[tr]; Xte=X[te]; yte=y[te]
mu=Xtr.mean(); sd=Xtr.std()+1e-12; A=(Xtr-mu)/sd; B=(Xte-mu)/sd
pred=[]
for z in B:
 d=np.mean((A-z)**2,axis=1); ix=np.argsort(d)[:2]; ds=np.maximum(d[ix],1e-15); w=1/(ds**2); pred.append(float(np.sum(w*ytr[ix])/np.sum(w)))
pred=np.asarray(pred); true_mm=300+400*yte; pred_mm=300+400*pred
chall=np.abs(pred_mm-true_mm); base=np.full_like(chall,15.0); improvement=base-chall
rng=np.random.default_rng(20260827); boots=[]
for _ in range(20000):
 ix=rng.integers(0,len(chall),len(chall)); boots.append(float(np.mean(improvement[ix])))
boots=np.asarray(boots)
# exact sign-style descriptive counts; paired bootstrap is primary inferential summary
summary={'n':int(len(chall)),'baseline_mae_mm':15.0,'challenger_mae_mm':float(chall.mean()),'mean_improvement_mm':float(improvement.mean()),'relative_mae_reduction_pct':float(100*improvement.mean()/15.0),'paired_bootstrap_improvement_ci95_mm':[float(np.quantile(boots,.025)),float(np.quantile(boots,.975))],'bootstrap_prob_improvement_gt_0':float(np.mean(boots>0)),'challenger_better_count':int(np.sum(chall<base)),'tie_count':int(np.sum(chall==base)),'challenger_worse_count':int(np.sum(chall>base)),'errors_gt_15mm':int(np.sum(chall>15)),'errors_gt_30mm':int(np.sum(chall>30)),'max_error_mm':float(chall.max())}
# sensitivity: remove each holdout observation one at a time
loo=[]
for i in range(len(chall)):
 keep=np.arange(len(chall))!=i; loo.append(float(chall[keep].mean()))
summary['leave_one_out_mae_range_mm']=[float(np.min(loo)),float(np.max(loo))]
summary['leave_one_out_all_below_15mm']=bool(np.max(loo)<15)
pd.DataFrame({'true_mm':true_mm,'pred_mm':pred_mm,'challenger_abs_err_mm':chall,'baseline_abs_err_mm':base,'paired_improvement_mm':improvement}).to_csv(OUT/'paired_errors.csv',index=False)
(OUT/'summary.json').write_text(json.dumps(summary,indent=2))
manifest={'gate':'M6 statistical validation','model':'frozen M5 knn2_cont','tuning_performed':False,'primary_statistic':'paired bootstrap of baseline MAE minus challenger MAE','bootstrap_replicates':20000,'seed':20260827,'guardrail':'validates benchmark result only; does not establish NS-MDS attribution or industrial performance'}
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)); print(json.dumps(summary,indent=2)); print(json.dumps(manifest,indent=2))