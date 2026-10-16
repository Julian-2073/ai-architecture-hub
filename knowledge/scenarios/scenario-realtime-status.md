> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 不用刷新就看到状态变化

ID：`scenario-realtime-status`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

状态 / 消息 / 进度 / 数据；不用刷新 / 实时更新 / 即时 / 推送 / 双向。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先比较轮询、SSE 与 WebSocket；通常复用现有后端，不为推送新增整套服务框架。

- 允许多大延迟，是否双向？
- 断线、鉴权和代理限制是什么？

## 技术职责与候选

- [FastAPI](../technologies/tech-fastapi.md)：Python 服务端接口载体，不是推送协议本身
- [NestJS](../technologies/tech-nestjs.md)：TypeScript 服务端接口载体，不是推送协议本身

## 模块与数据流

后端状态 → 轮询或SSE/WebSocket → 客户端重连 → 一致性。

## 实现后应观察

- 断线后状态可恢复
- 不因实时一词强制引入双向连接

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-realtime-status.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-realtime-status.json)。
