# Geometry Dash em Pygame

Versão simplificada inspirada no Geometry Dash, criada em Python e
Pygame como mostrado no vídeo. O cubo pula e gira no ar, a fase é
escrita como texto e anda no ritmo da música: cada obstáculo chega numa
batida.

## Como executar

Tenha o Python instalado. Na pasta do repositório, execute:

```bash
python -m pip install -r requirements.txt
python geometry_dash.py
```

No Windows, se o comando `python` não funcionar, use `py` no lugar dele.

Pressione **espaço** para pular. Ao encostar num espinho ou bater de
frente num bloco, o cubo explode e a música para. Um segundo depois, a
fase e a música recomeçam do início. Feche a janela para sair.

## A música

O `musica.mp3` é uma trilha própria de 124 batidas por minuto, feita
para este jogo. Para usar outra música, troque o arquivo e ajuste o
`BPM` no código para o ritmo dela.

## Código passo a passo

O arquivo `geometry_dash.py` contém o jogo completo. A pasta `passos/`
mostra as quatro versões executáveis apresentadas no vídeo: cubo e chão,
pulo, fase e morte. Rode cada uma a partir da pasta do repositório (por
exemplo, `python passos/3-fase.py`), para o jogo encontrar o
`musica.mp3`.

Na fase, cada caractere é uma coluna de 40 pixels: `.` é vazio, `^` é
um espinho e `1`, `2` ou `3` é uma coluna de blocos com essa altura.

## Aprenda Python do zero

Quer aprender Python do zero? Conheça o [curso completo de Python](https://academify.com.br/#github-pygame-geometry-dash).
