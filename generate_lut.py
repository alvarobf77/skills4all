#!/usr/bin/env python3
"""
Genera un LUT 3D (.cube) pastel/cinematográfico limpio, apto para YouTube.

Uso:
    python3 generate_lut.py --intensity sutil --output MiLUT.cube
    python3 generate_lut.py --intensity moderado --size 33 --split-warm 0.5 --split-cool 0.5
    python3 generate_lut.py --intensity fuerte --sat 0.8 --title "MiLook"

Parámetros clave (todos opcionales, tienen defaults por intensidad):
    --intensity   sutil | moderado | fuerte   (preset base, default: sutil)
    --size        tamaño de la malla del LUT, 17/33/65 (default: 33)
    --lift        cuánto se levantan los negros (0-0.1 aprox)
    --gain        compresión de blancos, <1.0 = más comprimido
    --gamma       curva de contraste, <1 más suave, >1 más contrastado
    --sat         multiplicador de saturación (1.0 = sin cambio)
    --shoulder    fuerza del rolloff de altas luces (0 = desactivado)
    --split-cool  fuerza del tinte frío en sombras
    --split-warm  fuerza del tinte cálido en luces
    --title       nombre interno del LUT (TITLE en el .cube)
    --output      ruta de archivo de salida (.cube)
"""

import argparse
import numpy as np
import colorsys

PRESETS = {
    # intensity: (lift, gain, gamma, sat, shoulder, split_cool, split_warm)
    "sutil":    dict(lift=0.018, gain=0.985, gamma=0.985, sat=0.94, shoulder=0.10, split_cool=0.006, split_warm=0.006),
    "moderado": dict(lift=0.035, gain=0.965, gamma=0.960, sat=0.85, shoulder=0.18, split_cool=0.012, split_warm=0.012),
    "fuerte":   dict(lift=0.055, gain=0.940, gamma=0.930, sat=0.75, shoulder=0.28, split_cool=0.022, split_warm=0.022),
}


def soft_shoulder(x, k):
    return x - k * (x ** 3) * (x > 0.6)


def build_grade_fn(lift, gain, gamma, sat, shoulder, split_cool, split_warm):
    lift_tint = np.array([-split_cool * 0.4, 0.0, split_cool])
    gain_tint = np.array([split_warm, split_warm * 0.35, -split_warm])

    def grade(rgb):
        rgb = np.clip(rgb, 0, 1)
        rgb = np.power(rgb, gamma)
        rgb = rgb * (gain + gain_tint)
        rgb = rgb + (lift + lift_tint)
        rgb = soft_shoulder(rgb, shoulder)
        rgb = np.clip(rgb, 0, 1)

        r, g, b = rgb
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        s *= sat
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        return np.clip(np.array([r, g, b]), 0, 1)

    return grade


def generate_cube(path, size, title, grade_fn):
    lines = [
        f'TITLE "{title}"',
        f"LUT_3D_SIZE {size}",
        "DOMAIN_MIN 0.0 0.0 0.0",
        "DOMAIN_MAX 1.0 1.0 1.0",
    ]
    for b_i in range(size):
        for g_i in range(size):
            for r_i in range(size):
                r = r_i / (size - 1)
                g = g_i / (size - 1)
                b = b_i / (size - 1)
                out = grade_fn(np.array([r, g, b]))
                lines.append(f"{out[0]:.6f} {out[1]:.6f} {out[2]:.6f}")
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
    return len(lines) - 4


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--intensity", choices=PRESETS.keys(), default="sutil")
    p.add_argument("--size", type=int, default=33, choices=[17, 33, 65])
    p.add_argument("--lift", type=float, default=None)
    p.add_argument("--gain", type=float, default=None)
    p.add_argument("--gamma", type=float, default=None)
    p.add_argument("--sat", type=float, default=None)
    p.add_argument("--shoulder", type=float, default=None)
    p.add_argument("--split-cool", type=float, default=None)
    p.add_argument("--split-warm", type=float, default=None)
    p.add_argument("--title", type=str, default=None)
    p.add_argument("--output", type=str, default="Pastel_Cinematic.cube")
    args = p.parse_args()

    params = dict(PRESETS[args.intensity])
    overrides = {
        "lift": args.lift, "gain": args.gain, "gamma": args.gamma, "sat": args.sat,
        "shoulder": args.shoulder, "split_cool": args.split_cool, "split_warm": args.split_warm,
    }
    for k, v in overrides.items():
        if v is not None:
            params[k] = v

    title = args.title or f"Pastel_Cinematic_{args.intensity.capitalize()}"
    grade_fn = build_grade_fn(**params)
    n_entries = generate_cube(args.output, args.size, title, grade_fn)

    print(f"LUT generado: {args.output}")
    print(f"  Tamaño: {args.size}x{args.size}x{args.size} ({n_entries} entradas)")
    print(f"  Intensidad base: {args.intensity}  |  Parámetros finales: {params}")


if __name__ == "__main__":
    main()
