> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 把耗时处理放到后台

ID：`scenario-background-jobs`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

耗时 / 大文件 / 任务 / 处理；后台 / 排队 / 异步 / 不阻塞 / 重试 / 进度。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 现有后端语言和队列是什么？
- 任务时限、幂等和结果保留要求是什么？

## 技术职责与候选

- [Celery](../technologies/tech-celery.md)：在 Worker 中执行异步任务。
- [BullMQ](../technologies/tech-bullmq.md)：管理后台任务、重试和调度。
- [RabbitMQ](../technologies/tech-rabbitmq.md)：将消息路由并交付给消费者。

## 模块与数据流

请求 → 任务记录 → 队列与Worker → 结果 → 进度查询。

## 实现后应观察

- 请求不被重计算阻塞
- 失败、重试和完成状态可回读

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-background-jobs.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-background-jobs.json)。
