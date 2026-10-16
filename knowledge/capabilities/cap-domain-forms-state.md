> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 表单、状态与数据网格

ID：`cap-domain-forms-state`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

字段/远端数据 → 校验状态、缓存或网格行为。

## 关键判断

状态归属、缓存键、行 ID、受控组件及服务端分页。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [React Hook Form](../technologies/tech-react-hook-form.md)
- [Zustand](../technologies/tech-zustand.md)
- [TanStack Query](../technologies/tech-tanstack-query.md)
- [TanStack Table](../technologies/tech-tanstack-table.md)
- [AG Grid](../technologies/tech-ag-grid.md)

## 退出与数据

字段 schema、查询协议、列配置和业务状态模型。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-forms-state.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想让表单、筛选和大表格稳定工作。

1. **起点**：问题来自本地状态、远端缓存还是网格功能？
2. **简单或既有路线**：局部状态与原生输入够用则保持简单；复用当前表单表格。
3. **升级条件**：异步失效、动态字段或网格功能确有负担再分别引入工具。
4. **验证重点**：行ID、缓存租户边界、校验、分页与编辑回读。

[对应模板](../templates/template-data-contract.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-forms-state.json)，不是运行通过证据。

## 从“同事修改后点保存”拆开责任

默认先复用已有表单、列表和接口。复杂度确有缺口才引入相应层的工具，不把下表当成全部必装组件。

| 需要保留的内容 | 责任归属 | 候选入口与判断 |
|---|---|---|
| 未提交的字段和错误 | 表单草稿 | [React Hook Form](../technologies/tech-react-hook-form.md)等；简单原生/现有表单够用则复用 |
| 输入结构、转换与错误 | 运行时校验 | [Zod](../technologies/tech-zod.md)等；不能证明权限或事实真实性 |
| 跨组件的界面选择/偏好 | 客户端共享状态 | [Zustand](../technologies/tech-zustand.md)等；不要复制所有查询结果 |
| 可分享、可后退的筛选 | URL及路由契约 | 先利用已有路由，不把它只藏在内存store |
| 服务端结果及加载/刷新 | 查询层 | [TanStack Query](../technologies/tech-tanstack-query.md)等；正确划分缓存范围和失效 |
| 行列、排序、分页、编辑交互 | 表格/网格层 | 自定义UI的[TanStack Table](../technologies/tech-tanstack-table.md)或功能网格[AG Grid](../technologies/tech-ag-grid.md)，按交付负担和许可比较 |
| 权限、规则、事务及已保存记录 | 服务端与事实存储 | 优先现有API/数据库；前端按钮或校验不能替代 |

### 一次保存应怎样贯通

用户编辑 → 字段/结构检查 → 服务端身份与业务校验 → 事务提交 → 返回已保存结果/版本 → 按契约更新查询与视图。局部状态、缓存或乐观显示的更新不能单独作为保存证明。

多人修改同一条记录时，先明确冲突语义，例如版本检查、人工合并或业务允许的覆盖；不要因使用了查询库就假设冲突自动解决。网络失败、重复提交、账号/企业切换和旧页面迟到响应需要有相应处理。

### 推荐与变更条件

简单录入先用现有UI和请求方式；复杂表单才增加表单层；跨页面取数与失效明显复杂时再评估查询层；表格UI成本过高时比较完整网格。共享UI状态与运行时schema校验按各自缺口独立判断。成本包含表单/数据适配、缓存一致性、无障碍、网格许可、升级与退出，不把免费开源理解为零维护。

[录入保存验收模板](../templates/template-acceptance.md)；[社区版来源登记](../../evidence/curation/cap-domain-forms-state.json)为inference，没有运行本管线或核查具体项目。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-forms-state.json)。
