> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 断网也能填写与保存

ID：`scenario-local-offline`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

断网 / 离线 / 没网络 / 无网络 / 本地；填写 / 保存 / 使用 / 继续写 / 同步 / 工作 / 接着写。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先确认浏览器、桌面还是移动；浏览器可评估原生 IndexedDB，当前目录不是原生能力白名单。

- 是否只在一台设备？
- 联网后是否需要合并多人修改？

## 技术职责与候选

- [SQLite](../technologies/tech-sqlite.md)：本地持久化候选；浏览器不能不经适配直接使用系统 SQLite
- [Yjs](../technologies/tech-yjs.md)：需要并发/离线合并时的共享状态候选

## 模块与数据流

本地状态 → 持久化 → 可选同步与冲突处理 → 恢复。

## 实现后应观察

- 刷新与重启不丢数据
- 联网冲突与导出备份明确

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-local-offline.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-local-offline.json)。
