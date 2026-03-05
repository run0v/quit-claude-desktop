# Quit Claude Desktop

A lightweight macOS utility that closes **Claude Desktop** without affecting **Claude Code** or other processes.

## Features

- Targets Claude Desktop exclusively by Bundle ID (`com.anthropic.claudefordesktop`)
- Runs silently — no terminal window, no Dock icon
- Graceful shutdown with SIGTERM, falls back to force-quit if needed
- Universal Binary — runs natively on both Intel (x86_64) and Apple Silicon (arm64)
- Supports all macOS icon resolutions

## Project Structure

```
quit-claude-desktop/
├── Sources/
│   └── main.swift               # Application source
├── Assets/
│   └── AppIcon.iconset/         # Icon source files (all macOS sizes)
├── Scripts/
│   ├── build.sh                 # Build script
│   └── generate_icon.py        # Icon generator (Python + Pillow)
├── dist/
│   └── Quit Claude Desktop.app/ # Built app bundle
├── docs/
│   └── system-monitor.png       # Reference screenshot
├── .gitignore
└── README.md
```

## Requirements

- macOS 12+
- Xcode Command Line Tools (`xcode-select --install`)
- Python 3 + Pillow (`pip3 install Pillow`) — only for icon regeneration

## Compatibility

| Architecture | Chips | Support |
|---|---|---|
| `arm64` | Apple Silicon (M1 / M2 / M3 / M4) | Native |
| `x86_64` | Intel (2006–2020) | Native |

The app is compiled as a **Universal Binary** via `lipo`. No Rosetta 2 required.

## Build

```bash
bash Scripts/build.sh
```

Rebuild with icon update:

```bash
bash Scripts/build.sh --icon
```

To verify the binary after building:

```bash
lipo -info "dist/Quit Claude Desktop.app/Contents/MacOS/kill_claude"
# Architectures in the fat file: ... are: x86_64 arm64
```

## Usage

Double-click `dist/Quit Claude Desktop.app`.

For quick access, assign a keyboard shortcut via:
`System Settings → Keyboard → Keyboard Shortcuts → App Shortcuts`

## How It Works

1. Finds all running apps with Bundle ID `com.anthropic.claudefordesktop`
2. Calls `app.terminate()` (graceful)
3. Waits 1.5 seconds
4. Calls `app.forceTerminate()` if the process is still alive

## Why Not `kill` / `ps`?

The original `ps + kill` approach matched any process containing "claude" in its name, which also terminated Claude Code. Using `NSWorkspace` with a specific Bundle ID ensures only Claude Desktop is affected.
