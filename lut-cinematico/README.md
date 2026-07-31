# 🎨 LUT Cinemático Pastel — Skill para Claude

Genera LUTs 3D `.cube` con look pastel/cinematográfico limpio para video — listos para
Premiere, DaVinci Resolve, Final Cut Pro y OBS. Tú solo dices "hazme un LUT pastel para mis
videos de YouTube" y la skill se encarga de todo: parámetros de grading, archivo `.cube` y
una imagen de preview antes/después.

- 🎞️ **Look pastel/cinematográfico**: negros levantados, luces comprimidas con rolloff
  suave, desaturación ligera, split-toning frío en sombras / cálido en luces
- 🎚️ **3 niveles listos**: sutil, moderado, fuerte — o parámetros custom si quieres afinar
- 🖼️ **Preview automático**: genera una imagen antes/después con franjas de color
  representativas (piel, cielo, pasto, atardecer, sombra, blanco) sin necesidad de
  importar el LUT a tu editor para verificarlo
- 📦 **Formato estándar**: `.cube` de 33×33×33 (35,937 entradas), el formato universal de
  LUTs — funciona en cualquier software de edición de video

---

## ⚙️ Cómo funciona (por dentro)

```
intensidad → parámetros de grading (lift/gain/gamma/saturación/rolloff/split-tone)
           → genera malla 3D de 33×33×33 puntos → escribe archivo .cube
           → aplica el mismo grading a franjas de color de muestra → preview.png
```

- El grading se aplica en orden: **gamma → gain (tinte cálido) → lift (tinte frío) →
  rolloff de luces → desaturación HSV**. Este orden evita que el tinte de sombras/luces
  se pierda al desaturar.
- No depende de ningún servicio externo, API key, ni conexión a internet — corre 100%
  local con `numpy` y `pillow`, ya disponibles en el entorno de Claude.
- Costo: $0, no consume ninguna API de pago.

---

## 📥 Instalación

### Claude.ai (web, escritorio o móvil)

1. Descarga la carpeta `lut-cinematico/` de este repo y comprímela en `.zip` (el `.zip`
   debe contener la carpeta `lut-cinematico` en su raíz — el nombre debe coincidir
   exactamente con `name: lut-cinematico` del frontmatter de `SKILL.md`).
2. Perfil → **Settings → Capabilities → Skills → + Upload skill** (requiere plan
   Pro/Max/Team/Enterprise y *Code execution* activado).
3. Sube el `.zip` y actívala con el toggle.

### Claude Code (terminal, VSCode, JetBrains, o la app de escritorio)

Instala en todos tus proyectos:
```bash
git clone https://github.com/alvarobf77/skills4all.git
cp -r skills4all/lut-cinematico ~/.claude/skills/
```

O solo en un proyecto específico (se versiona junto con tu código):
```bash
mkdir -p .claude/skills
cp -r skills4all/lut-cinematico .claude/skills/
```

Reinicia Claude Code (o abre una sesión nueva) para que la detecte.

### Otros IDEs (Cursor, Windsurf, Antigravity, Copilot, etc.)

Estos no leen el formato `SKILL.md` de forma nativa — es específico de Anthropic/Claude.
Copia y pega el contenido de [`SKILL.md`](./SKILL.md) directo en el chat del asistente como
instrucciones, o pégalo en el archivo de reglas propio del IDE (`.cursorrules`,
`.windsurfrules`, etc.) si quieres que persista entre sesiones.

---

## 🚀 Uso

```
hazme un LUT pastel para mis videos de YouTube
```
```
quiero un look cinematográfico moderado para mi canal
```
```
dame una variante más fuerte de mi LUT pastel
```

La skill pregunta la intensidad si no la especificaste, genera el `.cube` + el preview, y
te explica qué ajustar si el resultado no es exactamente lo que buscabas.

### Opciones

- **Intensidad**: `sutil` (casi natural) · `moderado` (pastel notorio) · `fuerte`
  (estilizado)
- **Tamaño del LUT**: 17 (más liviano) · 33 (default, estándar de industria) · 65
  (máxima precisión, archivo más pesado)
- **Ajustes finos**: `--lift`, `--gain`, `--gamma`, `--sat`, `--shoulder`, `--split-cool`,
  `--split-warm` — ver tabla de ajustes rápidos en [`SKILL.md`](./SKILL.md#ajustes-finos-post-entrega)

---

## 🍬 ¿Por qué es útil?

- **No hay que abrir DaVinci o Premiere para probar look**: el preview antes/después se
  genera en segundos, directo en el chat.
- **Reproducible**: los mismos parámetros siempre generan el mismo LUT — útil si manejas
  varios canales o clientes y quieres consistencia de marca visual.
- **Sin credenciales ni APIs externas**: cero fricción de configuración, cero costo
  variable.
- **Ajustable en lenguaje natural**: "se ven quemadas las luces" o "muy desaturado" son
  suficiente — la skill sabe qué parámetro tocar.

---

## 🧰 Requisitos

- Claude.ai (Pro/Max/Team/Enterprise) o Claude Code
- Code execution / entorno con Python 3, `numpy` y `pillow` (ya incluido en el entorno de
  Claude — no requiere instalación adicional de tu parte)
- Ningún API key ni cuenta de terceros

---

## 📄 Licencia

MIT — úsalo, modifícalo, compártelo.

Hecho con 🎨 para la comunidad de **Infinitix Group**.
