> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 消息、任务与工作流

ID：`cap-domain-async-workflows`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

事件、任务或流程定义 → 异步动作与执行状态。

## 关键判断

去重、幂等、顺序、重试、死信、补偿和执行授权。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [n8n](../technologies/tech-n8n.md)
- [Temporal](../technologies/tech-temporal.md)
- [Apache Kafka](../technologies/tech-kafka.md)
- [RabbitMQ](../technologies/tech-rabbitmq.md)
- [Celery](../technologies/tech-celery.md)
- [BullMQ](../technologies/tech-bullmq.md)

## 退出与数据

任务协议、事件 schema、流程状态、幂等键与重放方案。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-async-workflows.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想后台处理、自动连接系统、失败后能继续。

1. **起点**：要分发任务、保留事件还是持久化长流程？
2. **简单或既有路线**：少量工作先用现有后台机制或任务表。
3. **升级条件**：重放、多消费者、恢复与人工节点明确时比较队列、事件流和工作流。
4. **验证重点**：重复、乱序、幂等、补偿、外部授权和回执。

[对应模板](../templates/template-ai-tool-contract.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-async-workflows.json)，不是运行通过证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-async-workflows.json)。
