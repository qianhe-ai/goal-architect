---
name: goal-architect
description: Refine fuzzy intentions, project ideas, and incomplete task requests into a complete, longer-running, agent-ready objective with a clear user outcome, evidence plan, scope guardrails, reasonable extensions, excluded work, risk triggers, and a readable copy-ready Codex `/goal` block. Use when the user asks to polish a goal, improve task instructions, turn a plan into an executable agent objective, write a Goal 指令, define acceptance criteria, diagnose an overly vague request, or prepare Codex/Claude Code/OpenClaw work that should run autonomously for a substantial task.
---

# Goal Architect

Improve the goal before the work begins. The skill turns a human's rough intent into an execution charter that lets an agent do a more complete one-pass job without widening into risky or unrelated work. It also adds a practical runtime estimate when time matters.

## Core Idea

Use a three-layer refinement path:

1. **Intent Map**: identify who benefits, what result matters, and what the user may have implied but not said.
2. **Evidence Plan**: define observable proof, not taste words or confidence phrases.
3. **Execution Envelope**: set reasonable extensions, allowed actions, excluded work, retry rules, completion criteria, and handoff triggers.

Only after those three layers are clear, produce the `/goal` block.

## Behavior Rules

- Keep Codex output as `/goal` by default. If the user targets Claude Code, OpenClaw, OpenCode, or a generic agent surface that may not support `/goal`, output a "通用 Agent 执行版" with the same labels instead of relying on the slash command.
- Use Chinese by default for Chinese users.
- Do not run the generated goal unless the user explicitly asks.
- Make conservative assumptions for low-risk gaps and state them.
- Prefer a complete bounded target over a thin MVP: when the user is vague, design a goal that can occupy one substantial agent run and usually includes context discovery, implementation or production, quality checks, documentation, and a handoff summary.
- Reasonably extend the user's request when it improves the likely result, but keep those extensions inside the stated outcome and mark larger product or external actions as non-goals.
- When the user wants a long run, overnight run, "尽量跑久一点", gives a desired duration, or asks how long an agent task may take, estimate the natural runtime before writing the goal. Do not name the task as "short", "standard", "deep", or "overnight" in user-facing output.
- If the user gives a target duration or time window, plan backward from that window: preserve the core result, then add a useful extension pool, verification depth, documentation, packaging, examples, and a hard stop rule. Make clear what belongs to the required goal and what only runs if time remains.
- Use a time budget only for useful work: discovery, implementation, verification, iteration, examples, documentation, packaging, regression checks, and handoff. Never pad time with unrelated exploration.
- If the request is naturally short, say it may finish early and propose valuable extensions, a follow-up automation/checkpoint, or a wider but still relevant scope instead of pretending it can fill the night.
- Ask a question only when the answer changes budget, account access, ownership, public release, production systems, legal/medical/financial exposure, destructive changes, or product direction.
- Convert vague words into proof:
  - "高级/专业/好看" -> screenshots, spacing, hierarchy, readability, responsiveness, no overlap
  - "稳定/可用" -> repeatable workflow, logs, tests, sample data, failure behavior
  - "完善" -> named missing pieces, acceptance checklist, out-of-scope list
- Put the user's desired result first. Put scoring, boundaries, non-goals, and risks after the result summary.
- Do not put the full executable version in a fenced code block by default; long code-style boxes often do not wrap well. Use normal Markdown lines under a "可复制执行版" heading. Use a code block only if the user explicitly asks.

## Refinement Flow

1. Identify the planning posture internally: discovery, decision, delivery, repair, operating system, or high-risk. Do not show this as a task type label unless the user asks.
2. Rewrite the request as a user-visible or artifact-visible result.
3. State one default assumption when the input is vague but low-risk.
4. Estimate natural runtime as a range:
   - under 15 minutes: answer, small edit, single lookup, tiny fix
   - 15-60 minutes: bounded research, one-file change, simple document, narrow debug
   - 1-3 hours: multi-file repair, medium feature, polished document/PDF, market scan, setup plus validation
   - 3-8 hours: large research synthesis, production-quality artifact, cross-browser/frontend polish, data pipeline, multi-source analysis, full package/release preparation
   - over 8 hours or cannot be estimated safely: credentials, human review, long external waits, production systems, large migrations, or ambiguous product decisions
5. If the user gives a desired duration, reverse-plan from that target:
   - name the minimum core deliverable that must be completed first
   - compare natural runtime with the desired window
   - build an extension pool that improves the same outcome without changing the user's intent
   - order extensions by value: more evidence, more examples, stronger QA, better docs, cleaner packaging, wider source coverage, final risk report
   - state that the agent should stop and hand off when completion evidence is reached, even if time remains
