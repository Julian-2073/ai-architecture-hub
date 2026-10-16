> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 桌面安装并操作本地文件

ID：`scenario-desktop-app`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

电脑 / 桌面 / macOS / Windows / Mac；安装 / 应用 / 本地文件 / 离线 / 客户端。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 是否必须安装还是浏览器即可？
- 本地文件、签名和更新要求是什么？

## 技术职责与候选

- [Tauri](../technologies/tech-tauri.md)：组合 Web 前端与原生应用能力。
- [Electron](../technologies/tech-electron.md)：用 Chromium 与 Node.js 构建桌面应用。

## 模块与数据流

Web界面 → 进程或原生桥 → 系统权限 → 打包与更新。

## 实现后应观察

- 系统权限和文件操作正确
- 目标系统安装与更新可验证

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-desktop-app.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-desktop-app.json)。
