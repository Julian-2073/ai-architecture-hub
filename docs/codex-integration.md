# 接入 Codex

在 Codex 中打开仓库，根 `AGENTS.md` 提供当前项目的入口。若希望在其他项目中使用，安装可选 Skill：

```bash
python3 scripts/install_codex_skill.py --skills-dir ~/.codex/skills --dry-run
python3 scripts/install_codex_skill.py --skills-dir ~/.codex/skills
```

先确认显示的仓库路径。安装器只写指定目录中的 `architecture-hub/SKILL.md`，将当前仓库绝对路径写入用户自己的本地 Skill，不修改全局 AGENTS.md、不联网、不安装其他依赖；已有目录会拒绝覆盖。重新安装前自行备份原 Skill 并选择另一个目录或手动合并。

移动/删除仓库后需手动更新安装后的路径。不同 Codex 宿主的技能加载规则可能不同；在新聊天中确认该 Skill 是否可见，再进行真实触发测试。安装成功与实际触发是两项检查。

可说：“我要在网页上传销售表，筛选日期后看汇总并导出。”观察 Codex 是否调用 `discover`、读取相关卡片并解释取舍。再换一个没有技术词的说法，检查未命中时是否继续理解；不要把单次成功当作普遍保证。

只读讨论不会写入知识；开发授权内才实施与记录，发布和外部动作依照用户授权进行。本仓库不创建新后台服务或定时任务。
