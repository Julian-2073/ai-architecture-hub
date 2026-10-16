> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# AI 评估

ID：`cap-domain-ai-evaluation`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

样本、预期与输出 → 断言、指标和误差分析。

## 关键判断

人工标注、模型判分校准、样本代表性和成本。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [promptfoo](../technologies/tech-promptfoo.md)
- [Ragas](../technologies/tech-ragas.md)

## 退出与数据

数据集、版本、判分标准、原始输出与失败分类。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-ai-evaluation.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想知道AI的回答到底有没有变好。

1. **起点**：怎样定义正确、样本来自哪里？
2. **简单或既有路线**：先有人可解释的代表性样本与简单断言。
3. **升级条件**：样本增长或指标需要时引入评估工具，模型判分先校准。
4. **验证重点**：人工真值、失败类别、波动、成本与外部留出集。

[对应模板](../templates/template-poc.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-ai-evaluation.json)，不是运行通过证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-ai-evaluation.json)。
