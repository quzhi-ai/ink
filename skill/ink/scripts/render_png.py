#!/usr/bin/env python3
"""
render_png.py — Render an Ink card HTML file to a high-res PNG.

Usage:
    python3 render_png.py card.html [output.png]

Requirements:
    - Google Chrome or Chromium installed
    - No other dependencies

Output:
    1170 × 1560 px PNG (3:4 ratio, 3x device scale factor)
"""

import subprocess
import sys
import os
import shutil
import tempfile


VIEWPORT_W = 390
VIEWPORT_H = 520
SCALE = 3  # 3x for Retina: 390*3=1170, 520*3=1560


def find_chrome():
    candidates = [
        # macOS
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        # Windows (common paths)
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        # Linux
        "google-chrome",
        "chromium-browser",
        "chromium",
    ]
    for c in candidates:
        if os.path.isfile(c) or shutil.which(c):
            return c
    return None


def render(html_path, output_path=None):
    if not os.path.isfile(html_path):
        print(f"Error: {html_path} not found", file=sys.stderr)
        sys.exit(1)

    chrome = find_chrome()
    if not chrome:
        print("Error: Google Chrome not found. Install Chrome or set CHROME_PATH.", file=sys.stderr)
        sys.exit(1)

    if output_path is None:
        base = os.path.splitext(os.path.basename(html_path))[0]
        output_path = f"{base}.png"

    abs_html = os.path.abspath(html_path)
    file_url = f"file://{abs_html}"

    with tempfile.TemporaryDirectory() as tmpdir:
        screenshot_path = os.path.join(tmpdir, "screenshot.png")

        cmd = [
            chrome,
            "--headless=new",
            f"--screenshot={screenshot_path}",
            f"--window-size={VIEWPORT_W},{VIEWPORT_H}",
            f"--force-device-scale-factor={SCALE}",
            "--hide-scrollbars",
            "--disable-gpu",
            "--no-sandbox",
            file_url,
        ]

        subprocess.run(cmd, capture_output=True, check=True)

        shutil.move(screenshot_path, output_path)

    print(f"Saved: {output_path} ({VIEWPORT_W * SCALE}×{VIEWPORT_H * SCALE} px)")
    return output_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} card.html [output.png]")
        sys.exit(1)

    html = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    render(html, out)
