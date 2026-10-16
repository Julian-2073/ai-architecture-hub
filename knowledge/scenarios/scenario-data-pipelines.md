> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 从多个系统定时整理数据

ID：`scenario-data-pipelines`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

多个系统 / 数据源 / 数据管道 / 仓库；定时 / 同步 / 清洗 / 汇总 / 转换 / 补数。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 源系统权限、数据口径和更新频率是什么？
- 增量、删除和补数怎样处理？

## 技术职责与候选

- [dbt（版本与发行线需区分）](../technologies/tech-dbt.md)：把 SQL 转换组织成可依赖、测试的模型。2026-10-16 读取的原官方仓库入口 README 区分 v1 分支与 Rust 重写的新主线，并说明源码与产品发行许可可能不同。选型必须先确定代际、发行版及适配器，不能沿用所有 dbt 都依赖 Python 的假设。这里记录的是 README 声明，未完成目标版本测试与许可全文审计。
- [Apache Airflow](../technologies/tech-airflow.md)：按依赖与调度组织数据任务。
- [DuckDB](../technologies/tech-duckdb.md)：以 SQL 分析本地表格与列式文件。

## 模块与数据流

采集 → 校验 → 转换模型 → 调度 → 血缘与数据质量。

## 实现后应观察

- 增量和补数不重复
- 源变化可追踪且口径一致

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-data-pipelines.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-data-pipelines.json)。
