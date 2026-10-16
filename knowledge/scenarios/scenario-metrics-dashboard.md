> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 查看趋势并点击筛选数据

ID：`scenario-metrics-dashboard`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

趋势 / 折线 / 漏斗 / 桑基 / 指标 / 经营 / 数据；图 / 大屏 / 看板 / 仪表盘 / 筛选 / 展示 / 监控。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 指标口径与数据来源是什么？
- 刷新频率和最大数据量是什么？

## 技术职责与候选

- [Apache ECharts](../technologies/tech-echarts.md)：交互式折线、漏斗、桑基和其他统计图。
- [AntV G2](../technologies/tech-g2.md)：以图形语法组合数据可视化。
- [D3](../technologies/tech-d3.md)：数据映射、比例尺与自定义可视化。

## 模块与数据流

数据查询 → 口径与聚合 → 图表适配 → 筛选联动 → 刷新。

## 实现后应观察

- 数值和时间口径正确
- 筛选与刷新不串数据

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-metrics-dashboard.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-metrics-dashboard.json)。
