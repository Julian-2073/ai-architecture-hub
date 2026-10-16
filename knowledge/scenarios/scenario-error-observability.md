> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 知道哪里报错和为什么变慢

ID：`scenario-error-observability`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

报错 / 错误 / 故障 / 变慢 / 延迟；发现 / 监控 / 定位 / 排查 / 追踪 / 告警。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 要回答错误细节、趋势还是跨服务路径？
- 敏感字段与保留期限是什么？

## 技术职责与候选

- [Sentry](../technologies/tech-sentry.md)：采集应用错误、上下文和性能信号。
- [OpenTelemetry](../technologies/tech-otel.md)：采集和导出链路、指标及日志信号。
- [Prometheus](../technologies/tech-prometheus.md)：抓取、存储和查询时间序列指标。
- [Grafana](../technologies/tech-grafana.md)：连接数据源制作监控面板。

## 模块与数据流

运行信号 → 采集脱敏 → 存储查询 → 告警 → 定位。

## 实现后应观察

- 关键故障能被发现和定位
- 敏感数据和成本可控

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-error-observability.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-error-observability.json)。
