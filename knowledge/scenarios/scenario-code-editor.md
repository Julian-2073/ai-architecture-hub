> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 在页面中编辑代码或脚本

ID：`scenario-code-editor`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

页面 / 网页 / 浏览器 / 在线；代码 / 脚本 / 语法 / IDE / 代码编辑。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 只是编辑还是要执行代码？
- 支持哪些语言与设备？

## 技术职责与候选

- [Monaco Editor](../technologies/tech-monaco.md)：提供代码编辑、语法与语言服务接入。
- [CodeMirror](../technologies/tech-codemirror.md)：组合代码编辑与语言扩展。2026-10-16 读取的 GitHub 仓库 README 声明开发仓库已迁到 code.haverbeke.berlin；该 GitHub 地址保留为历史入口。正式维护与 issue 核查应沿官方迁移地址进行，不凭旧仓库活跃度判定项目停滞。

## 模块与数据流

编辑文本 → 语法服务 → 保存 → 独立受控执行层。

## 实现后应观察

- 中文输入与大文件可用
- 代码执行权限与编辑器分离

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-code-editor.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-code-editor.json)。
