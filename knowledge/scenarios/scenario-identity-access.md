> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 登录并限制谁能操作

ID：`scenario-identity-access`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

登录 / 账号 / 认证 / 身份；权限 / 角色 / 限制 / 看不到 / 能操作 / 访问。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 现有身份系统是什么？
- 权限需要到对象、字段还是文件？

## 技术职责与候选

- [Keycloak](../technologies/tech-keycloak.md)：集中登录、身份联邦与标准认证。
- [Supabase](../technologies/tech-supabase.md)：组合数据库、认证、存储等后端能力。

## 模块与数据流

身份认证 → 会话 → 对象授权 → 操作 → 审计。

## 实现后应观察

- 直接API越权被拒绝
- 退出、角色变化与令牌生效

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-identity-access.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-identity-access.json)。
