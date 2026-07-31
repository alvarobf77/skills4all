# Instalación rápida — lut-cinematico

Tres formas de instalarla, según dónde uses Claude. Elige la tuya.

---

## 1. Claude.ai (web, escritorio o móvil)

Requiere plan Pro/Max/Team/Enterprise y **Code execution** activado.

1. Descarga la carpeta `lut-cinematico/` completa de este repo (o el `.zip`/`.skill` ya
   empaquetado si está disponible en la sección de releases).
   - Si descargas la carpeta suelta: comprímela en `.zip` — el `.zip` debe contener la
     carpeta `lut-cinematico` en su raíz (no los archivos sueltos), y el nombre de la
     carpeta debe coincidir exactamente con `name: lut-cinematico` del frontmatter de
     `SKILL.md`.
2. En claude.ai: perfil → **Settings** → **Capabilities** (o **Customize** → **Skills**
   según tu plan) → **Skills** → **+ Upload skill**.
3. Selecciona el `.zip` (o `.skill`) y confirma.
4. Actívala con el toggle. Listo — a partir de ahora se dispara sola cuando pidas un LUT,
   look cinematográfico, o grading pastel para video.

No requiere comandos ni terminal.

---

## 2. Claude Code (terminal, VSCode, JetBrains, o la app de escritorio)

Claude Code lee skills desde carpetas locales — no hay que subir nada.

**Opción A — disponible en todos tus proyectos:**
```bash
git clone https://github.com/alvarobf77/skills4all.git
cp -r skills4all/lut-cinematico ~/.claude/skills/
```

**Opción B — solo para un proyecto/repo específico** (se versiona junto con el código):
```bash
cd tu-proyecto
mkdir -p .claude/skills
cp -r ../skills4all/lut-cinematico .claude/skills/
git add .claude/skills/lut-cinematico
git commit -m "Add lut-cinematico skill"
```

En ambos casos, Claude Code la detecta automáticamente al iniciar sesión — solo pide
"hazme un LUT pastel para YouTube" y se activa sola. Funciona igual en la terminal, en la
extensión de VSCode/JetBrains, o en la app de escritorio de Claude Code.

---

## 3. Otros IDEs (Cursor, Windsurf, Antigravity, Copilot, etc.)

**Aclaración importante:** el formato "Skill" (`SKILL.md` + frontmatter YAML) es específico
de Anthropic/Claude — no es un estándar que otros IDEs lean de forma nativa. Antigravity (de
Google) y otros asistentes con su propio sistema de agentes no van a interpretar este
`SKILL.md` automáticamente solo por tenerlo en el repo.

Lo que sí funciona en la práctica en cualquier IDE con un asistente de IA integrado:

1. Abre `lut-cinematico/SKILL.md` y `lut-cinematico/scripts/*.py` de este repo.
2. Copia y pega el contenido completo (instrucciones + scripts) directo en el chat del
   asistente, con un mensaje tipo:
   > "Usa estas instrucciones como referencia para generar LUTs pastel/cinematográficos
   > cuando te lo pida: [pega aquí el contenido de SKILL.md]"
3. El asistente no la "recordará" entre sesiones como sí hace Claude con una skill instalada
   — hay que volver a pegarla cada conversación nueva, salvo que el IDE tenga su propio
   sistema de reglas/contexto persistente (ej. `.cursorrules`, `.windsurfrules`), en cuyo
   caso puedes pegar el contenido de `SKILL.md` ahí.

Si tu equipo usa mayormente Claude Code o Claude.ai, las opciones 1 y 2 son las que dan la
experiencia completa (activación automática, sin copiar/pegar cada vez).
