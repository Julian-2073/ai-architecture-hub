> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 让系统通过接口交换业务数据

ID：`scenario-api-backend`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

接口 / API / api / 后端；调用 / 数据 / 服务 / 对接 / 业务 / 请求。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 现有语言和部署环境是什么？
- 同步接口还是长任务？

## 技术职责与候选

- [FastAPI](../technologies/tech-fastapi.md)：Python 服务端候选
- [NestJS](../technologies/tech-nestjs.md)：有模块约定的 TypeScript 服务端候选
- [Express](../technologies/tech-express.md)：轻量 Node 服务端候选
- [Hono](../technologies/tech-hono.md)：需核查目标运行时的 Web 服务候选

## 模块与数据流

输入契约 → 认证校验 → 业务规则 → 存储 → 响应。

## 实现后应观察

- 错误与对象权限正确
- 关键事务和超时可验证

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-api-backend.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-api-backend.json)。
