> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 预测与优化

ID：`cap-domain-prediction-optimization`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

特征/序列/约束 → 预测或可行方案。

## 关键判断

时间切分、基线、标签、泄漏、约束与失败解释。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [scikit-learn](../technologies/tech-scikit-learn.md)
- [LightGBM](../technologies/tech-lightgbm.md)
- [Chronos](../technologies/tech-chronos.md)
- [OR-Tools](../technologies/tech-ortools.md)

## 退出与数据

训练数据边界、特征、模型、约束、评估与求解配置。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-prediction-optimization.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想知道未来会怎样，或如何安排更好。

1. **起点**：需要预测结果还是在约束内选择行动？
2. **简单或既有路线**：先有简单预测/规则基线和明确评价，避免直接上复杂模型。
3. **升级条件**：按时间回测或约束建模证明复杂方案有价值后才接入。
4. **验证重点**：泄漏、误差、可行性、超时状态与商业收益分开。

[对应模板](../templates/template-poc.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-prediction-optimization.json)，不是运行通过证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-prediction-optimization.json)。
