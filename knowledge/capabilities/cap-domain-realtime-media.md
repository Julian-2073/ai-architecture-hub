> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 实时事件、音视频与媒体会话

## 从业务描述开始

只是状态推送，还是双向事件、语音视频或媒体房间？

## 能力接口

事件/媒体流 → 会话、传输与可观察状态。这是职责示意，不是固定API。

## 情境化决策分支

1. 服务端单向状态：先比较轮询或SSE，不默认引入会议平台。
2. 双向事件：原生协议与事件框架的配套方式分别核查。
3. 音视频产品：先看完整平台能力是否满足设备、房间、录制和地区要求。
4. 定制SFU：只有团队能承担信令、NAT、弱网、调度和运维时才选择低层路线。

## 候选与关系

- [Socket.IO](../technologies/tech-socketio.md)：在客户端与服务端交换事件。
- [LiveKit](../technologies/tech-livekit.md)：提供房间、媒体传输及相关SDK能力。
- [mediasoup](../technologies/tech-mediasoup.md)：提供低层媒体转发能力。

## 关键验证与退出

核查：设备权限、TURN/NAT、代理、弱网、延迟、重连和授权。

保留：业务房间ID、事件/信令契约、接入边界与媒体处理策略。

[情境决策树模板](../templates/template-selection-decision-tree.md)、[完整地图](cap-software-map.md)。建议来自 [社区版来源登记](../../evidence/curation/cap-domain-realtime-media.json)，没有执行候选软件或项目验收。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-realtime-media.json)。
