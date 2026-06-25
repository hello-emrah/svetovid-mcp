<div align="center">

<img src="assets/logo.png" alt="Svetovid" width="160" />

# Svetovid

**An MCP server for seeing and editing video in DaVinci Resolve Studio.**

Svetovid is the four faced Slavic god who watches every direction at once, the all seer. *Svet* is light, *vid* is sight, the same ancient root that gives us the word video. The name signals the one thing most tooling cannot do: see.

<a href="https://www.buymeacoffee.com/hello_emrah"><img src="https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=%E2%98%95&slug=hello_emrah&button_colour=9686D8&font_colour=3a2a10&coffee_colour=3a2a10&outline_colour=3a2a10&font_family=Inter" alt="Buy me a coffee" height="44" /></a>

</div>

---

Svetovid is a Model Context Protocol server for DaVinci Resolve Studio. Most tools drive an editor blind, pushing metadata they cannot see. Svetovid renders the frame at the playhead and hands it back, so the agent works from what is really on screen, not a guess. It speaks to Resolve over its scripting API, and you and the agent share the same open project. Built for personal use, shared openly, not productised.

Runs on your machine, alongside your open Resolve project.

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

MIT, see [LICENSE](LICENSE).
