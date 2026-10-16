> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# mediasoup

> WebRTC SFU 工具。候选；需按项目情境核查，不等于已采用。

## 用户想完成什么

提供低层媒体转发能力。定位来自官方资料；下面的情境判断、组合和验证是作者建议。

## 什么时候考虑

团队需要定制实时媒体服务。先检查当前项目和平台已有能力；同一技术在不同业务条件下可以有不同采用决定。

## 选择分界与组合

信令、房间、权限和运维仍需实现；不等于完整会议应用。

状态推送、双向事件和WebRTC媒体是不同层；低层SFU需要自建大量应用能力，先比较完整平台与已有服务。

## 接入前提

- 核实具体产品/发行版/版本、依赖与锁文件；HEAD和网页示例不是应直接采用的稳定配置。
- 重点检查：设备权限、TURN/NAT、代理、弱网、延迟、重连和授权。
- 明确数据来源、对象权限、错误与恢复、维护人及可导出格式；官方能力不自动补齐业务规则。

## 会改变选择的验证

验证浏览器、弱网、NAT、多人媒体与资源。事先确定代表性数据、目标环境、通过标准与停止条件；目前没有本项目PoC、集成或运行通过证据。

## 成本、维护与退出

服务器与网络和定制开发；保留信令协议与客户端边界。接入人力、固定运行、按量与维护分别计算；商业模块、服务、模型、字体和素材条款分别核查。未知价格和规模不估金额。

维护判断需结合支持政策、变更和安全信息；本次只记录正文中明确的具体提示，不凭热度决定成熟度。

## 证据与状态

- [官方入口](https://mediasoup.org/documentation/)；[项目或仓库入口](https://github.com/versatica/mediasoup)。
- [社区版来源登记](../../evidence/curation/tech-mediasoup.json)：`src-community-tech-mediasoup`，inference；读取日期2026-10-16，不当作网页发布日期。
- [社区版来源登记](../../evidence/curation/tech-mediasoup.json)：`src-community-tech-mediasoup`，inference。
- 目标版本、许可、PoC、集成和运行状态以 catalog.json 的 validations 为准，未因收录升级。

[所属能力域](../capabilities/cap-domain-realtime-media.md) · [情境决策树模板](../templates/template-selection-decision-tree.md) · [技术目录](../../docs/technology-catalog.md)

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/tech-mediasoup.json)。
