---
name: ink
description: |
  Scan local AI tools, count conversation turns, generate a beautiful social sharing card.
  Use this skill when the user wants to:
  (1) See their AI conversation statistics (daily / weekly / monthly)
  (2) Generate a shareable social media card from AI usage data
  (3) Run /ink, /ink week, /ink month, /ink day
  Supports: Claude Code, Codex, Cursor, Windsurf, Claude Desktop, ChatGPT Desktop, Ollama, LM Studio, and more.
---

# Ink 墨 — AI Conversation Statistics & Social Sharing

Scan every AI tool on the user's machine. Count conversation turns. Generate a stunning card. Export as PNG.

## Trigger

`/ink` — default last 7 days
`/ink day` — today only
`/ink month` — last 30 days
`/ink 2026-06-01 2026-06-26` — custom range

## Language

Ask the user on first run: **English** or **中文**. Remember the choice for subsequent runs.

---

## Workflow: First-Time Experience

The first time a user runs `/ink`, deliver a **Spotify Wrapped-style narrative reveal**. Each step is a "wow moment."

### Step 0 — Ask Name

Before anything else, ask the user's name:

> "Before we start — what name should appear on your card?"

Save the name to `~/.ink/name`. This name will appear on every card (e.g., "曲直" on a prescription, "曲直先生" in a newspaper headline, "Player: 曲直" on an NBA stats card). The card is theirs — their name makes it personal.

### Step 1 — Scan & Discover

Scan the user's machine for AI tools. Check known data paths (see [Data Scanning](#data-scanning) below). Report what you found:

> "I scanned your machine and found **3 AI tools**: Claude Code, Codex, Cursor."
> "Over the past 7 days, you talked to AI **713 times.**"

This is the first wow: the Skill found tools the user didn't even tell it about.

### Step 2 — Data Reveal

Walk through the highlights one by one:

- Total turns and daily average
- Peak day (which day, how many turns)
- Peak hour (what time of day is the user most active)
- Source breakdown (which AI tool gets the most love)
- Any surprising patterns ("You started using Claude Desktop on Wednesday — 4 days in and already 65 turns")

Each reveal should feel like discovering something about yourself.

### Step 3 — Style Selection

Present the style modes:

> "Pick your ink style:"
> 1. 正经反差 / Formal Contrast — serious formats, playful data (exam papers, prescriptions, imperial edicts)
> 2. 视觉美学 / Visual Art — stunning first impression (vinyl records, movie posters, tarot cards)
> 3. 极客硬核 / Geek Mode — data-dense, techy (terminal, NASA console, K-line charts)
> 4. 生活脑洞 / Life Remix — everyday objects reimagined (delivery orders, coffee sleeves, recipes)
> 5. 时空穿越 / Time Travel — cross-era mashups (old newspapers, telegrams, passports)
> 6. 随机惊喜 / Surprise Me — anything goes, maximum unpredictability

### Step 4 — Generate 3 Cards

Generate **3 different cards** in the chosen mode. Each card must:
- Use a completely different visual concept (not just color variations)
- Be sized at **1170 × 1560 px** (3:4 ratio, Retina 3x)
- Include all key statistics
- Include the **user's name** prominently (read from `~/.ink/name`) — woven naturally into the format (e.g., patient name on a prescription, headline subject in a newspaper, artist name on a vinyl record)
- Include one **original philosophical quote** (adapted from a real quote, not a direct copy)
- Include the text "Made with Ink" at the bottom in small type
- All text in the user's chosen language

Render all 3 using `show_widget` so the user can see them inline.

### Step 5 — Export

User picks one. Export as high-res PNG to Desktop:

> "Saved to Desktop: `Ink_2026W26.png`"
> "Go share it."

---

## Workflow: Returning User (Quick Mode)

After the first run, skip the narrative. Go straight to:

1. Scan (silent, show summary in one line)
2. Ask style mode (or use last choice if user just says `/ink`)
3. Generate 3 cards
4. User picks → Export

---

## Data Scanning

### Strategy

Scan known data directories for each AI tool. Only read **metadata** (timestamps, source, turn count). Never read conversation content.

### Known Paths (macOS)

| Tool | Path | What to Read |
|------|------|-------------|
| Claude Code | `~/.claude/projects/` | JSONL conversation logs — count entries with timestamps |
| Codex | `~/.codex/` | Session logs |
| Cursor | `~/Library/Application Support/Cursor/User/workspaceStorage/` | Chat history DB/JSON |
| Claude Desktop | `~/Library/Application Support/Claude/` | Conversation records |
| ChatGPT Desktop | `~/Library/Application Support/com.openai.chat/` | Local conversation cache |
| Windsurf | `~/Library/Application Support/Windsurf/` | AI chat logs |
| Aider | `~/.aider.chat.history.md`, `~/.aider/` | Chat history files |
| Ollama | `~/.ollama/` | Model interaction logs |
| LM Studio | `~/Library/Application Support/LM Studio/` | Chat history |
| Warp | `~/Library/Application Support/dev.warp.Warp-Stable/` | AI command logs |

