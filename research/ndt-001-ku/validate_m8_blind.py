"""M8: pre-specified blind validation gate for NDT-001 KU.

This script intentionally freezes the challenger from M5/M6 (two nearest
training waveforms, inverse-square distance interpolation) and evaluates it
on a deterministic held-out subset that was not used for M5/M6 model tuning.

Guardrail: this is an internal blind re-split, not third-party or industrial
validation, and it does not establish canonical NS-MDS attribution.
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from urllib.request import urlopen
from io import BytesIO

OUT = Path(__file__).parent / "results_m8"
OUT.mkdir(parents=True, exist_ok=True)
URL = "https://raw.githubusercontent.com/imakafanxy/UltrasonicData_Bristol/main/UltraSonic%20guided-wave%20sig/OOD%20ultrasonic%20guided-wave%20signals/Noise-free%20normalized%20delamination%20damage%20position%20at%200%20to%201.csv"
SEED = 20260827


def load():
    raw = urlopen(URL, timeout=60).read()
    df = pd.read_csv(BytesIO(raw), header=None)
    # Same orientation convention as the frozen benchmark: rows are samples
    # after transpose when signals are stored by columns.
    if df.shape[0] > df.shape[1]:
        df = df.T
    a = df.apply(pd.to_numeric, errors="coerce").to_numpy(float)
    a = a[np.isfinite(a).all(axis=1)]
    return a


def predict(train_x, train_y, x):
    d = np.linalg.norm(train_x - x, axis=1)
    ix = np.argsort(d)[:2]
    dd = np.maximum(d[ix], 1e-12)
    w = 1.0 / (dd ** 2)
    return float(np.sum(w * train_y[ix]) / np.sum(w))


def main():
    X = load()
    n = len(X)
    # Position labels are equally spaced across the public 0..1 damage-position
    # series, matching the benchmark's position-index interpretation.
    y = np.linspace(0.0, 1000.0, n)

    # Freeze a deterministic 20% blind subset before evaluation. Remaining 80%
    # are reference library. No labels from blind subset affect prediction.
    rng = np.random.default_rng(SEED)
    blind = np.sort(rng.choice(n, size=max(1, n // 5), replace=False))
    train = np.setdiff1d(np.arange(n), blind)

    pred = np.array([predict(X[train], y[train], X[i]) for i in blind])
    err = np.abs(pred - y[blind])
    baseline = np.array([y[train][np.argmin(np.linalg.norm(X[train]-X[i], axis=1))] for i in blind])
    berr = np.abs(baseline - y[blind])

    result = {
        "gate": "M8 internal blind validation",
        "seed": SEED,
        "n_total": int(n),
        "n_blind": int(len(blind)),
        "baseline_mae_mm": float(berr.mean()),
        "challenger_mae_mm": float(err.mean()),
        "relative_mae_reduction_pct": float(100*(berr.mean()-err.mean())/berr.mean()) if berr.mean() else None,
        "challenger_median_mm": float(np.median(err)),
        "challenger_p90_mm": float(np.quantile(err, .9)),
        "challenger_max_mm": float(err.max()),
        "challenger_better_count": int(np.sum(err < berr)),
        "challenger_worse_count": int(np.sum(err > berr)),
        "pass_rule": "challenger MAE < nearest-neighbor MAE on pre-specified blind subset",
        "pass": bool(err.mean() < berr.mean()),
        "tuning_on_blind_labels": False,
        "guardrail": "internal blind re-split only; not independent third-party/industrial validation; not canonical NS-MDS attribution"
    }
    pd.DataFrame({"index": blind, "true_mm": y[blind], "baseline_mm": baseline, "challenger_mm": pred, "baseline_error_mm": berr, "challenger_error_mm": err}).to_csv(OUT/"blind_predictions.csv", index=False)
    (OUT/"summary.json").write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
