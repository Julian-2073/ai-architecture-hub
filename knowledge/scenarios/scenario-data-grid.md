> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 处理很多行并排序分组的表格

ID：`scenario-data-grid`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

表格 / 列表 / 数据网格；很多行 / 排序 / 分组 / 筛选 / 固定列 / 导出 / 编辑单元格。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 哪些网格功能是必须且可付费？
- 服务端分页还是本地数据？

## 技术职责与候选

- [AG Grid](../technologies/tech-ag-grid.md)：提供复杂数据表格交互。
- [TanStack Table](../technologies/tech-tanstack-table.md)：管理表格列、排序、筛选与行模型。
- [Ant Design](../technologies/tech-antd.md)：提供表格、表单和弹窗等界面组件。

## 模块与数据流

查询协议 → 行模型与唯一ID → 网格交互 → 编辑或导出。

## 实现后应观察

- 排序筛选覆盖全部目标数据
- 编辑与导出符合业务口径

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-data-grid.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-data-grid.json)。
