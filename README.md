# Blender MCP

Control a running Blender instance via JSON-over-TCP on port 9876.

**New here / not technical?** Read [`START-HERE.md`](START-HERE.md) first — it
explains the folder layout in plain language.

## Files

| File | Description |
|------|-------------|
| `engine/blender_mcp_addon.py` | Blender addon (v1.2) — install in Blender, start server from N-panel |
| `engine/SKILL.md` | Hermes skill — protocol docs, bpy patterns, helper snippets |
| `START-HERE.md` | Artist-facing guide to the project folders |

## Quick Start

1. Install addon in Blender: `Edit > Preferences > Add-ons > Install > Select engine/blender_mcp_addon.py`
2. Enable "Interface: Blender MCP"
3. Press N in viewport → "BlenderMCP" tab → "Start Server"
4. Verify: `nc -z -w2 localhost 9876 && echo OPEN`

## Protocol

Plain UTF-8 JSON over TCP (no length prefix).

Send:     {"type": "execute_code", "params": {"code": "..."}}
Receive:  {"status": "success", "result": ...}

Commands: `execute_code`, `get_scene_info`, `get_object_info`, `get_viewport_screenshot`
