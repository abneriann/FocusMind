"""Gera PNGs transparentes a partir dos SVGs do pack FocusMind.

Uso:
  python -m pip install cairosvg
  python scripts/generate_icon_pngs.py

Os SVGs originais nunca são alterados.
"""
from pathlib import Path
import cairosvg

ROOT = Path(__file__).resolve().parents[1] / "assets" / "icons"
SRC = ROOT / "svg"
DEST = ROOT / "png"
size_large = {"modulos", "badges"}

for svg in sorted(SRC.rglob("*.svg")):
    subdir = svg.parent.relative_to(SRC)
    target = DEST / subdir / f"{svg.stem}.png"
    target.parent.mkdir(parents=True, exist_ok=True)
    size = 512 if subdir.parts[0] in size_large else 256
    cairosvg.svg2png(url=str(svg), write_to=str(target),
                     output_width=size, output_height=size)
    print(target.relative_to(ROOT))