6. If the user wants to fill a night, add an expansion plan only when it improves the result: broader source collection, baseline comparison, test matrix, visual QA, multiple examples, documentation, packaging, release notes, and final risk report. Include a stopping rule so completion still wins over time padding.
7. Add a "complete-pass" plan: likely phases such as discovery, build/write, verify, refine, document, and summarize.
8. Pick evidence: command output, screenshots, rendered files, exported docs, logs, sample records, API responses, browser checks, or review checklist.
9. Draw the action perimeter: writable locations, touched systems, accounts, data, services, and forbidden areas.
10. Add exclusions so the agent does not silently build adjacent features.
11. Add retry behavior: what evidence to inspect before changing strategy and when repeated failure should stop.
12. Add handoff triggers for credentials, payment, production, private data, destructive operations, compliance, copyright, or unclear ownership.
13. Pick the output surface:
   - Codex: use `/goal` as the executable line
   - Claude Code/OpenClaw/OpenCode/generic agents: use "目标：" as the executable first line and keep the same fields as normal text
   - unclear target: default to Codex and mention that the same fields can be copied into other agents
14. Grade the refined goal. If it cannot reach a solid grade, revise before showing it.

For reusable patterns, read `references/goal-archetypes.md` only when the request is broad, risky, or not clearly coding work. Read `references/runtime-estimation.md` when the user asks about duration, overnight work, long-running goals, or using a time budget well.

## Rubric

Score internally with five 0-20 checks:

- **Outcome**: one concrete result is named.
- **Proof**: completion can be observed.
- **Perimeter**: write/action boundaries are narrow enough.
- **Exclusions**: non-goals prevent scope creep.
- **Handoff**: human-only decisions and risk triggers are explicit.

If the draft is written to a file, run:

```bash
python3 scripts/audit_goal_rubric.py <goal-file>
```

## Response Shape

For Chinese users, prefer:

1. **规划结果**: first say what substantial result the agent will aim to deliver.
2. **执行范围概览**: list the main phases, such as context discovery, production, verification, refinement, documentation, and handoff.
3. **预计耗时**: state an estimated range and which useful loops may consume extra time. Do not add a duration category name.
4. **可复制执行版**: write the `/goal` and each label on separate normal Markdown lines, not inside a fenced code block.
5. **为什么这样规划**: explain the default assumptions briefly.
6. **可调整项**: offer short choices only when helpful.
7. **质量评估与风险**: put score, boundaries, non-goals, and risks after the main result.

Example shape:

规划结果：这次目标会让 agent 完成用户真正关心的主要结果，并顺带完成必要的上下文确认、质量检查和交付总结，最终交付可审阅证据。

执行范围概览：
- 先读取/确认上下文
- 再完成主体交付
- 然后验证、修正、补文档
- 最后输出路径、证据和剩余风险

预计耗时：约 ...；如果目标窗口是 ...，会先完成核心交付，再把剩余时间用于 ...；如果提前达到完成条件，以完成证据为准，不为耗时而扩展无关范围。

可复制执行版（多行普通文本，便于阅读和复制）

/goal ...

验证：...

预计耗时：...

约束：...

边界：...

非目标：...

迭代策略：...

完成条件：...

暂停条件：...

If the target is Claude Code, OpenClaw, OpenCode, or a generic agent, replace the command line with:

通用 Agent 执行版

目标：...

验证：...

预计耗时：...

约束：...

边界：...

非目标：...

迭代策略：...

完成条件：...

暂停条件：...

为什么这样规划：...

可调整项：...

质量评估与风险：...

If the user asks for only the final command, put the executable block first and keep all commentary short. Add a cross-tool mirror only when the target toolchain or user asks for it.

## Pass/Fail Standard

Pass:

- The `/goal` line contains a result, not just an action.
- Verification names evidence.
- Boundaries are narrower than "the whole repo/machine".
- Non-goals are present for any multi-step or creative task.
- Pause conditions cover auth, payment, production, destructive actions, regulated judgment, copyright, unclear ownership, and external approvals when relevant.
- The goal is substantial enough for one meaningful autonomous run unless the user explicitly asks for a tiny task.
- Duration estimate is present when the user asks for long-running, overnight, or time-budgeted work.

Fail and revise:

- The draft contains placeholders such as `[x]`, `<path>`, `TODO`, `TBD`, `待定`, or `待补充`.
- The goal depends on "looks good", "make sure it works", "随便改", "一直尝试", or similar language.
- The agent can alter unrelated systems.
- Success is subjective or unverifiable.
- Risky external action is allowed without explicit user confirmation.
- The goal tries to "use up time" through unrelated browsing, speculative refactors, or repetitive retries without new evidence.

## Differentiation

This skill is not only a `/goal` formatter. It should surface the hidden product/operational intent, expand vague requests into a complete but bounded one-pass objective, and put the user-visible result before metadata. It should work for software, documents, research, automations, knowledge bases, content operations, and business analysis.

## Resources

- `references/goal-archetypes.md`: archetypes, evidence options, exclusions, and sample refinements.
- `references/runtime-estimation.md`: empirical duration bands, overnight expansion patterns, and stop conditions.
- `scripts/audit_goal_rubric.py`: minimal file-based rubric audit for generated goal drafts.
