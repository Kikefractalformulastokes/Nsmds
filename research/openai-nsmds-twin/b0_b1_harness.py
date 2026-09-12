#!/usr/bin/env python3
import math
import json


def memory_euler(u_fn, tau, dt, t_end):
    m = 0.0
    t = 0.0
    vals = []
    n = int(round(t_end / dt))
    for _ in range(n):
        u = u_fn(t)
        m = m + dt * ((u - m) / tau)
        t += dt
        vals.append((t, m))
    return vals


def exact_memory_ramp(t, tau):
    # u(t)=t, m(t)=int_0^t tau^-1 exp(-(t-s)/tau) s ds
    return t - tau + tau * math.exp(-t / tau)


def b0_control_gate():
    # Residual model: R_exp = R_base - gamma*(D1-D2).
    samples = [
        (0.0, 0.0),
        (1.25, -0.4),
        (-3.0, 2.0),
        (1e-9, -2e-9),
    ]
    max_zero_diff = 0.0
    nonzero_detected = False
    for r_base, twin in samples:
        gamma = 0.0
        r_exp = r_base - gamma * twin
        max_zero_diff = max(max_zero_diff, abs(r_exp - r_base))

        gamma = 0.25
        r_exp_nonzero = r_base - gamma * twin
        if abs(twin) > 0 and abs(r_exp_nonzero - r_base) > 0:
            nonzero_detected = True

    passed = max_zero_diff == 0.0 and nonzero_detected
    return {
        "gate": "B0",
        "passed": passed,
        "max_gamma0_residual_difference": max_zero_diff,
        "nonzero_gamma_detected": nonzero_detected,
    }


def b1_memory_gate():
    tau = 0.7
    t_end = 4.0
    dts = [0.1, 0.05, 0.025, 0.0125]
    errors = []

    for dt in dts:
        vals = memory_euler(lambda t: t, tau=tau, dt=dt, t_end=t_end)
        t, m = vals[-1]
        exact = exact_memory_ramp(t, tau)
        err = abs(m - exact)
        errors.append(err)

    strictly_decreasing = all(errors[i + 1] < errors[i] for i in range(len(errors) - 1))
    finite = all(math.isfinite(e) for e in errors)
    refinement_ratio = errors[0] / errors[-1] if errors[-1] else float("inf")
    passed = strictly_decreasing and finite and refinement_ratio > 4.0

    return {
        "gate": "B1",
        "passed": passed,
        "tau": tau,
        "t_end": t_end,
        "dts": dts,
        "final_time_errors": errors,
        "strictly_decreasing": strictly_decreasing,
        "refinement_ratio_coarse_to_fine": refinement_ratio,
    }


def main():
    result = {
        "study": "OpenAI x NS-MDS Twin-Derivative Study",
        "amendment": "B0 v0.2",
        "B0": b0_control_gate(),
        "B1": b1_memory_gate(),
    }
    result["overall_passed"] = result["B0"]["passed"] and result["B1"]["passed"]
    print(json.dumps(result, indent=2, sort_keys=True))
    with open("b0_b1_results.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, sort_keys=True)
    if not result["overall_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
