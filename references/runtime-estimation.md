# Runtime Estimation

Use this reference when a user asks how long an agent task may run, wants an overnight goal, or wants to use a long time window well.

## Ground Truth To Remember

Runtime is an estimate, not a guarantee. Agent wall-clock time changes with model speed, tool latency, network quality, repo size, test duration, browser/PDF rendering, external services, approval pauses, and how many verification loops are useful.

Do not claim exact hours. Give a range and explain what drives it.

Local Codex history on the maintainer machine showed this rough distribution across completed turns:

- median around 4 minutes
- 75th percentile around 11 minutes
- 90th percentile around 19 minutes
- 95th percentile around 27 minutes
- a small number of large tasks reached 1-2 hours

This means ordinary turns often finish quickly. Overnight usage requires deliberately designing a larger, evidence-heavy goal, not merely asking the agent to "keep working".

Public guidance is directionally consistent: Codex supports long-running `/goal` work, but "long-horizon" means the goal has enough meaningful work and feedback loops, not that every prompt automatically runs for hours.

## Time Bands

Use these bands internally when drafting goals. In user-facing output, give only the estimated time range and the reason. Do not label the task as short, standard, deep, or overnight.

- **15 分钟内**: answer, small edit, single lookup, tiny bug fix, one command check.
- **15-60 分钟**: bounded research, one-file change, simple doc, narrow debug, small script, quick repo inspection.
- **1-3 小时**: multi-file repair, medium feature, polished document/PDF, market scan, setup plus tests, browser verification.
- **3-8 小时**: large research synthesis, production-quality artifact, complex data pipeline, cross-browser/frontend polish, package/release prep, multi-source intelligence system, many examples plus validation.
- **超过 8 小时或无法安全估算**: needs login/2FA, payment, production deployment, irreversible operations, ambiguous product choices, legal/medical/financial judgment, large external waits, or repeated human approvals.

## Overnight Expansion Patterns

If the user wants to use a night well, only expand with useful loops:

- broaden source discovery across named channels and record source quality
- build a baseline first, then compare alternatives
- add representative examples and edge cases
- add validation scripts, smoke tests, browser checks, screenshots, or rendered artifact checks
- run tests after each meaningful change and inspect logs before retrying
- produce documentation, usage notes, release notes, and a final handoff summary
- add a "second-pass polish" phase after first completion evidence
- create a failure report when blocked instead of silently spinning
- convert the desired time window into a core goal plus an ordered extension pool

Never expand by:

- browsing unrelated sources
- refactoring unrelated files
- retrying the same failing command without new evidence
- adding features the user did not ask for
- touching credentials, payments, production data, or destructive operations

## Reverse Planning From Desired Duration

When the user says "希望跑 4 小时", "睡前跑到明早", "尽量用满晚上", or gives a deadline window, draft the goal from the time budget backward:

1. **Core deliverable first**: define the smallest complete result that would satisfy the original request.
2. **Natural runtime**: estimate how long that core work likely takes without padding.
3. **Target window**: compare the natural runtime with the user's desired duration.
4. **Extension pool**: add adjacent work only if it improves the same result. Good extensions include broader discovery, more comparisons, more examples, visual or browser QA, test matrix expansion, edge-case handling, documentation, packaging, release notes, and final risk review.
5. **Priority order**: tell the agent to complete core delivery first, then run extensions in value order until the target window is mostly used or completion evidence is strong.
6. **Stop rule**: if all useful core and extension work is complete early, stop and hand off evidence instead of filling time.
7. **Pause rule**: pause for credentials, payment, production, destructive operations, regulated judgment, public release, unclear ownership, or repeated failures without new evidence.

Useful phrasing:

- "自然耗时约 1-2 小时；如果你希望跑 6 小时，会把剩余时间投入到二轮验证、更多样例、文档和风险复查。"
- "这个需求本身可能 20-40 分钟完成。可以扩展到 2 小时做更完整的测试和交付说明，但不建议硬拉到一整晚。"
- "目标窗口 6-8 小时可行，因为有足够的收集、制作、渲染检查、二轮修正和示例扩展空间。"
- "如果提前完成所有有价值工作，agent 应该交付结果和证据，而不是继续无关探索。"

## Output Pattern

When time matters, add this field to the goal:

预计耗时：约 X-Y。若目标窗口是 N 小时，先完成核心交付，再按优先级把剩余时间用于 A/B/C 等有价值验证与打磨；若提前达到完成条件，应停止并交付证据，不为耗时继续扩展。

In the explanation, use plain language:

- "预计 20-40 分钟，强行拉到一整晚没有意义。"
- "预计 1-3 小时，主要时间会花在验证、示例和文档上。"
- "预计 4-6 小时，因为有足够的收集、制作、校验和二轮改进空间。"
- "暂时无法安全估算完整耗时，关键节点需要人工批准。"
