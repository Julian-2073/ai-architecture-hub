> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 估计未来销量需求与库存

ID：`scenario-time-series-forecast`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

未来 / 预测 / 估计 / 下周 / 下月；销量 / 需求 / 库存 / 销售 / 时间序列。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 历史跨度与预测粒度是什么？
- 预测时实际能获得哪些特征？

## 技术职责与候选

- [Chronos](../technologies/tech-chronos.md)：使用预训练模型进行时间序列预测。
- [LightGBM](../technologies/tech-lightgbm.md)：结构化特征的分类与回归。
- [scikit-learn](../technologies/tech-scikit-learn.md)：预处理、传统模型与模型评估。

## 模块与数据流

历史数据 → 时间切分 → 简单基线 → 候选预测 → 回测。

## 实现后应观察

- 无未来信息泄漏
- 同口径优于或解释未优于基线

## 可选模板

- [最小技术验证 PoC](../templates/template-poc.md)
- [项目集成验收](../templates/template-acceptance.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-time-series-forecast.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-time-series-forecast.json)。
