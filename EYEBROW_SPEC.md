# Build Spec — Emotive Eyebrows for the White Chicken

Agreed via a `/grill-me` session. This is the authoritative brief for the build session.
**Execute exactly this. Do not re-litigate resolved decisions.**

## Environment (how to drive Blender)

- Blender runs on the **desktop**, reached over SSH: `ssh desktop-friend`.
  (SSH prints a post-quantum warning to stderr — ignore/grep it out.)
- The blender-mcp addon server listens on **localhost:9876 on the desktop** (JSON over TCP,
  no length prefix). `execute_code` captures `print()` stdout and returns it as `result`.
- Run driver scripts **on the desktop** (they must connect to the desktop's localhost). Pattern:
  `scp driver.py desktop-friend:'D:\blender_mcp_assets\driver.py'` then
  `ssh desktop-friend "python D:\blender_mcp_assets\driver.py"`.
- Helper `blender_exec(code)` and a working example live in `_inspect_driver.py` / `_shot_driver.py`.
- Asset already copied to the desktop and **already imported** into the live session:
  `D:\blender_mcp_assets\chicken\WhiteChicken_anim.fbx` (+ `textures\chicken_txtr.jpeg`).
  If the session was reset, re-import from that path (guard on: any ARMATURE present).

## Rig facts (verified)

- Objects: `Armature`, mesh `Body` (1205 v), empty `Chicken`, mesh **`Face`** (1322 v).
- Head bone: **`ChickenHead`**. Existing face bones incl. `ChickenUpperLip`, `ChickenLowerLip` (beak),
  and **`ChickenHeadBone003` / `ChickenHeadBone004` = the EYES** (symmetric, X=±10.7, Y≈120.7, Z≈28.1
  in armature-local space).
- **Axes:** Y = up (feet Y≈2 → head Y≈103–144), Z = forward (face front ≈ Z 23–35), X = left/right.
- **Scale:** FBX imported at ~0.01, so bone coords read ~100 in armature-local space while the mesh
  sits at ~1 unit in world. Reconcile carefully when placing geometry (place relative to the eyes,
  don't hardcode absolute units).

## What to build

**Geometry**
- Two **thin 3D slabs** (real depth), rounded-corner rectangles — one brow per eye. Separate mesh
  objects `Eyebrow_L`, `Eyebrow_R`.
- **Forehead-conformed orientation:** pitch each slab to follow the head-surface slope above its eye;
  float it just clear of the skin (no clipping).
- **Size derived from the MEASURED eye extents** on the `Face` mesh so it reads as proportional.
  Starting ratios (tune if a test render looks off):
  - width ≈ 1.1 × eye width
  - bar height ≈ 25–30% of width
  - depth ≈ 10% of width
  - corner radius ≈ 35% of bar height
  - vertical gap (eye-top → brow-bottom) ≈ 20% of eye height

**Material**
- Dedicated **matte black** material on both brows.

**Rig**
- **One unified armature** — add two bones into the existing `Armature`:
  `ChickenLBrow`, `ChickenRBrow`, each **parented to `ChickenHead`** (brows ride with the head).
- Each brow mesh is **bone-parented** (object → bone parent) to its bone. Two independent objects.
- **DOF per brow** (independent L/R, no mirroring/linking):
  - **Rotate** in the plane of the face about a **center pivot** of the brow
    (inner-end-down = angry, inner-end-up = sad). Rotation axis = the forward/depth axis through
    the brow center.
  - **Slide up/down** along the head's up-axis (raise = surprise, lower = glare).
  - Set bone roll / pivot so these two motions are the clean, obvious local transforms an animator
    reaches for.

## Verification (do this before saving)

1. Fix the screenshot pipeline (the earlier `screenshot_area` to `D:\blender_mcp_assets\head_shot.png`
   did not land on disk — write to Blender's temp dir / an absolute path that exists, then scp the
   PNG back to the laptop worktree and confirm it opens).
2. Pose & capture front-on screenshots of: **neutral, angry (inner ends down), surprised (both raised),
   skeptical (one brow up)**. Pull them back to the laptop for review.
3. **Reset to rest pose** before saving (test poses are for screenshots only).

## Delivery

- Save **`WhiteChicken_brows.blend`** on the desktop (e.g. `D:\blender_mcp_assets\chicken\`).
- Copy it back to the laptop at
  `D:\dev\Blender_MCP\Aschbach2026\rigged-white-chicken-character\source\WhiteChicken_brows.blend`.
- **Do not** re-export FBX. **Do not** git-commit the asset. Leave the original FBX untouched.
  Repo next-steps are the user's call.
