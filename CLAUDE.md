# Project rules for Claude Code (the AI assistant)

This is a Blender art project. You control Blender by **sending it code over a
socket**, never by editing its files. Follow these rules.

## The one rule that matters most
- **Never open, read, or edit files in `scenes/`, `assets/`, or `renders/`.**
  They are binary (`.blend`, images, audio, video). Reading them wastes tokens;
  editing them corrupts them. The permission settings block this — don't fight it.
- All the code you write lives in `scripts/` as plain `.py` text files.

## Where things go
| Folder      | What's in it                        | You may... |
|-------------|-------------------------------------|------------|
| `scripts/`  | Python tools you write              | read + edit freely |
| `notes/`    | The artist's briefs & ideas (text)  | read + edit |
| `scenes/`   | `.blend` files                      | **blocked** |
| `assets/`   | textures, audio, video              | **blocked** |
| `renders/`  | finished image/video output         | **blocked** |
| `engine/`   | the Blender add-on that listens     | read only |

## How to actually change the Blender scene
Blender must be open with the add-on server running (see `engine/SKILL.md`).
Send Python (`bpy`) code to **TCP port 9876** as JSON:

    {"type": "execute_code", "params": {"code": "<your bpy code>"}}

The socket helper and common `bpy` patterns are in `engine/SKILL.md` — read that
before writing Blender code. Render output paths must be **absolute**.

## Working style
- Prefer small, reversible steps. Break big scenes into several calls.
- Put reusable logic in a `.py` file under `scripts/`, don't paste giant blobs.
- If you learn something the hard way (an API quirk, a fix), add a short note
  here so you don't repeat the mistake.
