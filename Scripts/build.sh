#!/bin/bash
set -e

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
APP="$ROOT/dist/Quit Claude Desktop.app"
BINARY="$APP/Contents/MacOS/kill_claude"

echo "Building Quit Claude Desktop (Universal Binary)..."
swiftc "$ROOT/Sources/main.swift" -target x86_64-apple-macos12.0 -o /tmp/kill_claude_x86_64
swiftc "$ROOT/Sources/main.swift" -target arm64-apple-macos12.0  -o /tmp/kill_claude_arm64
lipo -create /tmp/kill_claude_x86_64 /tmp/kill_claude_arm64 -output "$BINARY"
rm /tmp/kill_claude_x86_64 /tmp/kill_claude_arm64
echo "Build successful ($(lipo -archs "$BINARY")): $BINARY"

# Rebuild icon if needed
if [ "$1" == "--icon" ]; then
  echo "Regenerating icon..."
  python3 "$ROOT/Scripts/generate_icon.py"
  iconutil -c icns "$ROOT/Assets/AppIcon.iconset" -o "$APP/Contents/Resources/AppIcon.icns"
  touch "$APP"
  killall Finder 2>/dev/null || true
  echo "Icon updated."
fi

echo "Done."
