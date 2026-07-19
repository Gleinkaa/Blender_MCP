# 👋 Start here

This folder is a **Blender project you can build with an AI helper** (Claude Code)
without worrying about it breaking your files. You don't need to be technical.

## The simple idea: two kinds of stuff

Think of the folders like a kitchen with a **red zone** and a **green zone**.

### 🟥 Red zone — YOUR stuff. The AI can't touch it.
| Folder     | Put this here                          |
|------------|----------------------------------------|
| `scenes/`  | Your Blender files (`.blend`)          |
| `assets/`  | Textures, sounds, and video you import |
| `renders/` | Finished pictures & videos come out here |

The AI is **locked out** of these on purpose. Even if it tried, it can't open or
change them. Your artwork is safe.

### 🟩 Green zone — the AI's workshop. Let it work here freely.
| Folder     | What it's for                                    |
|------------|--------------------------------------------------|
| `scripts/` | Little Python "tools" the AI writes to do jobs   |
| `notes/`   | Your ideas, briefs, references — anything in words |

## How you actually use it

1. **Open Blender** and start the little server (one-time setup is in
   [`engine/SKILL.md`](engine/SKILL.md) — install the add-on, press `N`, click
   *Start Server*).
2. **Drop your files** in the red-zone folders above.
3. **Write your idea** in `notes/` (e.g. "make a slowly spinning wooden chair on
   a white background") — or just tell the AI directly.
4. **Ask the AI** in plain words. It writes a small tool in `scripts/`, sends it
   to Blender, and your scene updates. You watch it happen in Blender.

That's it. You describe what you want; it does the fiddly button-pushing.

## Why the red/green split? (30-second version)

Blender files and images are "sealed boxes" of computer data. If the AI tries to
read them, it just sees noise (and it costs you money). If it tries to *edit*
them, it can wreck them. So we keep those boxes locked and let the AI work only
with plain writing and code — the stuff it's actually good and safe with.

## Good to know

- Everything the AI does is **tracked** (via Git). If something goes wrong, changes
  can be undone. Your `.blend` files are only ever changed *by Blender itself*,
  never by the AI directly.
- The locked-file list lives in `.claude/settings.json`. You can add more file
  types to block, but you never need to touch it to get started.
- Want to grow later (more automation, other apps like After Effects)? The
  research notes this was based on cover it — but you don't need any of that now.

## The map

```
📁 Your project
├── 👉 START-HERE.md      ← you are here
│
├── 🟩 scripts/           the AI's tools (safe to let it edit)
├── 🟩 notes/             your ideas & briefs (words)
│
├── 🟥 scenes/            your .blend files      (AI locked out)
├── 🟥 assets/            textures / audio / video (AI locked out)
├── 🟥 renders/           finished output        (AI locked out)
│
└── ⚙️ engine/            the add-on that lets the AI talk to Blender
```
