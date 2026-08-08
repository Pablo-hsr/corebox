# display — servidor X + i3

O módulo mais importante do corebox: monta o ambiente gráfico inteiro em cima de um Debian sem nenhum desktop environment.

## xorg

O servidor X11 — a camada que fala com a placa de vídeo e com teclado/mouse, e desenha o que aparece na tela. É o que qualquer coisa gráfica no Linux precisa por baixo, a não ser que você use Wayland (outro protocolo, incompatível). O i3 é feito pra X11 e não roda em Wayland; se um dia quiser migrar, o equivalente direto lá é o `sway` — mesma sintaxe de config, praticamente um drop-in.

## xinit

O pacote que dá o comando `startx`. Serve pra subir uma sessão X manualmente a partir do terminal (TTY), sem precisar de um *display manager* (GDM, LightDM, SDDM) rodando como daemon esperando você logar numa tela gráfica. Essa é uma escolha deliberada de minimalismo: sem display manager, você loga direto no terminal (TTY) e roda `startx`, que lê o `~/.xinitrc` e sobe o que estiver escrito lá — no caso, `exec i3`. Um processo a menos rodando o tempo todo em background.

## i3-wm

O window manager em si — e o motivo do corebox existir. O que faz diferença pra performance:

- **Tiling, não floating.** As janelas se organizam em grade automaticamente, sem precisar calcular sobreposição/z-index o tempo todo.
- **Sem animação, sem composição por padrão.** Trocar de janela ou workspace é instantâneo, sem efeito de transição consumindo GPU.
- **Controlado por teclado.** Não depende de renderizar barra de título, botões ou sombra em cada janela.
- É um binário C único, orientado a eventos — só "acorda" quando algo muda. Em idle, consumo de CPU é praticamente zero.

É o oposto do que um DE completo (GNOME/KDE) traz ligado por padrão: composição, animações, um daemon de sessão inteiro rodando por trás.

## O arquivo `config`

Os blocos principais da sua config:

- **`set $mod` + binds de foco/mover/resize** — navegação totalmente por teclado (`$mod+j/k/l/;` no lugar das setas, estilo vim).
- **`gaps inner/outer`** — o respiro entre janelas e bordas da tela. Puramente estético, não mexe em performance.
- **10 workspaces numerados** — `$mod+1..0` troca de workspace, `$mod+Shift+1..0` move a janela atual pra lá.
- **modo `resize`** — um "modo" temporário do i3 onde `j/k/l/;`/setas passam a redimensionar a janela em vez de mover o foco; sai com Enter, Esc ou `$mod+r`.
- **bloco `bar {}`** — configura a i3bar *nativa* do i3 (fonte, `mode hide`). Repare que isso existe em paralelo ao polybar: hoje as duas barras estão configuradas ao mesmo tempo. Se o plano é usar só o polybar, dá pra remover esse bloco inteiro.

## A cadeia de `exec` / `exec_always`

São os programas que a própria config do i3 sobe sozinha quando inicia. Nem todos são instalados por algum script hoje — o que ainda falta está marcado:

- **`dex --autostart`** *(ainda não instalado)* — lê os arquivos `.desktop` de autostart, o mesmo mecanismo que GNOME/KDE usam, e roda o que estiver marcado pra iniciar junto com a sessão.
- **`xss-lock` + `i3lock`** *(ainda não instalados)* — `xss-lock` escuta eventos de suspensão/idle do sistema e aciona o `i3lock` (a tela de bloqueio) antes de suspender.
- **`picom`** — o compositor. É o que permite transparência e outros efeitos de composição nas janelas. Usar compositor é a única concessão de performance que o corebox faz em troca de estética — o resto do stack evita esse tipo de camada extra de renderização.
- **`nitrogen`** — define e restaura o wallpaper.
- **`pulseaudio --start`** — inicia o servidor de áudio (módulo `sound/`) pro `pavucontrol`/`pamixer` terem o que controlar de fato.
- **`~/.config/polybar/launch.sh`** — sobe a barra do módulo `polybar/`. É a config do i3 que decide quando o polybar aparece, não o contrário.
