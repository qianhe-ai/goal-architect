# Goal Archetypes

Use this reference to adapt a vague request into a concrete agent objective.

## Archetype Selection

| Archetype | Use When | Default Shape |
|---|---|---|
| Discovery | Facts are uncertain or sources matter | inspect, cite, summarize, recommend |
| Decision | The user needs a choice | compare, score, trade off, decide |
| Delivery | A concrete artifact is needed | create, polish, verify, document, hand over |
| Repair | Something is broken | reproduce, isolate, patch, prove |
| Operating System | A repeatable workflow is needed | build loop, sample run, feedback path, operating notes |
| High-risk | Accounts, money, production, law, medical, finance, privacy, or destructive actions appear | discovery-only or pause-before-action |

## Evidence Menu

Pick evidence that matches the work:

- Code: tests, lint, typecheck, build, local run, logs, diff, usage notes.
- UI: desktop/mobile screenshots, no overlap, keyboard/mouse workflow, console logs.
- Documents: rendered PDF/DOCX, page count, visual review, source links, checklist, delivery summary.
- Research: source table, quote-limited citations, uncertainty notes, recommendation.
- Automation: sample input, sample output, run log, retry behavior, notification proof, operator instructions.
- Data: row counts, schema checks, before/after samples, validation query.

## Exclusion Prompts

Add non-goals when any of these appear:

- "做个系统": exclude full platform, login, billing, admin, deployment unless requested.
- "优化": exclude broad rewrite, unrelated refactor, new business logic.
- "帮我搜": exclude paid/private data, unverified rumors as facts, account actions.
- "自动化": exclude CAPTCHA bypass, 2FA handling, unapproved messaging/purchasing/posting.
- "设计": exclude full brand rebuild, marketing site, unrelated visual identity changes.
- "修复": exclude architecture replacement unless root cause proves it is required.

## Sample Refinements

### Discovery

```text
/goal 完成关于指定主题的可核验调研，输出一份带来源、结论、机会、风险和下一步建议的简报。
验证：至少核对指定材料和权威公开来源，列出来源链接、发布日期、可信度和未确认信息。
约束：不把社媒传言当事实，不替用户做法律/金融/医疗结论，不使用付费或私密数据。
边界：只读取公开网页和用户提供文件，不登录账号、不写入外部系统。
非目标：不直接执行购买、发布、注册、投资或生产变更。
迭代策略：先建立问题清单，再按可信度搜证；来源冲突时优先一手材料并标注不确定性。
完成条件：交付一份可审阅简报，并清楚区分事实、判断和建议。
暂停条件：需要登录、付费数据、私密材料、监管判断或用户授权时暂停。
```

### Delivery

```text
/goal 创建指定交付物的一版完整可审阅成果，覆盖核心使用流程、基础质量打磨、必要说明和交付总结，并保留现有风格和已给边界。
验证：打开或运行成品，用样例输入完成一次核心流程，检查日志/截图/导出文件/渲染结果，并确认说明文档或交付备注包含使用方式、输出路径和剩余风险。
约束：不加入账号、支付、云同步、生产部署、无关后端或用户未要求的高级功能。
边界：只写入新建目录或与交付物直接相关的文件。
非目标：不做完整商业化、不发布上线、不扩展到第二阶段功能或外部账号接入。
迭代策略：先完成主体交付，再根据证据做最多 3 轮聚焦质量修正，最后补充使用说明和剩余风险。
完成条件：成品路径明确，核心流程可复现，验证证据和交付说明均可审阅。
暂停条件：需要凭证、付费服务、生产数据、版权素材、公开发布或重大方向取舍时暂停。
```

### Repair

```text
/goal 修复指定异常，先复现并定位根因，再做最小必要改动。
验证：记录复现方式，运行相关检查，证明原异常消失且直接相关行为没有回归。
约束：不删除用户数据，不改生产配置，不做无关重构。
边界：只修改故障链路相关文件、测试和必要夹具。
非目标：不新增功能、不重做架构、不优化无关性能。
迭代策略：每次改动后验证；同一假设失败两次后必须换证据来源或缩小复现。
完成条件：原问题有修复证据，剩余风险被列出。
暂停条件：无法复现、需要生产凭证、破坏性数据操作或产品规则判断时暂停。
```

### Operating System

```text
/goal 建立指定工作流的一版完整本地闭环，让样例输入能经过采集、处理、输出和反馈路径，并配套基础配置样例、运行说明、失败处理说明和下一步扩展建议。
验证：用样例输入跑通全流程，保留运行日志、输出文件、失败处理说明、配置样例和下一步扩展入口。
约束：先做本地或低风险版本，不依赖未授权账号、付费 API、私密数据或生产服务器。
边界：只写入系统目录、配置样例、说明文档和必要脚本。
非目标：不追求无人值守全自动，不接入敏感账号，不对外发布。
迭代策略：先保证闭环可重复，再补错误处理、反馈表、运行说明和扩展建议。
完成条件：样例任务可重复运行，用户知道如何启动、检查、排错和扩展。
暂停条件：需要长期凭证、预算、生产部署、隐私数据或合规审批时暂停。
```

## Compact Question Set

Ask at most three questions when defaults are unsafe:

1. Result: do you want diagnosis, recommendation, artifact, or running system?
2. Evidence: should completion be proven by tests/logs, screenshots, rendered files, source links, or sample output?
3. Risk: may the agent touch accounts, paid services, production data, or public release?
