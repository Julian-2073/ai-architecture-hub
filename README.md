# AI Architecture Hub · AI 软件架构知识中台

**描述你想实现的效果，让 Codex 帮你找到合适的技术路径。**

An evidence-aware, local-first architecture knowledge hub for Codex. Describe the outcome; discover capabilities, components, trade-offs, and implementation steps.

[能力地图](knowledge/capabilities/cap-software-map.md) · [180 张技术卡片](docs/technology-catalog.md) · [需求场景](docs/scenarios.md) · [快速开始](#快速开始) · [接入 Codex](docs/codex-integration.md) · [贡献](CONTRIBUTING.md)

## 发现的痛点

不懂技术的人能说出想要的效果，却常常不知道该叫它什么，也不知道有哪些成熟组件。例如：

> “让客户可以绕着商品看一圈，还能换颜色。”

用户不应该先学会 Three.js、Blender 或 glTF，才能向 AI 提出这个需求。实际协作中还会遇到：

- **不知道工具名，就难以调用合适的工具。** 提示词停留在“做个 3D 效果”，容易漏掉模型制作、交互与性能要求。
- **AI 知道某个库，不代表选对了路线。** 建模软件、渲染库、业务模拟、工作流画布和执行器经常被混在一起。
- **每次聊天重新选型。** 项目的成功条件、失败原因与限制难以积累，下次又从零开始。
- **“已收录”容易被误读为“已验证”。** 官方功能介绍、工具已安装、局部 PoC 和真实业务验收之间缺少边界。

这是作者在个人项目协作中提出的问题定义，尚未做用户规模调查，也没有量化节省时间或成功率。

## 解决方案

以 **Codex 为自然语言入口、本地知识库为工程记忆**。Codex 理解业务，确定性工具负责检索、引用和完整性检查：

```mermaid
flowchart LR
  A[用自然语言描述目的与效果] --> B[Codex 理解与必要澄清]
  B --> C[能力地图与经验检索]
  C --> D[技术候选与职责分工]
  D --> E[按缺口核查与关键 PoC]
  E --> F[架构与开发交接]
  F --> G[后续项目实现及验收]
  G --> H[带证据回写]
  H --> C
```

比如上面的商品展示需求，知识库会帮助区分：**Blender 可用于制作资产，Three.js / Babylon.js 是网页运行候选；已有合适模型时，不必新增建模步骤。** 最后仍需确认目标设备、素材、预算、许可和实际项目环境。

对未命中的新说法，Codex 可以提交附用户原话引用的意图解释。用户不用填写 JSON，也不用先知道技术名。

## 解决哪些问题

| 原来的困难 | 这个项目提供的帮助 | 仍需项目自己完成 |
|---|---|---|
| 说不清技术需求 | 从目的、操作、输入与效果拆解能力 | 确认关键约束与成功标准 |
| 不知道可用组件 | 可检索的候选、职责、适用条件与替代路径 | 核查目标版本、许可和兼容性 |
| 只得到一串技术名 | 架构理由、接口边界、任务和验收模板 | 真实编码、接入和部署 |
| 经验散落在聊天中 | 稳定 ID、目录、来源、决策和经验结构 | 提供可回读的实现与验收证据 |
| 不知道证据证明了什么 | 分开记录资料、版本许可、PoC、集成与运行 | 在当前环境复验，不继承别的项目结论 |

## 当前功能

- **52 条能力记录**：含 32 个能力域总图及专项组合指南。
- **180 张技术卡片**：适用条件、职责边界、替代路径、接入前提、成本、迁移与重新评估条件。
- **45 个需求场景**：把口语中的任务线索映射到能力、条件性候选和关键问题。
- **26 份模板**：需求、架构、ADR、PoC、接口、验收、成本、迁移与知识回写；其中 **5 份结构化实施路径**。
- **`search`**：关键词、中文词组与能力别名检索，按记录类型、证据、范围和结果筛选。
- **`discover`**：场景发现、技术职责、项目依赖声明检查、实现路径和开发交接骨架。
- **有引用的意图解释**：支持 `--intent` / `--intent-json`，校验原话引用、已知约束、推断与排除项。
- **`validate`**：检查 ID、引用、文件、来源登记指纹、验证范围与证据边界。
- **可选 Codex Skill**：在新对话中提供自动发现入口；不依赖额外模型服务。

## 快速开始

需要 Python **3.10+** 和 Git；检索工具只用 Python 标准库，无额外依赖，不启动常驻服务。

```bash
git clone https://github.com/Julian-2073/ai-architecture-hub.git
cd ai-architecture-hub
python3 scripts/kb.py validate --strict
python3 scripts/kb.py discover '做一个可以拖动旋转的产品展示' --json
python3 scripts/kb.py search '离线 表格 导入 导出'
python3 -m unittest discover -s tests -v
```

在 Codex 中打开这个仓库，可以直接说：

> 我要做一个上传 CSV 后可以筛选、查看销售汇总并导出结果的工作台。先帮我理解需求，找可复用的技术路径，再给出实施方案。

根目录的 [AGENTS.md](AGENTS.md) 引导 Codex 使用本库。[CSV 工作台交接示例](examples/csv-workbench/handoff.md) 展示怎样从口语需求形成可实施的交接包，示例软件尚未实现。

要在其他项目中也使用，可运行可选安装器：

```bash
python3 scripts/install_codex_skill.py --skills-dir ~/.codex/skills
```

安装器仅写入一个名为 `architecture-hub` 的 Skill 目录（含技能正文和本机路径配置）；目录已存在则停止，默认不覆盖。仓库需要保留在安装时的位置。安装后新建聊天核验触发，详见[接入说明](docs/codex-integration.md)。

## 如何使用检索结果

`discover` 的词组规则是发现线索，不是通用语义模型。未命中时，Codex 继续理解原话、按能力检索，必要时提交有引用的解释；单独运行 CLI 不会自动调用大模型。

```bash
python3 scripts/kb.py discover '让买家绕着商品瞧瞧' --intent examples/grounded-intent.json --json
python3 scripts/kb.py discover '拖动节点，把几个步骤连起来' --project /path/to/your/project --json
python3 scripts/kb.py search '三维' --kind technology --json
python3 scripts/kb.py search '失败' --kind experience --outcome failed --json
```

最后一条在初始社区库中可以返回空结果：私人项目经验未公开。贡献者加入有证据的经验后即可检索，不应为填满目录而编造经验。

`--project` 只读指定根目录的相关依赖清单，声明不等于已安装。`--check-environment` 只检查 Python / Node / Blender 的可执行路径，不启动软件，也不证明插件可用。

## 开源版的证据与范围

本仓库公开当前能力地图、技术卡片、通用场景、模板与检索代码。**不包含私人项目代码、业务数据、凭证、本机配置备份或原私人仓库历史。** 官方参考 URL 保留，第三方网页全文不随包分发。

为避免误读，社区版候选的材料、目标版本与许可、PoC、集成和运行验证统一标为 **未执行 / 待复核**。`evidence/curation/` 是作者编制说明与参考链接登记，其指纹仅证明该文件未变，不是官方网页内容的指纹。原私人库的验证记录没有被改写或升级。

本项目可以输出有依据的架构建议与开发交接；**当前 CLI 不安装组件、不自动创建应用，也不自动部署。** Codex 或其他编码 Agent 在授权范围内承接实施。五类路径是模板，不是五个已验收应用；自动触发仍取决于宿主是否加载并遵循 Skill。

详见[证据规则](docs/evidence-policy.md)、[社区版清单](docs/community-manifest.json)及[发布验证](docs/release-verification.md)。

## 目录

```text
catalog.json                 稳定 ID、关系、来源与验证状态
data/                        需求场景和结构化实施路径
knowledge/capabilities/      能力地图与组合指南
knowledge/technologies/      技术卡片
knowledge/scenarios/         自然语言需求场景
knowledge/templates/         架构、验证与交接模板
evidence/curation/           作者编制说明和外部参考登记
scripts/                     标准库检索、发现、校验和可选安装器
skills/architecture-hub/     可移植 Skill 模板
tests/                       行为、证据边界与可移植性检查
examples/                    意图解释与 CSV 交接示例
```

Markdown 正文承载论证，JSON 目录负责定位和筛选。没有向量数据库或后台抓取任务，更新在实际需求与项目复盘中进行。

## 贡献与路线

欢迎提交需求场景、卡片修正、失败经验和可复现的项目证据。先读 [CONTRIBUTING.md](CONTRIBUTING.md)，说明原话、适用条件、数据性质、版本、验证范围和未覆盖限制。

接下来优先积累公开可复现的项目案例、反例测试和目标环境兼容证据。更多卡片不等于更高成熟度；不承诺通用需求理解准确率或全自动软件交付。

代码与作者原创内容采用 [MIT](LICENSE)。第三方产品、商标、链接内容、模型权重、素材及其服务条款分别适用原许可，参见 [第三方说明](THIRD_PARTY_NOTICES.md)。
