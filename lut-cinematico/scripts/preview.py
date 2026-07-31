#!/usr/bin/env python3
"""
Genera una imagen comparativa antes/después usando los mismos parámetros
de grading que generate_lut.py, sin necesidad de aplicar el .cube completo.

Uso:
    python3 preview.py --intensity moderado --output preview.png
"""

import argparse
import numpy as np
from PIL import Image
from generate_lut import PRESETS, build_grade_fn

SWATCHES = [
    (0.85, 0.62, 0.50),  # piel
    (0.35, 0.55, 0.80),  # cielo
    (0.30, 0.55, 0.25),  # pasto
    (0.90, 0.45, 0.20),  # atardecer / naranja
    (0.15, 0.15, 0.18),  # sombra / negro
    (0.95, 0.95, 0.93),  # blanco
]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--intensity", choices=PRESETS.keys(), default="sutil")
    p.add_argument("--output", type=str, default="preview_antes_despues.png")
    p.add_argument("--width", type=int, default=900)
    p.add_argument("--height", type=int, default=300)
    args = p.parse_args()

    grade_fn = build_grade_fn(**PRESETS[args.intensity])

    W, H = args.width, args.height
    img = np.zeros((H, W, 3), dtype=np.float64)
    band_w = W // len(SWATCHES)
    for i, c in enumerate(SWATCHES):
        img[:, i * band_w:(i + 1) * band_w] = c

    graded = np.zeros_like(img)
    for y in range(H):
        for x in range(0, W, band_w):
            graded[y, x:x + band_w] = grade_fn(img[y, x])

    before = Image.fromarray((img * 255).astype(np.uint8))
    after = Image.fromarray((graded * 255).astype(np.uint8))

    combo = Image.new("RGB", (W, H * 2 + 10), "white")
    combo.paste(before, (0, 0))
    combo.paste(after, (0, H + 10))
    combo.save(args.output)
    print(f"Preview guardado: {args.output}")


if __name__ == "__main__":
    main()
