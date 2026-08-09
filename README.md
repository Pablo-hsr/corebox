# corebox

Dotfiles minimalista para Debian netinstall, montado em cima do i3 — sem ambiente de desktop, sem processo sobrando, focado 100% em performance.

## Filosofia

- **Minimalismo de verdade** — nada de GNOME/KDE/XFCE completo por trás. Cada peça do stack é escolhida por ser leve e ter baixo consumo em idle.
- **Sem daemon à toa** — sem display manager (GDM/LightDM/SDDM); login direto no TTY com `startx`.
- **Tiling, sem composição por padrão** — i3 puro, sem animação. O único compositor (`picom`) entra por escolha estética consciente, não por padrão de DE.
- **Modular** — cada camada do ambiente (display, pacotes, áudio, terminal, barra) é um script independente.

## Pré-requisito

Debian instalado via **netinstall**, sem marcar nenhum desktop environment no tasksel — um sistema só com base + linha de comando. O corebox monta o resto a partir daí.

## Estrutura

| pasta | cuida de |
|---|---|
| `packages/` | utilitários de base do sistema |
| `display/` | servidor X + i3 |
| `polybar/` | barra de status |
| `sound/` | áudio |
| `terminal/` | emulador de terminal |

## Instalação

```bash
git clone https://github.com/seu-usuario/corebox.git ~/corebox
cd ~/corebox
bash install.sh
```

O `install.sh` roda os módulos em sequência (`display`, `packages`, `polybar`, `sound`, `terminal`) e pede senha de `sudo` durante os `apt install`.

## O que é instalado

| tecnologia | módulo | pra quê |
|---|---|---|
| `xorg`, `xinit`, `i3-wm` | `display/` | servidor gráfico + window manager tiling |
| `polybar` | `polybar/` | barra de status |
| `pulseaudio`, `pavucontrol`, `pamixer` | `sound/` | servidor de áudio + controles |
| `kitty` | `terminal/` | terminal com renderização por GPU |
| `thunar`, `rofi`, `curl`, `wget`, `fastfetch`, `network-manager`, `firefox-esr` | `packages/` | utilitários de base |

Detalhes de cada tecnologia e o porquê da escolha estão em [`corebox-guide.md`](./corebox-guide.md) e, especificamente pra pilha X11+i3, em [`display/display-guide.md`](./display/display-guide.md).

## Atalhos principais

| atalho | ação |
|---|---|
| `$mod+Return` | abrir terminal (kitty) |
| `$mod+d` | abrir launcher (rofi) |
| `$mod+j/k/l/;` | mover foco entre janelas |
| `$mod+1..0` | trocar de workspace |
| `$mod+Shift+1..0` | mover janela atual pro workspace |
| `$mod+F6/F7/F8` | volume: baixar / mutar / subir |

`$mod` é a tecla definida em `set $mod` no `display/config`.

## Status

Funcional no essencial (X + i3 + barra + terminal + áudio). Ainda faltam:

- [ ] `dex` — autostart de `.desktop`
- [ ] `xss-lock` + `i3lock` — bloqueio de tela
- [ ] `network-manager-gnome` — ícone de wifi na bandeja (`nm-applet`)
- [ ] `wpasupplicant` + firmware da placa wireless, se o wifi não aparecer no `nmtui`
- [ ] fonte `JetBrainsMono Nerd Font` — ícones da barra