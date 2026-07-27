#!/usr/bin/env python3
"""Score DR readiness controls from 0=unknown to 2=proven."""
from __future__ import annotations
import argparse, json, pathlib
CONTROLS=("rpo_rto","backup_source","failover_path","restore_path","dependency_order","decision_ownership","technical_validation","business_validation","communications","evidence")

def score(payload: dict) -> dict:
    controls=payload.get("controls") or {}; errors=[]; values={}
    for name in CONTROLS:
        value=controls.get(name)
        if not isinstance(value,int) or value not in (0,1,2): errors.append(f"{name} must be 0, 1, or 2")
        else: values[name]=value
    total=sum(values.values())
    level="strong" if total>=19 else "exercised" if total>=15 else "documented" if total>=8 else "assumption-dependent"
    return {"score":total,"maximum":20,"level":level,"errors":errors,"controls":values}

def markdown(report: dict) -> str:
    lines=["# DR Readiness Score", "", f"Score: **{report['score']} / 20**", f"Level: **{report['level']}**", "", "| Control | Score |", "|---|---:|"]
    lines += [f"| {name.replace('_',' ').title()} | {value} |" for name,value in report["controls"].items()]
    if report["errors"]: lines += ["", "## Validation errors"]+[f"- {item}" for item in report["errors"]]
    return "\n".join(lines)+"\n"

def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument("input"); p.add_argument("--threshold",type=int,default=15); p.add_argument("--output",default="dr-readiness-report.md"); a=p.parse_args()
    report=score(json.loads(pathlib.Path(a.input).read_text(encoding="utf-8"))); pathlib.Path(a.output).write_text(markdown(report),encoding="utf-8"); print(json.dumps(report,indent=2))
    return 1 if report["errors"] or report["score"]<a.threshold else 0
if __name__=="__main__": raise SystemExit(main())
