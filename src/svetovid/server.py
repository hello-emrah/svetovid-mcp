"""Svetovid MCP server: the entry point that registers the tool modules."""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from .tools import perception, state

mcp = FastMCP("svetovid")

state.register(mcp)
perception.register(mcp)


def main() -> None:
    """Run the server over stdio (the default MCP transport)."""
    mcp.run()


if __name__ == "__main__":
    main()
