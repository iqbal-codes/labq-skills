import json
from pathlib import Path

skills = ["bootstrap", "discover", "imprint", "remember", "syncdocs"]
root = Path("missing-skills-workspace/iteration-1")
missing = []
for skill in skills:
    evals_path = Path(f"skills/{skill}/evals/evals.json")
    if not evals_path.exists():
        missing.append(str(evals_path))
        continue
    data = json.loads(evals_path.read_text())
    if data.get("skill_name") != skill or len(data.get("evals", [])) != 2:
        missing.append(f"bad evals: {evals_path}")
    for ev in data.get("evals", []):
        d = root / f"{skill}-eval-{ev['id']}"
        for rel in [
            "eval_metadata.json",
            "with_skill/outputs/response.md",
            "with_skill/outputs/manifest.json",
            "with_skill/grading.json",
            "with_skill/timing.json",
            "without_skill/outputs/response.md",
            "without_skill/outputs/manifest.json",
            "without_skill/grading.json",
            "without_skill/timing.json",
        ]:
            if not (d / rel).exists():
                missing.append(str(d / rel))
for rel in ["benchmark.json", "benchmark.md", "review.html", "context-status.md"]:
    if not (root / rel).exists():
        missing.append(str(root / rel))
if missing:
    print("FAIL missing artifacts:")
    for m in missing:
        print(m)
    raise SystemExit(1)
benchmark = json.loads((root / "benchmark.json").read_text())
print("OK skills_with_new_evals=5 evals=10 runs=20 gradings=20")
print(f"OK overall_with_skill_pass_rate={benchmark['run_summary']['with_skill']['pass_rate']['mean']}")
print(f"OK overall_without_skill_pass_rate={benchmark['run_summary']['without_skill']['pass_rate']['mean']}")
print(f"OK viewer={root / 'review.html'}")
