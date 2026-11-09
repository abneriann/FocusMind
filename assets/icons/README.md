# Ícones do FocusMind

Pack de **35 símbolos** em **59 variações SVG**, agrupados em módulos, navegação, ações, status e conquistas.

| Pasta | Ícones |
| --- | --- |
| `svg/modulos/` | FocusLearn, FocusMove, FocusLevel e FocusTeams |
| `svg/navegacao/` | Menus e navegação, versões laranja e creme |
| `svg/acoes/` | Botões e ações, versões laranja e creme |
| `svg/status/` | Indicadores de estado, versões laranja e creme |
| `svg/badges/` | Conquistas, medalhas e progresso |

**Cores:** laranja `#FF702B`, creme `#FFF7ED`, preto `#09080B`.

### Uso no React

Coloque os SVGs dentro de `public/icons/` ou ajuste o caminho conforme seu bundler:

```jsx
<img src="/icons/modulos/focuslearn.svg" alt="FocusLearn" width="48" height="48" />
```

### PNG

As versões PNG transparentes podem ser geradas a partir destes SVGs usando o script `scripts/generate_icon_pngs.py` (requer Python e `cairosvg`). Os arquivos são organizados automaticamente em `assets/icons/png/`, preservando as categorias do pack.

```bash
python -m pip install cairosvg
python scripts/generate_icon_pngs.py
```

### Identidade visual

Estes são ícones de interface e **não substituem a logo original do FocusMind**. Não alterar ou recriar a marca aprovada.

**Desenvolvedores:** Abner Alencar e Marcelo Sanches.
