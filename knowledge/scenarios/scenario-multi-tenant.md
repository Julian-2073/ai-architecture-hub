> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 不同公司只能看到自己的资料

ID：`scenario-multi-tenant`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

不同公司 / 不同企业 / 多家 / 各家公司 / 租户；各自 / 隔离 / 自己的 / 不能看到 / 权限。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 租户从哪里确定？
- 数据库、文件、缓存与检索如何隔离？

## 技术职责与候选

- [Supabase](../technologies/tech-supabase.md)：后端平台与 RLS 等能力候选
- [PostgreSQL](../technologies/tech-postgresql.md)：业务存储和隔离策略基础
- [Keycloak](../technologies/tech-keycloak.md)：身份服务，不代替对象授权

## 模块与数据流

可信身份与租户 → 对象策略 → 读写过滤 → 跨层审计。

## 实现后应观察

- 跨租户直接请求被拒绝
- 缓存文件与搜索不串资料

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-multi-tenant.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-multi-tenant.json)。
