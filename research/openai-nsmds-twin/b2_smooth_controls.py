#!/usr/bin/env python3
import json
import math

TAU1 = 0.18
TAU2 = 0.72
ALPHA = 1.0
BETA = 1.0
T_END = 8.0
DTS = [0.02, 0.01, 0.005]


def control_value(name, t):
    if name == "steady":
        return 1.0
    if name == "periodic":
        return math.sin(2.0 * math.pi * t / 2.5)
    if name == "decaying":
        return math.exp(-0.45 * t)
    if name == "high_gradient_smooth":
        # Entirely smooth, bounded transition with a deliberately steep but finite derivative.
        return math.tanh(8.0 * (t - 3.0))
    raise ValueError(name)


def control_derivative(name, t):
    if name == "steady":
        return 0.0
    if name == "periodic":
        w = 2.0 * math.pi / 2.5
        return w * math.cos(w * t)
    if name == "decaying":
        return -0.45 * math.exp(-0.45 * t)
    if name == "high_gradient_smooth":
        z = 8.0 * (t - 3.0)
        # Stable sech^2 evaluation through tanh.
        th = math.tanh(z)
        return 8.0 * (1.0 - th * th)
    raise ValueError(name)


def simulate(name, dt):
    m1 = 0.0
    m2 = 0.0
    t = 0.0
    s_values = []
    normalized = []
    tail_start = 4.0 * max(TAU1, TAU2)
    n = int(round(T_END / dt))

    for _ in range(n):
        u = control_value(name, t)
        du = control_derivative(name, t)
        m1 += dt * ((u - m1) / TAU1)
        m2 += dt * ((u - m2) / TAU2)
        t += dt
        u_next = control_value(name, t)
        du_next = control_derivative(name, t)
        d1 = du_next + ALPHA * (u_next - m1) / TAU1
        d2 = du_next + BETA * (u_next - m2) / TAU2
        s = abs(d1 - d2)
        scale = 1.0 + abs(u_next) + abs(du_next)
        sn = s / scale
        if t >= tail_start:
            s_values.append(s)
            normalized.append(sn)

    return {
        "dt": dt,
        "tail_max_s_twin": max(s_values),
        "tail_rms_s_twin": math.sqrt(sum(x*x for x in s_values) / len(s_values)),
        "tail_max_normalized": max(normalized),
        "finite": all(math.isfinite(x) for x in s_values + normalized),
    }


def assess_control(name):
    runs = [simulate(name, dt) for dt in DTS]
    finest = runs[-1]
    mid = runs[-2]

    # B2 is a smooth-null sanity gate, not a singularity classifier.
    # Required: finite signal and refinement stability of the bounded observable.
    denom = max(1e-12, abs(finest["tail_rms_s_twin"]))
    rel_refinement_change = abs(mid["tail_rms_s_twin"] - finest["tail_rms_s_twin"]) / denom
    bounded = finest["tail_max_normalized"] < 10.0
    refinement_stable = rel_refinement_change < 0.10
    finite = all(r["finite"] for r in runs)

    # A truly steady field should lose initialization transient and approach zero twin signal.
    steady_decay_ok = True
    if name == "steady":
        steady_decay_ok = finest["tail_max_s_twin"] < 0.03

    passed = finite and bounded and refinement_stable and steady_decay_ok
    return {
        "name": name,
        "passed": passed,
        "runs": runs,
        "relative_refinement_change_mid_to_fine": rel_refinement_change,
        "bounded_normalized_signal": bounded,
        "refinement_stable": refinement_stable,
        "steady_decay_ok": steady_decay_ok,
    }


def main():
    names = ["steady", "periodic", "decaying", "high_gradient_smooth"]
    controls = [assess_control(name) for name in names]
    result = {
        "study": "OpenAI x NS-MDS Twin-Derivative Study",
        "gate": "B2 smooth/null temporal controls",
        "scope_note": "These are scalar manufactured temporal controls for the twin-memory observable, not full 3D Navier-Stokes PDE solves and not evidence of singularity prediction.",
        "parameters": {
            "tau1": TAU1,
            "tau2": TAU2,
            "alpha": ALPHA,
            "beta": BETA,
            "t_end": T_END,
            "dts": DTS,
        },
        "controls": controls,
        "overall_passed": all(c["passed"] for c in controls),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    with open("b2_results.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, sort_keys=True)
    if not result["overall_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
