#!/usr/bin/env python3
import hashlib, json, os, urllib.request
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.signal import correlate
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import PCA

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results'; OUT.mkdir(parents=True, exist_ok=True)
BASE='https://raw.githubusercontent.com/imakafanxy/UltrasonicData_Bristol/main/UltraSonic%20guided-wave%20sig'
FILES={
 'noise_free': BASE+'/OOD%20ultrasonic%20guided-wave%20signals/Noise-free%20normalized%20delamination%20damage%20position%20at%200%20to%201.csv',
 'id10': BASE+'/ID%20ultrasonic%20guided-wave%20signals/Averaged%2010dB%20normalized%20delamination%20damage%20position%20at%200%20to%201.csv',
 'ood': BASE+'/OOD%20ultrasonic%20guided-wave%20signals/10dB%20normalized%20delamination%20damage%20position%20at%200.2%20to%200.3%20and%205dB%20at%200.7%20to%200.8.csv'
}

def get(name,url):
    p=ROOT/f'{name}.csv'
    urllib.request.urlretrieve(url,p)
    return p

def sha256(p):
    h=hashlib.sha256();
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()

def load(p):
    df=pd.read_csv(p)
    pos=df['position'].astype(float).to_numpy()
    X=df.drop(columns=['position']).to_numpy(float)
    return X,pos

def mm(y): return 300.0+400.0*np.asarray(y)

def engineered(X):
    # label-free waveform descriptors: temporal, derivative, curvature, spectral and multiscale energy.
    feats=[]
    n=X.shape[1]
    bands=np.array_split(np.arange(n//2+1),8)
    for x in X:
        dx=np.diff(x); dd=np.diff(x,n=2)
        spec=np.abs(np.fft.rfft(x))
        row=[x.mean(),x.std(),np.max(x),np.min(x),np.sqrt(np.mean(x*x)),
             dx.mean(),dx.std(),np.sqrt(np.mean(dx*dx)),dd.std(),
             np.argmax(np.abs(x))/max(1,n-1),
             np.sum(np.abs(x)),np.sum(np.abs(dx))]
        row += [float(np.mean(spec[b])) for b in bands]
        row += [float(np.sqrt(np.mean(x[i::4]**2))) for i in range(4)]
        feats.append(row)
    return np.asarray(feats)

def nearest_predict(Xtr,ytr,Xte):
    # scale each waveform globally using training statistics; Euclidean nearest waveform.
    mu=Xtr.mean(); sd=Xtr.std()+1e-12
    A=(Xtr-mu)/sd; B=(Xte-mu)/sd
    pred=[]
    for z in B:
        d=np.mean((A-z)**2,axis=1)
        pred.append(ytr[int(np.argmin(d))])
    return np.asarray(pred)

def metrics(y,p):
    e=np.abs(mm(p)-mm(y))
    return {'n':int(len(e)),'mae_mm':float(e.mean()),'median_mm':float(np.median(e)),
            'p90_mm':float(np.quantile(e,.9)),'within_5mm':float(np.mean(e<=5)),
            'within_10mm':float(np.mean(e<=10)),'max_mm':float(e.max())}

paths={k:get(k,u) for k,u in FILES.items()}
X,y=load(paths['noise_free']); Xi,yi=load(paths['id10']); Xo,yo=load(paths['ood'])
# Frozen alternating-position split: train indices 0,2,...; held-out interpolation indices 1,3,...
tr=np.arange(len(y))%2==0; te=~tr
# Models: raw nearest-neighbour baseline, PCA+Ridge baseline, CoreSyn multidimensional proxy (engineered descriptors + Ridge).
raw_nn=lambda Z: nearest_predict(X[tr],y[tr],Z)
pca=make_pipeline(StandardScaler(),PCA(n_components=min(20,tr.sum()-1),random_state=20260826),Ridge(alpha=1.0))
pca.fit(X[tr],y[tr])
F=engineered(X); Fi=engineered(Xi); Fo=engineered(Xo)
core=make_pipeline(StandardScaler(),Ridge(alpha=10.0))
core.fit(F[tr],y[tr])

rows=[]; preds=[]
def evalset(setname,Z,Y,FZ,mask=None):
    if mask is None: mask=np.ones(len(Y),dtype=bool)
    models={'nearest_raw':raw_nn(Z[mask]),'pca_ridge':pca.predict(Z[mask]),'coresyn_ndt_proxy':core.predict(FZ[mask])}
    for name,p in models.items():
        m=metrics(Y[mask],p); rows.append({'dataset':setname,'model':name,**m})
        for yt,yp in zip(Y[mask],p): preds.append({'dataset':setname,'model':name,'true_norm':float(yt),'pred_norm':float(yp),'true_mm':float(mm(yt)),'pred_mm':float(mm(yp)),'abs_err_mm':float(abs(mm(yp)-mm(yt)))})

evalset('noise_free_holdout',X,y,F,te)
evalset('id10_all',Xi,yi,Fi)
evalset('ood_10_5db',Xo,yo,Fo)

# Bootstrap the held-out rows for uncertainty on MAE (model predictions fixed, resample cases).
rng=np.random.default_rng(20260826)
boot=[]
for model in ['nearest_raw','pca_ridge','coresyn_ndt_proxy']:
    sub=pd.DataFrame(preds); sub=sub[(sub.dataset=='noise_free_holdout')&(sub.model==model)]
    e=sub.abs_err_mm.to_numpy()
    vals=[float(np.mean(rng.choice(e,size=len(e),replace=True))) for _ in range(2000)]
    boot.append({'model':model,'mae_boot_mean':float(np.mean(vals)),'mae_ci_low':float(np.quantile(vals,.025)),'mae_ci_high':float(np.quantile(vals,.975))})

pd.DataFrame(rows).to_csv(OUT/'metrics.csv',index=False)
pd.DataFrame(preds).to_csv(OUT/'predictions.csv',index=False)
pd.DataFrame(boot).to_csv(OUT/'bootstrap.csv',index=False)
manifest={'source_repo':'imakafanxy/UltrasonicData_Bristol','canonical_doi':'10.48804/JAIG58','source_files':{k:{'url':FILES[k],'sha256':sha256(p),'bytes':p.stat().st_size} for k,p in paths.items()},'split':'alternating positions: even-index train, odd-index holdout','seed':20260826,'claim_guardrail':'coresyn_ndt_proxy is an exploratory multidimensional proxy, not canonical NS-MDS'}
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2))
summary={'metrics':rows,'bootstrap':boot,'manifest':manifest}
(OUT/'summary.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
