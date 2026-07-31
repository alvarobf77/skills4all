# Skills for All

Colección pública de Skills para Claude, compartidas con la comunidad de Infinitix Group.

Cada carpeta es una skill independiente con su `SKILL.md` (instrucciones que Claude consulta
automáticamente) y, cuando aplica, sus `scripts/` de soporte.

## Estructura de cada skill

Para mantener todo homogéneo y fácil de usar por cualquiera, cada skill de este repo sigue
la misma estructura:

```
nombre-skill/
├── README.md   ← documentación completa: qué hace, cómo funciona, instalación, uso,
│                 opciones, requisitos, licencia (léelo primero)
├── SKILL.md    ← instrucciones que Claude consulta automáticamente al activarse
└── scripts/    ← código de soporte, si aplica
```

## Cómo instalar una skill (rápido)

- **Claude.ai** (web/escritorio/móvil): comprime la carpeta de la skill en `.zip` → perfil →
  **Settings → Capabilities → Skills → + Upload skill**.
- **Claude Code** (terminal, VSCode, JetBrains): `cp -r nombre-skill ~/.claude/skills/` para
  tenerla en todos tus proyectos, o dentro de `.claude/skills/` de un repo específico.
- **Otros IDEs** (Cursor, Windsurf, Antigravity, etc.): no leen el formato `SKILL.md` de
  forma nativa — copia y pega su contenido en el chat del asistente como instrucciones.

Cada skill trae su propio `README.md` con la guía detallada — revísalo si algo no queda
claro.

## Skills disponibles

| Skill | Descripción | Documentación |
|---|---|---|
| [`lut-cinematico`](./lut-cinematico) | Genera LUTs 3D `.cube` con look pastel/cinematográfico limpio para video (YouTube, Premiere, DaVinci, FCPX, OBS). | [README](./lut-cinematico/README.md) |
