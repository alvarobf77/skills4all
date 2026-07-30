---
name: lut-cinematico
description: Genera LUTs 3D (.cube) con estilo pastel/cinematográfico limpio para video, listos para Premiere, DaVinci Resolve, Final Cut u OBS. Úsala siempre que el usuario pida un LUT, preset de color, look cinematográfico, grading pastel, o quiera un archivo .cube/.LUT para sus videos de YouTube u otro contenido. También úsala si pide ajustar la intensidad de un LUT ya generado (sutil/moderado/fuerte), variantes de un look, o una previsualización antes/después de un grading.
---

# LUT Cinemático Pastel

Genera LUTs 3D (formato `.cube`, tamaño 33×33×33 por defecto = 35,937 entradas) con un look
pastel/cinematográfico limpio: negros levantados, luces comprimidas con rolloff suave,
desaturación ligera y split-toning frío en sombras / cálido en luces.

## Flujo de trabajo

1. **Pregunta la intensidad** si el usuario no la especificó, usando opciones cortas:
   - Sutil (casi natural, solo suaviza)
   - Moderado (look pastel notorio)
   - Fuerte (estética muy estilizada)

2. **Genera el LUT** con `scripts/generate_lut.py`:
   ```bash
   python3 scripts/generate_lut.py --intensity moderado --output MiLUT.cube
   ```
   Parámetros ajustables si el usuario pide algo más específico (ver `--help` en el script):
   `--size` (17/33/65), `--lift`, `--gain`, `--gamma`, `--sat`, `--shoulder`,
   `--split-cool`, `--split-warm`, `--title`.

3. **Genera un preview antes/después** con `scripts/preview.py` (usa las mismas franjas
   representativas: piel, cielo, pasto, atardecer, sombra, blanco) para que el usuario
   verifique el resultado sin tener que importar el LUT a su editor:
   ```bash
   python3 scripts/preview.py --intensity moderado --output preview.png
   ```
   Muestra la imagen con `view` antes de entregar el archivo final.

4. **Copia ambos archivos a `/mnt/user-data/outputs/`** y preséntalos con `present_files`.

5. **Aclara siempre en tu respuesta**: el `.cube` es un archivo LUT estándar (LUT = Look-Up
   Table); algunas apps lo etiquetan como `.LUT` pero es el mismo formato — funciona en
   Premiere (Lumetri → Browse), DaVinci Resolve (Color → LUTs → clic derecho en carpeta → Add),
   Final Cut Pro (arrastrar a la carpeta de LUTs de macOS) y OBS.

## Ajustes finos post-entrega

Si el usuario pide cambios tras ver el resultado, no regeneres todo desde cero explicando
teoría de color — solo ajusta el parámetro correspondiente y vuelve a correr los scripts:

| El usuario dice... | Ajusta |
|---|---|
| "muy lavado" / "negros muy grises" | bajar `--lift` |
| "se ven quemadas las luces" | bajar `--gain` o subir `--shoulder` |
| "muy desaturado" / "se ve gris" | subir `--sat` (más cerca de 1.0) |
| "quiero más contraste" | subir `--gamma` (o acercarlo a 1.0) |
| "más teal-naranja" / "más cinematográfico" | subir `--split-cool` y `--split-warm` |
| "muy amarillo/naranja en general" | bajar `--split-warm` |
| "archivo muy pesado" / "lento de cargar" | bajar `--size` a 17 |

## Notas técnicas

- El grading se aplica en orden: gamma → gain (con tinte cálido) → lift (con tinte frío) →
  rolloff de luces → desaturación HSV. Este orden evita que el tinte de sombras/luces se
  pierda al desaturar.
- `PRESETS` en `generate_lut.py` define los tres niveles base (sutil/moderado/fuerte);
  edítalos ahí si el usuario pide cambiar los defaults de forma permanente.
- Los scripts no requieren conexión a red ni dependencias fuera de `numpy` y `pillow`
  (ya disponibles en el entorno).
