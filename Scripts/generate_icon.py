import os
import math
from PIL import Image, ImageDraw

def draw_icon(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = size / 2, size / 2
    r = size / 2

    # Background: rounded square (squircle-like), dark navy
    pad = size * 0.04
    draw.rounded_rectangle(
        [pad, pad, size - pad, size - pad],
        radius=size * 0.22,
        fill=(28, 27, 46, 255)
    )

    # Outer arc of power symbol (gap at top ~60 degrees)
    arc_r = r * 0.54
    arc_width = max(1, int(size * 0.075))
    gap_deg = 60
    start = 90 + gap_deg / 2
    end = 90 - gap_deg / 2 + 360

    bbox = [
        cx - arc_r, cy - arc_r,
        cx + arc_r, cy + arc_r
    ]
    draw.arc(bbox, start=start, end=end, fill=(220, 60, 60, 255), width=arc_width)

    # Vertical line (power stem) going up through the gap
    stem_top = cy - arc_r * 1.05
    stem_bottom = cy - arc_r * 0.28
    hw = arc_width / 2
    draw.rounded_rectangle(
        [cx - hw, stem_top, cx + hw, stem_bottom],
        radius=hw,
        fill=(220, 60, 60, 255)
    )

    # Small Claude-style dots (three dots like Anthropic logo halo)
    dot_r_orbit = r * 0.72
    dot_size = max(1, size * 0.045)
    for angle_deg in [210, 270, 330]:
        angle = math.radians(angle_deg)
        dx = cx + dot_r_orbit * math.cos(angle)
        dy = cy + dot_r_orbit * math.sin(angle)
        draw.ellipse(
            [dx - dot_size, dy - dot_size, dx + dot_size, dy + dot_size],
            fill=(160, 140, 220, 200)
        )

    return img


sizes = {
    "icon_16x16.png": 16,
    "icon_16x16@2x.png": 32,
    "icon_32x32.png": 32,
    "icon_32x32@2x.png": 64,
    "icon_128x128.png": 128,
    "icon_128x128@2x.png": 256,
    "icon_256x256.png": 256,
    "icon_256x256@2x.png": 512,
    "icon_512x512.png": 512,
    "icon_512x512@2x.png": 1024,
}

iconset_path = os.path.join(os.path.dirname(__file__), "..", "Assets", "AppIcon.iconset")
os.makedirs(iconset_path, exist_ok=True)

for filename, size in sizes.items():
    img = draw_icon(size)
    img.save(os.path.join(iconset_path, filename))
    print(f"Generated {filename} ({size}x{size})")

print("Done.")
