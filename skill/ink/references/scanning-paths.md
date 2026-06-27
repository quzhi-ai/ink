# AI Tool Scanning Paths

## macOS

| Tool | Category | Path | Data Format |
|------|----------|------|-------------|
| Claude Code | Coding | `~/.claude/projects/` | JSONL with timestamps |
| Codex | Coding | `~/.codex/` | Session logs |
| Cursor | Coding | `~/Library/Application Support/Cursor/User/workspaceStorage/` | SQLite / JSON |
| Windsurf | Coding | `~/Library/Application Support/Windsurf/User/workspaceStorage/` | JSON |
| Aider | Coding | `~/.aider.chat.history.md` and `~/.aider/` | Markdown logs |
| Continue.dev | Coding | `~/.continue/` | JSON session files |
| Cline | Coding | VS Code extension storage under `~/Library/Application Support/Code/User/globalStorage/` | JSON |
| Claude Desktop | Chat | `~/Library/Application Support/Claude/` | JSON / SQLite |
| ChatGPT Desktop | Chat | `~/Library/Application Support/com.openai.chat/` | Local cache |
| Ollama | Local | `~/.ollama/` | Interaction logs |
| LM Studio | Local | `~/Library/Application Support/LM Studio/` | Chat history JSON |
| Jan | Local | `~/jan/` | Thread JSON files |
| GPT4All | Local | `~/Library/Application Support/nomic.ai/GPT4All/` | Chat DB |
| Warp AI | Terminal | `~/Library/Application Support/dev.warp.Warp-Stable/` | AI command logs |
| Raycast AI | Productivity | `~/Library/Application Support/com.raycast.macos/` | AI chat logs |

## Windows

| Tool | Category | Path | Data Format |
|------|----------|------|-------------|
| Claude Code | Coding | `%USERPROFILE%\.claude\projects\` | JSONL with timestamps |
| Codex | Coding | `%USERPROFILE%\.codex\` | Session logs |
| Cursor | Coding | `%APPDATA%\Cursor\User\workspaceStorage\` | SQLite / JSON |
| Windsurf | Coding | `%APPDATA%\Windsurf\User\workspaceStorage\` | JSON |
| Aider | Coding | `%USERPROFILE%\.aider.chat.history.md` | Markdown logs |
| Claude Desktop | Chat | `%APPDATA%\Claude\` | JSON / SQLite |
| ChatGPT Desktop | Chat | `%LOCALAPPDATA%\Packages\*OpenAI*\` | Local cache |
| Ollama | Local | `%USERPROFILE%\.ollama\` | Interaction logs |
| LM Studio | Local | `%USERPROFILE%\.cache\lm-studio\` | Chat history JSON |
| Jan | Local | `%USERPROFILE%\jan\` | Thread JSON files |

## Scanning Logic

1. Detect OS (`process.platform` or `uname`)
2. For each tool in the table above, check if the path exists
3. If exists → read files, extract timestamps and **count only user-sent messages** (never AI responses, tool results, or system messages)
4. Group by: date, hour, source
5. Skip any tool that is not installed (silent, no error)

### Counting Rules (Critical)

Each tool stores both user input and AI output. **Only count user input turns:**

- **Claude Code** (`~/.claude/projects/`): JSONL entries where `type == "user"`. Exclude entries where `message.content` is a list consisting entirely of `tool_result` blocks (these are automatic tool responses, not manual user input).
- **Codex** (`~/.codex/`): JSONL entries where `type == "event_msg"` and `payload.type == "user_message"`. Exclude automation sessions (sessions where `session_meta.originator == "Codex Desktop"` and only 1 `user_message` exists — these are cron-triggered, not manual).
- **Other tools**: Apply the same principle — filter for user-authored input only. Do not count AI replies, system messages, or automatically generated entries.

## Privacy Rule

**Only extract:**
- Timestamp (when)
- Source tool name (which AI)
- Turn count (how many)

**Never extract:**
- Message content
- User prompts
- AI responses
- File paths discussed
- Any PII
