[English](README.md) · **🌐 中文**

<h1 align="center">Ink 墨</h1>

<p align="center">
  <em>「你的 AI 对话，可视化。每周一幅新作。」</em><br>
  <em>"Your AI conversations, visualized. Every week a new masterpiece."</em>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
  <a href="https://skills.sh"><img src="https://img.shields.io/badge/skills.sh-Compatible-brightgreen" alt="skills.sh"></a>
  <a href="#"><img src="https://img.shields.io/badge/Agent-Agnostic-blueviolet" alt="Agent Agnostic"></a>
  <a href="#"><img src="https://img.shields.io/badge/macOS%20%2B%20Windows-supported-blue" alt="Cross-platform"></a>
</p>

**Ink 扫描你电脑上所有的 AI 工具，统计对话轮次，生成一张精美的社交分享卡片——每次都是全新的风格。** 不同的版式、不同的金句、不同的视觉概念。导出高清 PNG，直接发朋友圈、X/Twitter、小红书、微博。

不用 Figma。没有模板。一条命令搞定。

```
npx skills add quzhi-ai/ink
```

[怎么工作](#怎么工作) · [6 种风格](#6-种风格模式) · [支持的工具](#支持的-ai-工具) · [安装](#安装)

<p align="center">
  <img src="assets/hero-collage.png" width="900" alt="Ink 卡片示例 — 6 种风格模式" />
</p>

---

## 怎么工作

### 第一次：揭晓体验

你的第一次 `/ink` 是一场 **Spotify Wrapped 式的叙事揭晓**。每一步都是一个惊喜：

```
/ink
```

> 「正在扫描你的电脑……」
> 「发现了 3 个 AI 工具：Claude Code、Codex、Cursor。」
> 「过去一周，你跟 AI 说了 **713** 句话。」
> 「你最活跃的时间是晚上 10 点。别人在追剧，你在和 AI 论道。」
> 「选一个墨风吧。给你三张卡片，选一张。」
> 「已保存到桌面。去晒吧。」

### 之后：一条命令，一张卡片

```
/ink              # 最近 7 天，上次的风格
/ink day          # 今天
/ink month        # 最近 30 天
/ink 2026-06-01 2026-06-26   # 自定义范围
```

三张卡片出来。选一张。搞定。

---

## 6 种风格模式

每张卡片都是**从零生成**——没有固定模板。AI 每次创造一个全新的视觉概念，沿着六个创意方向之一：

| 模式 | 气质 | 联想…… |
|------|------|--------|
| **正经反差** | 越严肃越好笑 | 考试卷、处方笺、圣旨、银行对账单、成绩单 |
| **视觉美学** | 第一眼就被美到 | 黑胶唱片、塔罗牌、电影海报、酒标、音乐播放器 |
| **极客硬核** | 技术圈想转发 | 终端命令行、NASA 控制台、K 线图、健身圆环 |
| **生活脑洞** | 日常场景大改造 | 外卖订单、咖啡杯套、宜家说明书、食谱、签语饼 |
| **时空穿越** | 古今中外碰撞 | 民国老报纸、电报、护照签证页、漫画分镜、精灵图鉴 |
| **随机惊喜** | 没有规则，最大惊喜 | 打开才知道。 |

每张卡片都有一句**哲学金句**，改编自真实名人名言，每次都不一样。

### 卡片画廊

<table>
<tr>
<td align="center"><img src="examples/style_k_prescription/card.png" width="180"><br><sub>处方笺</sub></td>
<td align="center"><img src="examples/style_z5_exam_paper/card.png" width="180"><br><sub>考试卷</sub></td>
<td align="center"><img src="examples/style_a1_imperial_edict/card.png" width="180"><br><sub>圣旨</sub></td>
<td align="center"><img src="examples/style_r_report_card/card.png" width="180"><br><sub>成绩单</sub></td>
</tr>
<tr>
<td align="center"><img src="examples/style_a8_bank_statement/card.png" width="180"><br><sub>银行对账单</sub></td>
<td align="center"><img src="examples/style_a9_imperial_exam/card.png" width="180"><br><sub>科举金榜</sub></td>
<td align="center"><img src="examples/style_l_vinyl_record/card.png" width="180"><br><sub>黑胶唱片</sub></td>
<td align="center"><img src="examples/style_z1_tarot/card.png" width="180"><br><sub>塔罗牌</sub></td>
</tr>
<tr>
<td align="center"><img src="examples/style_z3_film_poster/card.png" width="180"><br><sub>电影海报</sub></td>
<td align="center"><img src="examples/style_u_wine_label/card.png" width="180"><br><sub>酒标</sub></td>
<td align="center"><img src="examples/style_s_constellation/card.png" width="180"><br><sub>星图</sub></td>
<td align="center"><img src="examples/style_x_concert_ticket/card.png" width="180"><br><sub>演唱会门票</sub></td>
</tr>
<tr>
<td align="center"><img src="examples/style_a2_spotify_player/card.png" width="180"><br><sub>音乐播放器</sub></td>
<td align="center"><img src="examples/style_e_terminal/card.png" width="180"><br><sub>终端命令行</sub></td>
<td align="center"><img src="examples/style_w_stock_chart/card.png" width="180"><br><sub>K线图</sub></td>
<td align="center"><img src="examples/style_a3_nasa_mission/card.png" width="180"><br><sub>太空任务控制台</sub></td>
</tr>
<tr>
<td align="center"><img src="examples/style_z8_fitness_app/card.png" width="180"><br><sub>健身圆环</sub></td>
<td align="center"><img src="examples/style_a6_basketball_stats/card.png" width="180"><br><sub>NBA球员卡</sub></td>
<td align="center"><img src="examples/style_a7_pokedex/card.png" width="180"><br><sub>精灵图鉴</sub></td>
<td align="center"><img src="examples/style_g_receipt/card.png" width="180"><br><sub>小票</sub></td>
</tr>
<tr>
<td align="center"><img src="examples/style_q_recipe/card.png" width="180"><br><sub>食谱</sub></td>
<td align="center"><img src="examples/style_a5_meituan_order/card.png" width="180"><br><sub>外卖订单</sub></td>
<td align="center"><img src="examples/style_z7_ikea_manual/card.png" width="180"><br><sub>宜家说明书</sub></td>
<td align="center"><img src="examples/style_a10_coffee_sleeve/card.png" width="180"><br><sub>咖啡杯套</sub></td>
</tr>
<tr>
<td align="center"><img src="examples/style_z9_fortune_cookie/card.png" width="180"><br><sub>签语饼</sub></td>
<td align="center"><img src="examples/style_z6_wechat_moments/card.png" width="180"><br><sub>朋友圈</sub></td>
<td align="center"><img src="examples/style_z4_shipping_label/card.png" width="180"><br><sub>快递面单</sub></td>
<td align="center"><img src="examples/style_o_newspaper/card.png" width="180"><br><sub>民国老报纸</sub></td>
</tr>
<tr>
<td align="center"><img src="examples/style_v_telegram/card.png" width="180"><br><sub>电报</sub></td>
<td align="center"><img src="examples/style_j_boarding_pass/card.png" width="180"><br><sub>登机牌</sub></td>
<td align="center"><img src="examples/style_p_passport/card.png" width="180"><br><sub>护照签证页</sub></td>
<td align="center"><img src="examples/style_i_postcard/card.png" width="180"><br><sub>明信片</sub></td>
</tr>
<tr>
<td align="center"><img src="examples/style_z2_metro_map/card.png" width="180"><br><sub>地铁线路图</sub></td>
<td align="center"><img src="examples/style_a4_manga_panel/card.png" width="180"><br><sub>漫画分镜</sub></td>
<td colspan="2"></td>
</tr>
</table>

---

## 支持的 AI 工具

Ink 自动扫描以下本地工具（零配置）：

### 编程助手
Claude Code · Codex · Cursor · Windsurf · Aider · Continue.dev · Cline · Roo Code · GitHub Copilot

### AI 对话（桌面端）
Claude Desktop · ChatGPT Desktop · Gemini Desktop

### 本地大模型
Ollama · LM Studio · Jan · GPT4All

### 终端 & 效率工具
Warp AI · Raycast AI

找不到你的工具？Ink 也支持**自定义 JSON 数据文件**：

```
/ink --data ~/my-ai-stats.json
```

---

## 输出

- **格式**：PNG，1170 × 1560 px（3:4，Retina 级清晰度）
- **保存位置**：默认桌面
- **文件名**：`墨_2026W26.png`
- **水印**：底部小字 "Made with Ink"——你的卡片就是最好的广告

---

## 安装

```bash
npx skills add quzhi-ai/ink
```

或手动安装：

```bash
git clone https://github.com/quzhi-ai/ink.git
cp -r ink/skill/ink ~/.claude/skills/
```

然后：

```
/ink
```

---

## 架构

```
ink/
├── README.md                  # English
├── README.zh.md               # 中文（本文件）
├── LICENSE                    # MIT
├── skill/
│   └── ink/                   # 真正的 Claude Code Skill
│       ├── SKILL.md           # Skill 定义 + 品味基准线 + 工作流
│       ├── references/        # 风格模式定义、扫描路径
│       └── scripts/
│           └── render_png.py  # Puppeteer/Chrome headless → PNG 导出
├── docs/                      # 同样的参考文档，方便 GitHub 浏览
├── examples/                  # Demo 卡片（源 HTML + 输出 PNG）
├── demos/
│   └── donate/                # 支持项目（微信支付 + 支付宝）
└── assets/
    └── hero-collage.png       # README 头图
```

---

## 隐私

Ink 只读取**元数据**（时间戳和来源名称）。**绝不读取你的对话内容**。你的 prompt 和回复完全私密。

---

## 依赖

```
Node.js          # Puppeteer PNG 渲染
Google Chrome    # Headless 截图引擎
```

开发者电脑上基本都有。无需额外安装。

---

## 支持项目

如果 Ink 对你有帮助，欢迎请作者喝杯咖啡：

| 微信支付 | 支付宝 |
|:---:|:---:|
| <img src="demos/donate/wechat-pay.jpg" width="200"> | <img src="demos/donate/alipay.jpg" width="200"> |

## Star History

<p align="center">
  <a href="https://star-history.com/#quzhi-ai/ink&Date">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=quzhi-ai/ink&type=Date&theme=dark" />
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=quzhi-ai/ink&type=Date" />
      <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=quzhi-ai/ink&type=Date" width="600" />
    </picture>
  </a>
</p>

## License

MIT — 见 [LICENSE](LICENSE)

---

<p align="center">
  <em>你的 AI 对话留下痕迹。墨，让它们变美。</em>
</p>
