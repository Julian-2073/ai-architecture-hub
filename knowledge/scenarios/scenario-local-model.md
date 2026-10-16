> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 把模型放在自己的电脑或服务器

ID：`scenario-local-model`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

模型 / 大模型 / AI / ai；本地 / 自己电脑 / 不出本机 / 私有 / 自建 / 服务器推理。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 硬件、内存和模型许可是什么？
- 数据边界与并发需求是什么？

## 技术职责与候选

- [Ollama](../technologies/tech-ollama.md)：在本机或服务端运行模型并提供调用接口。
- [vLLM](../technologies/tech-vllm.md)：组织模型推理和服务端吞吐。
- [Transformers](../technologies/tech-transformers.md)：加载不同任务的预训练模型。

## 模块与数据流

模型与权重 → 运行引擎 → 受控接口 → 任务评估。

## 实现后应观察

- 具体硬件支持并测量资源
- 工具与权重许可分开

## 可选模板

- [需求与约束记录](../templates/template-requirements.md)
- [技术方案成本估算模型](../templates/template-cost-model.md)
- [最小技术验证 PoC](../templates/template-poc.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-local-model.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-local-model.json)。
