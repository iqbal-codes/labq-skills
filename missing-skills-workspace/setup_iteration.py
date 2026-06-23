import json
from pathlib import Path

SKILLS = ["bootstrap", "discover", "imprint", "remember", "syncdocs"]
BASE = Path("missing-skills-workspace/iteration-1")
count = 0
for skill in SKILLS:
    data = json.loads(Path(f"skills/{skill}/evals/evals.json").read_text())
    if data["skill_name"] != skill:
        raise SystemExit(f"skill_name mismatch for {skill}")
    for ev in data["evals"]:
        eval_name = f"{skill}-eval-{ev['id']}"
        d = BASE / eval_name
        (d / "with_skill" / "outputs").mkdir(parents=True, exist_ok=True)
        (d / "without_skill" / "outputs").mkdir(parents=True, exist_ok=True)
        metadata = {
            "eval_id": ev["id"],
            "eval_name": eval_name,
            "skill_name": skill,
            "prompt": ev["prompt"],
            "assertions": ev.get("expectations", []),
        }
        (d / "eval_metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")
        count += 1
print(f"created {count} eval metadata files")
