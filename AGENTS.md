# AGENTS.md — conventions for AI agents working in this repo

This is a Blender art project. Agents drive Blender by **sending Python over a
socket**, never by editing Blender's files. Read this before doing anything.

## Golden rules

- **Never open, read, or edit files in `scenes/`, `assets/`, or `renders/`.**
  They are binary (`.blend`, images, audio, video) — reading wastes tokens,
  editing corrupts them. Permissions block this; don't fight it.
- All code you write lives in `scripts/` as plain `.py` text.
- `engine/` (the addon that listens) is **read-only**.
- Prefer small, reversible steps. Break big scenes into several socket calls.

## Folder map

| Folder     | Contents                       | Agent access   |
|------------|--------------------------------|----------------|
| `scripts/` | Python tools you write         | read + edit    |
| `notes/`   | Artist briefs & ideas (text)   | read + edit    |
| `scenes/`  | `.blend` files                 | **blocked**    |
| `assets/`  | textures, audio, video         | **blocked**    |
| `renders/` | finished image/video output    | **blocked**    |
| `engine/`  | the Blender add-on that listens| read only      |

## Socket protocol

Blender must be running with the add-on server started (see
[engine/SKILL.md](engine/SKILL.md) for install/start steps). The server listens
on **TCP port 9876**.

- **Wire format:** plain UTF-8 JSON over TCP, **no length prefix**. Read until
  the accumulated buffer parses as complete JSON.
- **Request:**  `{"type": "<command>", "params": {<kwargs>}}`
- **Response:** `{"status": "success", "result": <value>}`
  or `{"status": "error", "message": "<reason>"}`

### Commands

| type                    | params            | description                    |
|-------------------------|-------------------|--------------------------------|
| `execute_code`          | `code` (str)      | Run arbitrary `bpy` Python     |
| `get_scene_info`        | (none)            | List all objects in the scene  |
| `get_object_info`       | `object_name`     | Details on a specific object   |
| `get_viewport_screenshot`| (none)           | Screenshot of current viewport |

### Conventions

- **Check the socket is open before sending:** `nc -z -w2 localhost 9876`.
- **Render output paths must be absolute**, never relative.
- **One concern per call.** Split complex scenes across multiple `execute_code`
  calls to avoid timeouts; don't paste giant blobs — put reusable logic in
  `scripts/*.py` and send a small driver instead.
- `shade_smooth()` needs the object selected and in object mode.
- The add-on server must be (re)started inside Blender each session
  (N-panel → BlenderMCP → Start Server); it does not autostart.

See [engine/SKILL.md](engine/SKILL.md) for the Python socket helper and common
`bpy` patterns (clear scene, add meshes, materials, keyframes, render).

## When you learn something the hard way

Add a one-line note here or in `CLAUDE.md` (an API quirk, a fix) so the next
agent doesn't repeat the mistake.
