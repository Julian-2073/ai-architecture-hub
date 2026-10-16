> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 把多份表格合并成经营指标

ID：`scenario-spreadsheet-analysis`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

表格 / Excel / excel / CSV / csv / 工作簿；合并 / 上传 / 分析 / 汇总 / 指标 / 计算 / 导入。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 源表字段和计算口径是否明确？
- 单人本地还是多人共享？

## 技术职责与候选

- [pandas](../technologies/tech-pandas.md)：清洗、连接、聚合表格数据。
- [DuckDB](../technologies/tech-duckdb.md)：以 SQL 分析本地表格与列式文件。
- [Polars](../technologies/tech-polars.md)：表达表格数据变换与分析。

## 模块与数据流

文件 → schema与质量校验 → 清洗合并 → 指标计算 → 查询与导出。

## 实现后应观察

- 空白与零不混淆
- 关键指标与原表对照一致

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-spreadsheet-analysis.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-spreadsheet-analysis.json)。
