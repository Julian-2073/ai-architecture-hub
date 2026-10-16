> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 建立填报与管理页面

ID：`scenario-business-forms`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

填报 / 录入 / 表单 / 后台 / 管理页面；提交 / 编辑 / 字段 / 审核 / 客户 / 订单 / 数据。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 哪些字段、规则和角色？
- 提交成功后在哪里回读？

## 技术职责与候选

- [Ant Design](../technologies/tech-antd.md)：提供表格、表单和弹窗等界面组件。
- [Mantine](../technologies/tech-mantine.md)：提供表单、布局和交互组件。
- [React Hook Form](../technologies/tech-react-hook-form.md)：管理输入、校验和表单提交状态。
- [Zod](../technologies/tech-zod.md)：校验运行时数据并推导类型。

## 模块与数据流

字段 → 校验 → 业务服务 → 事务存储 → 列表和结果回读。

## 实现后应观察

- 重复提交与错误输入可处理
- 保存后重新读取一致

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-business-forms.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-business-forms.json)。
