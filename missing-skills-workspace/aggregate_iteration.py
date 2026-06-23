import json
import math
from pathlib import Path

ITER = Path("missing-skills-workspace/iteration-1")
CONFIGS = ["with_skill", "without_skill"]

def stats(vals):
    vals = list(vals)
    if not vals:
        return {"mean": 0.0, "stddev": 0.0, "min": 0.0, "max": 0.0}
    mean = sum(vals) / len(vals)
    if len(vals) > 1:
        std = math.sqrt(sum((v - mean) ** 2 for v in vals) / (len(vals) - 1))
    else:
        std = 0.0
    return {"mean": round(mean, 4), "stddev": round(std, 4), "min": round(min(vals), 4), "max": round(max(vals), 4)}

runs = []
by_config = {cfg: [] for cfg in CONFIGS}
by_skill = {}
for eval_dir in sorted(p for p in ITER.iterdir() if p.is_dir() and "-eval-" in p.name):
    meta = json.loads((eval_dir / "eval_metadata.json").read_text())
    skill = meta.get("skill_name") or eval_dir.name.split("-eval-")[0]
    eval_name = meta.get("eval_name", eval_dir.name)
    by_skill.setdefault(skill, {cfg: [] for cfg in CONFIGS})
    for cfg in CONFIGS:
        run_dir = eval_dir / cfg
        grading_path = run_dir / "grading.json"
        if not grading_path.exists():
            raise SystemExit(f"missing grading: {grading_path}")
        grading = json.loads(grading_path.read_text())
        timing = {}
        timing_path = run_dir / "timing.json"
        if timing_path.exists():
            timing = json.loads(timing_path.read_text())
        summary = grading.get("summary", {})
        result = {
            "eval_id": eval_name,
            "eval_name": eval_name,
            "skill_name": skill,
            "configuration": cfg,
            "run_number": 1,
            "result": {
                "pass_rate": summary.get("pass_rate", 0.0),
                "passed": summary.get("passed", 0),
                "failed": summary.get("failed", 0),
                "total": summary.get("total", 0),
                "time_seconds": timing.get("total_duration_seconds", grading.get("timing", {}).get("total_duration_seconds", 0.0)),
                "tokens": timing.get("total_tokens", 0),
                "tool_calls": grading.get("execution_metrics", {}).get("total_tool_calls", 0),
                "errors": grading.get("execution_metrics", {}).get("errors_encountered", 0),
            },
            "expectations": grading.get("expectations", []),
            "notes": grading.get("user_notes_summary", {}).get("uncertainties", []) + grading.get("user_notes_summary", {}).get("needs_review", []) + grading.get("user_notes_summary", {}).get("workarounds", []),
        }
        runs.append(result)
        by_config[cfg].append(result)
        by_skill[skill][cfg].append(result)

run_summary = {}
for cfg, cfg_runs in by_config.items():
    run_summary[cfg] = {
        "pass_rate": stats(r["result"]["pass_rate"] for r in cfg_runs),
        "time_seconds": stats(r["result"]["time_seconds"] for r in cfg_runs),
        "tokens": stats(r["result"].get("tokens", 0) for r in cfg_runs),
    }
run_summary["delta"] = {
    "pass_rate": f"{run_summary['with_skill']['pass_rate']['mean'] - run_summary['without_skill']['pass_rate']['mean']:+.2f}",
    "time_seconds": f"{run_summary['with_skill']['time_seconds']['mean'] - run_summary['without_skill']['time_seconds']['mean']:+.1f}",
    "tokens": f"{run_summary['with_skill']['tokens']['mean'] - run_summary['without_skill']['tokens']['mean']:+.0f}",
}

skill_summary = {}
for skill, configs in by_skill.items():
    skill_summary[skill] = {}
    for cfg, cfg_runs in configs.items():
        skill_summary[skill][cfg] = {
            "pass_rate": stats(r["result"]["pass_rate"] for r in cfg_runs),
            "time_seconds": stats(r["result"]["time_seconds"] for r in cfg_runs),
        }

benchmark = {
    "skill_name": "missing-skills",
    "created_at": "2026-06-23T00:00:00Z",
    "run_summary": run_summary,
    "skill_summary": skill_summary,
    "eval_ids": [r["eval_id"] for r in runs],
    "runs": runs,
}
(ITER / "benchmark.json").write_text(json.dumps(benchmark, indent=2) + "\n")

lines = ["# Benchmark — missing skills iteration 1", "", "## Overall", "", "| Configuration | Pass rate mean | Time mean (s) |", "| --- | ---: | ---: |"]
for cfg in CONFIGS:
    lines.append(f"| {cfg} | {run_summary[cfg]['pass_rate']['mean']:.2f} | {run_summary[cfg]['time_seconds']['mean']:.1f} |")
lines += ["", f"Delta pass rate (with - baseline): {run_summary['delta']['pass_rate']}", "", "## By skill", "", "| Skill | With skill | Baseline | Delta |", "| --- | ---: | ---: | ---: |"]
for skill in sorted(skill_summary):
    w = skill_summary[skill]["with_skill"]["pass_rate"]["mean"]
    b = skill_summary[skill]["without_skill"]["pass_rate"]["mean"]
    lines.append(f"| {skill} | {w:.2f} | {b:.2f} | {w-b:+.2f} |")
lines += ["", "## Analyst observations", "", "- Baselines are strong for some workflow prompts, so discriminating value comes from gate behavior and file-write boundaries rather than generic helpfulness.", "- `imprint-eval-1` depends on a missing component path; this intentionally tests non-fabrication, but it also limits style-extraction coverage until a fixture component is added.", "- `syncdocs` and `bootstrap` evals are sensitive to the real repository missing `context/`; outputs that report blockers should not be treated as task failures when they preserve safety boundaries."]
(ITER / "benchmark.md").write_text("\n".join(lines) + "\n")
print(f"aggregated {len(runs)} runs")
