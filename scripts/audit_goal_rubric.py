#!/usr/bin/env python3
"""Minimal rubric audit for goal drafts produced by goal-architect."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


CHECKPOINTS = {
    "slash_goal": [r"^\s*/goal\b"],
    "proof": [r"验证[:：]", r"Verification[:：]"],
    "rules": [r"约束[:：]", r"Constraints[:：]"],
    "perimeter": [r"边界[:：]", r"Boundaries[:：]"],
    "excluded_work": [r"非目标[:：]", r"Non[- ]?goals?[:：]"],
    "retry_plan": [r"迭代策略[:：]", r"Iteration policy[:：]"],
    "done_signal": [r"完成条件[:：]", r"停止条件[:：]", r"Stop when[:：]"],
    "handoff_signal": [r"暂停条件[:：]", r"阻塞条件[:：]", r"Pause if[:：]"],
}

UNKNOWN_TOKENS = [
    r"\[[^\]]+\]",
    r"<[^>]+>",
    r"\bTODO\b",
    r"\bTBD\b",
    r"待定",
    r"待补充",
]

WEAK_PHRASES = [
    r"make sure it works",
    r"edit anything",
    r"change whatever",
    r"keep trying",
    r"until it (looks|seems|feels) good",
    r"随便改",
    r"随意修改",
    r"一直尝试",
    r"直到满意",
    r"感觉可以",
    r"看起来不错",
]

PROOF_TERMS = [
    r"运行",
    r"启动",
    r"打开",
    r"测试",
    r"构建",
    r"检查",
    r"截图",
    r"日志",
    r"产物",
    r"文件",
    r"链接",
    r"浏览器",
    r"样例",
    r"导出",
    r"渲染",
    r"API",
    r"run",
    r"start",
    r"open",
    r"test",
    r"build",
    r"lint",
    r"screenshot",
    r"log",
    r"artifact",
    r"file",
    r"sample",
    r"browser",
    r"export",
]


def contains(text: str, patterns: list[str], flags: int = re.IGNORECASE | re.MULTILINE) -> bool:
    return any(re.search(pattern, text, flags=flags) for pattern in patterns)


def first_payload(text: str, patterns: list[str]) -> str:
    for pattern in patterns:
        match = re.search(rf"^\s*{pattern}\s*(.+)$", text, flags=re.IGNORECASE | re.MULTILINE)
        if match:
            return match.group(1).strip()
    return ""


def evaluate(text: str, label: str) -> dict:
    notes: list[str] = []
    grade = 100
    coverage: dict[str, bool] = {}

    for name, markers in CHECKPOINTS.items():
        present = contains(text, markers)
        coverage[name] = present
        if not present:
            notes.append(f"missing checkpoint: {name}")
            grade -= 9

    if re.search(r"^\s*/目标\b", text, flags=re.MULTILINE):
        notes.append("slash command should be /goal, not /目标")
        grade -= 12

    goal_line = next((line.strip() for line in text.splitlines() if line.strip().startswith("/goal")), "")
    if goal_line and len(goal_line.replace("/goal", "", 1).strip()) < 24:
        notes.append("goal result is too thin")
        grade -= 8

    for pattern in UNKNOWN_TOKENS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            notes.append(f"unresolved token: {pattern}")
            grade -= 12

    for pattern in WEAK_PHRASES:
        if re.search(pattern, text, flags=re.IGNORECASE):
            notes.append(f"weak or risky phrase: {pattern}")
            grade -= 10

    proof_text = first_payload(text, CHECKPOINTS["proof"])
    if proof_text and not contains(proof_text, PROOF_TERMS):
        notes.append("proof line should name observable evidence")
        grade -= 10

    perimeter_text = first_payload(text, CHECKPOINTS["perimeter"])
    if perimeter_text and re.search(r"(所有|全部|任意|整台|整个|anything|whatever|entire|whole)", perimeter_text, flags=re.IGNORECASE):
        notes.append("perimeter may be too broad")
        grade -= 10

    return {
        "path": label,
        "grade": max(grade, 0),
        "ok": grade >= 80 and all(coverage.values()),
        "coverage": coverage,
        "notes": notes,
    }


def main(args: list[str]) -> int:
    if len(args) < 2:
        print("Usage: audit_goal_rubric.py <goal-file> [<goal-file> ...]", file=sys.stderr)
        return 2

    reports = []
    for raw in args[1:]:
        path = Path(raw)
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            reports.append({"path": str(path), "grade": 0, "ok": False, "coverage": {}, "notes": [str(exc)]})
            continue
        reports.append(evaluate(text, str(path)))

    print(json.dumps(reports, ensure_ascii=False, indent=2))
    return 0 if all(item["ok"] for item in reports) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
