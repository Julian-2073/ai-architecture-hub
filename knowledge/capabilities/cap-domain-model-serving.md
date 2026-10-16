> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 模型加载与推理

ID：`cap-domain-model-serving`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

输入、模型和生成参数 → 文本、向量或推理结果。

## 关键判断

具体模型、权重许可、硬件、上下文、并发和调用语义。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [Ollama](../technologies/tech-ollama.md)
- [vLLM](../technologies/tech-vllm.md)
- [Transformers](../technologies/tech-transformers.md)
- [Sentence Transformers](../technologies/tech-sentence-transformers.md)
- [LiteLLM](../technologies/tech-litellm.md)

## 退出与数据

模型与版本、输入输出协议、参数和可重建索引。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-model-serving.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想调用AI或把模型放在自己的设备。

1. **起点**：数据、硬件、用量和维护条件允许哪条路线？
2. **简单或既有路线**：单一模型调用先保持简单SDK或已有服务。
3. **升级条件**：多供应商、私有推理或容量要求明确时再评估网关与运行引擎。
4. **验证重点**：具体模型权重、输入输出、上下文、资源、成本和许可。

[对应模板](../templates/template-cost-model.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-model-serving.json)，不是运行通过证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-model-serving.json)。
