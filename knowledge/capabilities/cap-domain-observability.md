> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 可观测性

ID：`cap-domain-observability`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

运行信号 → 可诊断链路、指标、日志与评估记录。

## 关键判断

采样、标签基数、敏感信息、存储、告警和负责人。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [OpenTelemetry](../technologies/tech-otel.md)
- [LangSmith](../technologies/tech-langsmith.md)
- [Prometheus](../technologies/tech-prometheus.md)
- [Grafana](../technologies/tech-grafana.md)
- [Sentry](../technologies/tech-sentry.md)

## 退出与数据

标准遥测字段、仪表盘、规则、可导出日志与保留策略。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-observability.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想知道哪里出了问题、为何变慢。

1. **起点**：要事件细节、总体趋势还是跨服务路径？
2. **简单或既有路线**：从关键业务日志和可诊断ID开始，复用当前采集与面板。
3. **升级条件**：需要指标、链路或AI追踪时按问题增加对应能力。
4. **验证重点**：采样、标签基数、敏感字段、保留和真实告警。

[对应模板](../templates/template-acceptance.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-observability.json)，不是运行通过证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-observability.json)。
