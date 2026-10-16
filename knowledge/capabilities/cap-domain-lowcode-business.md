> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 内容平台、低代码与内部工具

## 从业务描述开始

需求能由内容模型、表格、表单和配置表达吗？

## 能力接口

数据模型/现有系统 → 管理页面、内容API和业务流程。这是职责示意，不是固定API。

## 情境化决策分支

1. 内容管理为主：比较CMS模型、发布与编辑角色。
2. 内部数据表和表单：评估表格平台或低代码后台，复用现有数据库和API。
3. 复杂公开产品：先验证交互、隔离、扩展和许可上限，再决定是否自研。
4. 需要对外提供平台服务：核查实际发行和服务条款，不从开源标签推断授权。

## 候选与关系

- [Directus](../technologies/tech-directus.md)：基于数据模型提供管理界面与接口。
- [Strapi](../technologies/tech-strapi.md)：组织内容模型、编辑流程与 API。
- [Payload](../technologies/tech-payload.md)：定义内容集合、管理界面和接口。
- [NocoDB](../technologies/tech-nocodb.md)：用表格视图管理数据并提供协作入口。
- [Budibase](../technologies/tech-budibase.md)：连接数据源构建表单、管理页与自动化。
- [Appsmith](../technologies/tech-appsmith.md)：用组件、查询和逻辑连接业务数据。

## 关键验证与退出

核查：连接器、对象权限、凭证范围、schema迁移、发布与导出。

保留：业务数据、内容模型、页面定义、查询与流程规格。

[情境决策树模板](../templates/template-selection-decision-tree.md)、[完整地图](cap-software-map.md)。建议来自 [社区版来源登记](../../evidence/curation/cap-domain-lowcode-business.json)，没有执行候选软件或项目验收。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-lowcode-business.json)。
