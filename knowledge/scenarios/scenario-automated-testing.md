> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 自动操作页面验证业务

ID：`scenario-automated-testing`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

测试 / 验证 / 检查 / 回归；页面 / 浏览器 / 功能 / 程序 / 软件 / 界面 / 回归 / 测试。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 最关键的用户任务与回读证据是什么？
- 哪些失败会实质影响交付？

## 技术职责与候选

- [Playwright](../technologies/tech-playwright.md)：执行真实浏览器操作并做断言。
- [Vitest](../technologies/tech-vitest.md)：运行单元与集成测试。

## 模块与数据流

场景与数据 → 动作或函数 → 业务断言 → 证据。

## 实现后应观察

- 关键成功和失败行为可观察
- 不以截图代替结果

## 可选模板

- [最小技术验证 PoC](../templates/template-poc.md)
- [项目集成验收](../templates/template-acceptance.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-automated-testing.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

人工核对合同或审核数据不因同时出现“自动”和“检查”就当成软件测试；参见[社区版来源登记](../../evidence/curation/scenario-automated-testing.json)。词组仍是线索，Codex需要核对语义。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-automated-testing.json)。
