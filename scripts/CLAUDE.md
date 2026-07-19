# Rules for the `scripts/` folder

This is your workshop. Everything here is plain-text Python — safe to create,
read, and edit.

## Conventions
- One tool per file, named for what it does: `make_turntable.py`, `apply_wood_material.py`.
- Each script should be runnable on its own and talk to Blender over the socket
  (port 9876). Reuse the `blender_exec()` helper from `engine/SKILL.md`.
- Keep secrets out. No API keys in these files — they get committed to Git.
- Render paths are **absolute** (e.g. write into the project's `renders/` folder
  using a full path), never relative.

## Before writing Blender code
Read `engine/SKILL.md` for the JSON protocol, the socket helper, and the common
`bpy` patterns (clear scene, add mesh, materials, keyframes, render).
