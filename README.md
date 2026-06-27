**🌐 English** · [中文](README.zh.md)

<h1 align="center">Ink 墨</h1>

<p align="center">
  <em>"Your AI conversations, visualized. Every week a new masterpiece."</em><br>
  <em>「你的 AI 对话，可视化。每周一幅新作。」</em>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
  <a href="https://skills.sh"><img src="https://img.shields.io/badge/skills.sh-Compatible-brightgreen" alt="skills.sh"></a>
  <a href="#"><img src="https://img.shields.io/badge/Agent-Agnostic-blueviolet" alt="Agent Agnostic"></a>
  <a href="#"><img src="https://img.shields.io/badge/macOS%20%2B%20Windows-supported-blue" alt="Cross-platform"></a>
</p>

**Ink scans every AI tool on your machine, counts your conversation turns, and generates a stunning social-sharing card — in a style you've never seen before.** Each card is unique: different format, different quote, different visual concept. Export as high-res PNG, ready for Twitter/X, WeChat Moments, Instagram, or anywhere you want to show off your AI life.

No Figma. No templates. Just one command.

```
npx skills add quzhi-ai/ink
```

[How it works](#how-it-works) · [Style modes](#the-6-style-modes) · [Supported tools](#supported-ai-tools) · [Install](#install)

<p align="center">
  <img src="assets/hero-collage.png" width="900" alt="Ink card examples across 6 style modes" />
</p>

---

## How It Works

### First Run: The Reveal

Your first `/ink` is a **Spotify Wrapped-style experience**. Each step reveals something about your AI usage:

```
/ink
```

> "I scanned your machine and found 3 AI tools..."
> "Over the past 7 days, you talked to AI 713 times."
> "Your most active hour? 10 PM. Everyone else is watching Netflix."
> "Pick your style. Here are 3 cards. Choose one."
> "Saved to Desktop. Go share it."

### After That: One Command, One Card

Returning users get the fast path:

```
/ink              # last 7 days, last style mode
/ink day          # today
/ink month        # last 30 days
/ink 2026-06-01 2026-06-26   # custom range
```

Three cards appear. Pick one. Done.

---

## The 6 Style Modes

Every card is **generated from scratch** — no fixed templates. The AI creates a completely new visual concept each time, guided by one of six creative directions:

| Mode | Vibe | Think... |
|------|------|----------|
| **Formal Contrast** | Serious format + playful data = comedy | Exam papers, prescriptions, imperial edicts, bank statements |
| **Visual Art** | Beautiful first, data second | Vinyl records, tarot cards, movie posters, wine labels |
| **Geek Mode** | Data-dense, technically precise | Terminal CLI, NASA mission control, K-line charts |
| **Life Remix** | Everyday objects reimagined | Food delivery orders, coffee sleeves, IKEA manuals |
| **Time Travel** | Cross-era mashups | 1920s newspapers, telegrams, passport stamps, manga panels |
| **Surprise Me** | No rules. Maximum chaos. | You'll find out when it renders. |

Each card includes a **philosophical quote**, remixed from a real author to fit your data. Never the same twice.

### Gallery

<table>
<tr>
<td align="center"><img src="examples/style_k_prescription/card.png" width="180"><br><sub>Prescription 处方笺</sub></td>
<td align="center"><img src="examples/style_z5_exam_paper/card.png" width="180"><br><sub>Exam Paper 考试卷</sub></td>
<td align="center"><img src="examples/style_a1_imperial_edict/card.png" width="180"><br><sub>Imperial Edict 圣旨</sub></td>
<td align="center"><img src="examples/style_r_report_card/card.png" width="180"><br><sub>Report Card 成绩单</sub></td>
</tr>
<tr>
<td align="center"><img src="examples/style_a8_bank_statement/card.png" width="180"><br><sub>Bank Statement 对账单</sub></td>
<td align="center"><img src="examples/style_a9_imperial_exam/card.png" width="180"><br><sub>Imperial Exam 科举金榜</sub></td>
<td align="center"><img src="examples/style_l_vinyl_record/card.png" width="180"><br><sub>Vinyl Record 黑胶唱片</sub></td>
<td align="center"><img src="examples/style_z1_tarot/card.png" width="180"><br><sub>Tarot Card 塔罗牌</sub></td>
</tr>
<tr>
<td align="center"><img src="examples/style_z3_film_poster/card.png" width="180"><br><sub>Film Poster 电影海报</sub></td>
<td align="center"><img src="examples/style_u_wine_label/card.png" width="180"><br><sub>Wine Label 酒标</sub></td>
<td align="center"><img src="examples/style_s_constellation/card.png" width="180"><br><sub>Star Map 星图</sub></td>
<td align="center"><img src="examples/style_x_concert_ticket/card.png" width="180"><br><sub>Concert Ticket 演唱会门票</sub></td>
</tr>
<tr>
<td align="center"><img src="examples/style_a2_spotify_player/card.png" width="180"><br><sub>Music Player 音乐播放器</sub></td>
<td align="center"><img src="examples/style_e_terminal/card.png" width="180"><br><sub>Terminal CLI 终端命令行</sub></td>
<td align="center"><img src="examples/style_w_stock_chart/card.png" width="180"><br><sub>K-Line Chart K线图</sub></td>
<td align="center"><img src="examples/style_a3_nasa_mission/card.png" width="180"><br><sub>NASA Mission 太空任务</sub></td>
</tr>
<tr>
<td align="center"><img src="examples/style_z8_fitness_app/card.png" width="180"><br><sub>Fitness Rings 健身圆环</sub></td>
<td align="center"><img src="examples/style_a6_basketball_stats/card.png" width="180"><br><sub>NBA Stats NBA球员卡</sub></td>
<td align="center"><img src="examples/style_a7_pokedex/card.png" width="180"><br><sub>Pokédex 精灵图鉴</sub></td>
<td align="center"><img src="examples/style_g_receipt/card.png" width="180"><br><sub>Receipt 小票</sub></td>
</tr>
<tr>
<td align="center"><img src="examples/style_q_recipe/card.png" width="180"><br><sub>Recipe 食谱</sub></td>
<td align="center"><img src="examples/style_a5_meituan_order/card.png" width="180"><br><sub>Delivery Order 外卖订单</sub></td>
<td align="center"><img src="examples/style_z7_ikea_manual/card.png" width="180"><br><sub>IKEA Manual 宜家说明书</sub></td>
<td align="center"><img src="examples/style_a10_coffee_sleeve/card.png" width="180"><br><sub>Coffee Sleeve 咖啡杯套</sub></td>
</tr>
<tr>
<td align="center"><img src="examples/style_z9_fortune_cookie/card.png" width="180"><br><sub>Fortune Cookie 签语饼</sub></td>
<td align="center"><img src="examples/style_z6_wechat_moments/card.png" width="180"><br><sub>WeChat Moments 朋友圈</sub></td>
<td align="center"><img src="examples/style_z4_shipping_label/card.png" width="180"><br><sub>Shipping Label 快递面单</sub></td>
<td align="center"><img src="examples/style_o_newspaper/card.png" width="180"><br><sub>Newspaper 民国老报纸</sub></td>
</tr>
<tr>
<td align="center"><img src="examples/style_v_telegram/card.png" width="180"><br><sub>Telegram 电报</sub></td>
<td align="center"><img src="examples/style_j_boarding_pass/card.png" width="180"><br><sub>Boarding Pass 登机牌</sub></td>
<td align="center"><img src="examples/style_p_passport/card.png" width="180"><br><sub>Passport 护照签证页</sub></td>
<td align="center"><img src="examples/style_i_postcard/card.png" width="180"><br><sub>Postcard 明信片</sub></td>
</tr>
<tr>
<td align="center"><img src="examples/style_z2_metro_map/card.png" width="180"><br><sub>Metro Map 地铁线路图</sub></td>
<td align="center"><img src="examples/style_a4_manga_panel/card.png" width="180"><br><sub>Manga Panel 漫画分镜</sub></td>
<td colspan="2"></td>
</tr>
</table>

---

## Supported AI Tools

Ink automatically scans for these tools on your machine (zero configuration):

### Coding Assistants
Claude Code · Codex · Cursor · Windsurf · Aider · Continue.dev · Cline · Roo Code · GitHub Copilot

### AI Chat (Desktop)
Claude Desktop · ChatGPT Desktop · Gemini Desktop

### Local Models
Ollama · LM Studio · Jan · GPT4All

### Terminal & Productivity
Warp AI · Raycast AI

Don't see your tool? Ink also accepts a **custom JSON file** with your conversation data:

```
/ink --data ~/my-ai-stats.json
```

---

## Output

- **Format**: PNG, 1170 × 1560 px (3:4, Retina-ready)
- **Saved to**: Desktop by default
- **Filename**: `Ink_2026W26.png`
- **Watermark**: Small "Made with Ink" at the bottom — your card is its own advertisement

---

## Install

```bash
npx skills add quzhi-ai/ink
```

Or manually:

```bash
git clone https://github.com/quzhi-ai/ink.git
cp -r ink/skill/ink ~/.claude/skills/
```

Then:

```
/ink
```

---

## Architecture

```
ink/
├── README.md                  # English (this file)
├── README.zh.md               # 中文
├── LICENSE                    # MIT
├── skill/
│   └── ink/                   # The actual Claude Code skill
│       ├── SKILL.md           # Skill definition + taste baseline + workflow
│       ├── references/        # Style mode definitions, scanning paths
│       └── scripts/
│           └── render_png.py  # Puppeteer/Chrome headless → PNG export
├── docs/                      # Same reference files, GitHub-browsable
├── examples/                  # Demo cards with source HTML + output PNG
├── demos/
│   └── donate/                # Support the project (WeChat Pay + Alipay)
└── assets/
    └── hero-collage.png       # README hero image
```

---

## Privacy

Ink only reads **metadata** (timestamps and source names) from your AI tools. It **never reads your conversation content**. Your prompts and responses stay private.

---

## Dependencies

```
Node.js          # For Puppeteer PNG rendering
Google Chrome    # Headless screenshot engine
```

Both are standard on most developer machines. No additional packages needed.

---

## Support the Project

If Ink has been useful, consider buying the author a coffee:

| WeChat Pay | Alipay |
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

MIT — see [LICENSE](LICENSE)

---

<p align="center">
  <em>Your AI conversations leave marks. Ink makes them beautiful.</em>
</p>
