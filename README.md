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

<!-- TODO: add hero image once generated -->
<!-- <p align="center">
  <img src="assets/hero-collage.png" width="900" alt="Ink card examples across 6 style modes" />
</p> -->

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
