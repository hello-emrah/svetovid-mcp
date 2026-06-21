<div align="center">

<img src="./assets/logo.png" alt="Svetovid" width="180" />

# Svetovid

**An MCP server that lets your agent see and edit video inside DaVinci Resolve Studio.**

<sub>Requires DaVinci Resolve <b>Studio</b> (the scripting API is Studio only)</sub>

</div>

---

Svetovid wires an AI agent into DaVinci Resolve. The agent can orient itself in your project, see the frame at the playhead, and assemble, grade and render on the timeline, working alongside you in the same project.

Named for the four faced Slavic god who watches in all directions. *Svet* is light, *vid* is sight, the same ancient root that gives us the word video.

## Why

Most tooling drives an editor blind, pushing metadata it cannot see. Svetovid is built perception first: the agent renders the actual frame and looks at it, so it edits against what is really on screen, not a guess.

## Requirements

- DaVinci Resolve **Studio** 18.5 or newer, running.
- External scripting enabled: Resolve, Preferences, System, General, **External scripting using** set to **Local**.
- Python 3.10 or newer.

## Install

```bash
pip install -e .
```

## Wire into Claude Code

```bash
claude mcp add svetovid -- svetovid-mcp
```

Or any MCP client, by running `svetovid-mcp` as the server command.

## Tools

| Tool | What it does |
|---|---|
| `get_state` | Orient. Returns the open project, the current timeline, frame rate, resolution, track counts and clip count. Call this first. |
| `render_current_frame` | See the edit. Exports the frame at the playhead and returns it as an image. |

More tools land as the build grows: media import, timeline assembly, markers, render and export.

## Environment

Resolve's scripting paths are auto-detected per platform. Override them in a `.env` only for a non-standard install (see `.env.example`).

## License

MIT. Built for personal use, shared openly, never productised.
