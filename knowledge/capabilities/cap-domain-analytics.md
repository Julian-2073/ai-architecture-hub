> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 数据工程与分析

ID：`cap-domain-analytics`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

原始表/文件/事件 → 清洗表、聚合和批处理结果。

## 关键判断

类型、空值、时区、增量、血缘、补数和重复执行。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [pandas](../technologies/tech-pandas.md)
- [DuckDB](../technologies/tech-duckdb.md)
- [Polars](../technologies/tech-polars.md)
- [ClickHouse](../technologies/tech-clickhouse.md)
- [dbt（版本与发行线需区分）](../technologies/tech-dbt.md)
- [Apache Airflow](../technologies/tech-airflow.md)

## 退出与数据

原始文件、SQL/表达式、转换口径、任务与模型配置。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-analytics.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想把不同来源的数据合并算清楚。

1. **起点**：本地文件分析还是持续数据管线？
2. **简单或既有路线**：简单表和SQL先复用当前工具，口径与质量优先。
3. **升级条件**：内存、规模、调度或转换治理出现实际瓶颈再升级。
4. **验证重点**：空值、类型、时间、增量、补数与原件对照。

[对应模板](../templates/template-data-contract.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-analytics.json)，不是运行通过证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-analytics.json)。