### Known Paths (Windows)

| Tool | Path | What to Read |
|------|------|-------------|
| Claude Code | `%USERPROFILE%\.claude\projects\` | JSONL conversation logs |
| Codex | `%USERPROFILE%\.codex\` | Session logs |
| Cursor | `%APPDATA%\Cursor\User\workspaceStorage\` | Chat history |
| Claude Desktop | `%APPDATA%\Claude\` | Conversation records |
| ChatGPT Desktop | `%LOCALAPPDATA%\Packages\*OpenAI*\` | Local conversation cache |
| Windsurf | `%APPDATA%\Windsurf\` | AI chat logs |

### Fallback: User-Provided JSON

If the user has a pre-collected JSON file (e.g., from an API scraper), accept it:

> `/ink --data ~/my-ai-stats.json`

Expected JSON structure:
```json
{
  "window": {"start": "2026-06-20", "end": "2026-06-26"},
  "summary": {
    "daily": {"2026-06-20": 91, "2026-06-21": 109, ...},
    "source_counts": {"claude-code": 293, "feishu": 355, "cursor": 65},
    "total": 713
  }
}
```

---

## Card Generation

### Taste Baseline

The following aesthetic principles define the quality bar. Every generated card must meet this standard:

**Layout & Structure:**
- Each card tells a story through its format — the format IS the content
- Data should be naturally woven into the format's language (e.g., boarding pass: departure = start date, arrival = end date, flight time = total turns)
- Must include: total turns, per-source breakdown, daily trend, peak day/hour, one philosophical quote

**Typography:**
- Chinese cards: use system Chinese fonts (PingFang SC, Songti SC, STKaiti)
- English cards: use system fonts (SF Pro, SF Mono, Georgia)
- Three-tier discipline: display/title font, body font, metadata/label font
- Never mix tiers in the same role

**Visual Quality:**
- No generic "AI slop" aesthetic (white + black + red accent, gradient backgrounds, decorative emoji)
- Every element must earn its space
- Color should serve meaning, not decoration
- Backgrounds should match the format (paper texture for old documents, dark for tech, warm for food/drink)

**Quote Rules:**
- Adapt a real philosopher/author/scientist quote to fit the AI conversation context
- Never use the original quote verbatim — always remix it
- The quote should feel like it was written for this exact card
- Attribution format: "— Original Author · adapted"

### The 5+1 Style Modes

**1. Formal Contrast (正经反差)**
Serious institutional formats filled with playful AI data. The humor comes from the gap between the solemn format and the silly content.
Examples: exam papers, prescriptions, bank statements, imperial edicts, report cards, court verdicts

**2. Visual Art (视觉美学)**
Cards that are beautiful first, informative second. Strong visual impact, art-directed layouts.
Examples: vinyl records, movie posters, tarot cards, star maps, wine labels, music players

**3. Geek Mode (极客硬核)**
Data-dense, technically precise. Appeals to developers and power users.
Examples: terminal CLI, NASA mission control, K-line stock charts, Apple Watch rings, cyberpunk IDs

**4. Life Remix (生活脑洞)**
Everyday objects reimagined as data carriers. Warm, funny, relatable.
Examples: food delivery orders, coffee sleeves, recipes, IKEA manuals, receipts, fortune cookies

**5. Time Travel (时空穿越)**
Cross-era and cross-culture mashups. Nostalgia meets futurism.
Examples: Republican-era newspapers, telegrams, passport stamps, boarding passes, postcards, manga panels

**6. Surprise Me (随机惊喜)**
No constraints. Generate something the user has never seen before. The more unexpected the format, the better. Push creative boundaries.

### Generation Constraints

- Output: complete, self-contained HTML + inline CSS
- Viewport: 390px wide (will be rendered at 3x for 1170px output)
- Aspect ratio: 3:4 (390 × 520 CSS px → 1170 × 1560 rendered px)
- All fonts: system fonts only (no external font loading)
- No JavaScript required
- No external images or resources
- "Made with Ink" in small text at bottom

---

## Image Export

### Using Puppeteer (Node.js)

```bash
node -e "
const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 520, deviceScaleFactor: 3 });
  await page.setContent(HTML_CONTENT);
  await page.screenshot({ path: OUTPUT_PATH, type: 'png' });
  await browser.close();
})();
"
```

### Fallback: Chrome Headless

```bash
google-chrome --headless --screenshot=OUTPUT_PATH --window-size=390,520 --force-device-scale-factor=3 INPUT_HTML
```

### Output

- Default save location: `~/Desktop/`
- Filename: `Ink_{period}.png` (EN) or `墨_{period}.png` (CN)
- Period format: `2026W26` (week) / `2026-06-27` (day) / `2026-06` (month)

---

## State

Track minimal state in `~/.ink/`:
- `~/.ink/name` — user's display name (shown on every card)
- `~/.ink/lang` — user's language preference (`en` or `zh`)
- `~/.ink/last_mode` — last selected style mode
- `~/.ink/first_run_done` — whether to show narrative or quick mode
