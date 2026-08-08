# corebox

Dotfiles minimalista para Debian (netinstall), montado em cima do i3. O ponto central é performance: cada peça do stack foi escolhida por ser leve, rápida de iniciar e ter baixo consumo em idle — sem ambiente de desktop completo (GNOME/KDE/XFCE), sem compositor pesado, sem daemon rodando à toa em background.

## Pré-requisito

Debian instalado via netinstall **sem** marcar nenhum "desktop environment" no tasksel — ou seja, um sistema só com base + utilitários de linha de comando. O corebox constrói o ambiente gráfico inteiro a partir daí: servidor X, janelas, barra, terminal, áudio.

## Como está organizado

Cada pasta é um módulo independente com seu próprio script `.sh`, chamado em sequência pelo `install.sh`:

| pasta | cuida de |
|---|---|
| `packages/` | utilitários de base do sistema |
| `display/` | servidor X + i3 — o coração do corebox (guia próprio em `display/display-guide.md`) |
| `polybar/` | barra de status |
| `sound/` | controle de áudio |
| `terminal/` | emulador de terminal |

## packages/ — base do sistema

`thunar` · `rofi` · `curl` · `wget` · `fastfetch` · `network-manager` · `firefox-esr`

- **thunar** — gerenciador de arquivos do XFCE. Dá pra instalar avulso, sem herdar a árvore de dependências de um DE inteiro — bem mais leve que Nautilus (GNOME) ou Dolphin (KDE).
- **rofi** — launcher de aplicativos, substituto do dmenu. Praticamente sem overhead, é o que abre no `$mod+d` da sua config do i3.
- **curl / wget** — clientes HTTP de linha de comando. Base pra baixar qualquer coisa que não vem pelo apt (por exemplo, a fonte mencionada no fim deste guia).
- **fastfetch** — mostra as specs do sistema no terminal, no estilo neofetch/screenfetch, mas escrito em C. O neofetch original está sem manutenção há um tempo; fastfetch é o sucessor direto e roda quase instantâneo.
- **network-manager** — o daemon (`NetworkManager`) e as ferramentas de linha de comando (`nmcli` / `nmtui`) pra gerenciar conexão. Importante: esse pacote **não** traz o `nm-applet` (o ícone de rede pra bandeja) — isso é o pacote `network-manager-gnome`, separado.
- **firefox-esr** — o Firefox que o Debian distribui por padrão no repositório estável. ESR (Extended Support Release) significa menos mudança de funcionalidade e foco em correção de segurança, alinhado com o ritmo mais devagar do Debian — você não fica levando atualização grande toda hora.

## polybar/ — barra de status

`polybar`

Barra modular: cada informação (workspace do i3, relógio, volume, bateria) é um "module" configurado num `.ini` separado. Escolhida no lugar da i3bar nativa porque é mais fácil de estilizar (transparência, cantos arredondados, ícones) sem abrir mão de leveza — continua sendo só um binário compilado, sem framework de UI por trás. Quem sobe ela é o `polybar/launch.sh`, chamado pela própria config do i3 via `exec_always` — o polybar não roda sozinho, ele depende do i3 já estar de pé.

## sound/ — áudio

`pulseaudio` · `pavucontrol` · `pamixer`

`pulseaudio` é o servidor de áudio em si — a peça que realmente gerencia os streams de som e conversa com a placa de som/ALSA por baixo. É ele que a linha `exec --no-startup-id pulseaudio --start` da sua config do i3 sobe; sem essa peça, `pavucontrol` e `pamixer` não têm nada pra controlar. `pavucontrol` e `pamixer` são só os controles em cima dele — o controle remoto, não a TV: `pavucontrol` é o mixer gráfico (volume por aplicativo, trocar saída de áudio), `pamixer` é o equivalente em linha de comando, usado nos atalhos `$mod+F6/F7/F8` da sua config do i3. (A alternativa mais atual seria `pipewire` + `pipewire-pulse`, que é o padrão em boa parte do Debian hoje, mas `pulseaudio` continua leve o suficiente pra esse uso e é mais direto de configurar sozinho.)

## terminal/ — emulador de terminal

`kitty`

Terminal com renderização acelerada por GPU (OpenGL), em vez de desenhar cada caractere na CPU como emuladores mais antigos (xterm, por exemplo). Na prática, scroll e redraw bem mais rápidos com muito texto na tela. É o terminal atrelado ao `$mod+Return` na config do i3, e o único terminal do setup.


