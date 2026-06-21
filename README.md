<p align="center">
  <img src="assets/logo.png" alt="Svetovid" width="240" />
</p>

<h1 align="center">Svetovid</h1>

<p align="center">
  An MCP server for seeing and editing video in DaVinci Resolve Studio.<br/>
  Orient, see the frame, assemble, grade, render.<br/>
  <strong>The agent renders the real frame and looks at it.</strong>
</p>

<p align="center">
  <a href="https://buymeacoffee.com/hello_emrah"><img src="https://img.shields.io/badge/Buy%20me%20a%20coffee-c46b44?logo=buymeacoffee&logoColor=ffffff&style=for-the-badge" alt="Buy Me a Coffee" /></a>
</p>

---

Svetovid is the four faced Slavic god who watches every direction at once, the all seer. *Svet* is light, *vid* is sight, the same ancient root that gives us the word video. The name signals the one thing most tooling cannot do: see. This MCP server lets the model driving Claude Code look at the actual frame on your timeline and edit against it.

Most tools drive an editor blind, pushing metadata they cannot see. Svetovid renders the frame at the playhead and hands it back, so the agent works from what is really on screen, not a guess. It speaks to DaVinci Resolve Studio over its scripting API, and you and the agent share the same open project.

## Tools

| Tool | What it does |
|---|---|
| `get_state` | Orient. Returns the open project, the current timeline, frame rate, resolution, track counts, clip count and timecode. Call this first. |
| `render_current_frame` | See the edit. Exports the frame at the playhead and returns it as an image. |

More tools land as the build grows: media import, timeline assembly, markers, render and export, each destructive action behind a confirm gate.

## Requirements

- DaVinci Resolve **Studio** 18.5 or newer, running. The scripting API is Studio only.
- External scripting enabled: Resolve, Preferences, System, General, **External scripting using** set to **Local**.
- Python 3.10 or newer.

## Install

```bash
git clone https://github.com/hello-emrah/svetovid-mcp.git
cd svetovid-mcp
pip install -e .
```

## Wire into Claude Code

Add an entry to `~/.claude.json` under `mcpServers`:

```json
{
  "mcpServers": {
    "svetovid": {
      "command": "svetovid-mcp"
    }
  }
}
```

Restart Claude Code. The tools appear under the `mcp__svetovid__*` namespace.

## Environment

Resolve's scripting paths are auto-detected per platform. Set `RESOLVE_SCRIPT_API` and `RESOLVE_SCRIPT_LIB` in a `.env` only for a non-standard install (see `.env.example`).

## Why "Svetovid"

Svetovid stood on the island of Rügen as a four faced idol, looking north, south, east and west so nothing could pass him unseen, the god of light, sight and divination. The name carries the whole idea of this tool: an editor the agent can see through, watching the timeline from every side. And the root underneath it, *vid*, to see, is the same one that surfaces in the word video.

## Design philosophy

The visual mark and the tool itself were built deliberately against the visual language of capitalist software design. No gradients, no neon, no glass, no drop shadows, no isometric stock illustration. Single-shade flat seals in warm earth tones, ancient-glyph silhouettes, generous whitespace. The mark could be pressed into wax or carved into stone.

This tool is built for personal use and shared openly. It is not productised, monetised, or instrumented. Use it for your own work or fork it for yours.

## License

MIT
