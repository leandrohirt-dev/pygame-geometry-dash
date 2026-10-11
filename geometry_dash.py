import pygame
import random

pygame.init()
tela = pygame.display.set_mode((600, 400))
relogio = pygame.time.Clock()
fonte = pygame.font.Font(None, 46)

BPM = 124
BATIDA = 60000 / BPM
VEL = 5 * 40 / BATIDA
CHAO, X = 320, 180
FASE = (
    ".................^.........^...^^........^^^......"
    "..111111111......^....1222223333..........1111^^11"
    "11....^....^....^^........^^^........^............"
)

cubo = pygame.Surface((40, 40), pygame.SRCALPHA)
cubo.fill("black")
cubo.fill("#5aff78", (3, 3, 34, 34))
cubo.fill("black", (10, 10, 20, 20))
cubo.fill("#00e6ff", (14, 15, 4, 7))
cubo.fill("#00e6ff", (22, 15, 4, 7))

y, vel, angulo = CHAO - 40, 0, 0
no_chao = True
tentativa = 1
morte, volta, pedacos = False, 0, []

pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play(-1)
inicio = pygame.time.get_ticks()

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN and no_chao:
            if evento.key == pygame.K_SPACE:
                vel = -13

    agora = pygame.time.get_ticks()
    if morte and agora >= volta:
        morte, inicio, pedacos = False, agora, []
        y, vel, angulo = CHAO - 40, 0, 0
        pygame.mixer.music.play(-1)
    if not morte:
        tempo = agora - inicio
        rolagem = tempo * VEL
    vel += 0.9
    y += vel
    no_chao = False
    if y >= CHAO - 40:
        y, vel, no_chao = CHAO - 40, 0, True

    batida = 1 - tempo % BATIDA / BATIDA
    luz = int(70 * batida ** 3)
    tela.fill((40 + luz // 2, 30 + luz // 3, 130 + luz))
    for i in range(5):
        bx = (i * 160 - rolagem / 4) % 800 - 100
        cor = (70 + luz, 60 + luz, 170 + luz)
        quadrado = (bx, 30 + i % 3 * 80, 100, 100)
        pygame.draw.rect(tela, cor, quadrado, 4)
    aviso = f"Tentativa {tentativa}"
    texto = fonte.render(aviso, 1, "white")
    tela.blit(texto, (330 - rolagem, 120))

    jogador = pygame.Rect(X, round(y), 40, 40)
    bateu = False
    col = int(rolagem // 40)
    for c in range(col, col + 16):
        letra = FASE[c % len(FASE)]
        x = c * 40 - rolagem
        if letra == "^":
            pontas = [(x, CHAO), (x + 20, CHAO - 40),
                      (x + 40, CHAO)]
            pygame.draw.polygon(tela, "black", pontas)
            pygame.draw.polygon(tela, "white", pontas, 2)
            perigo = (x + 14, CHAO - 24, 12, 24)
            if jogador.colliderect(perigo):
                bateu = True
        elif letra != ".":
            alt = 40 * int(letra)
            bloco = pygame.Rect(x, CHAO - alt, 40, alt)
            pygame.draw.rect(tela, "black", bloco)
            pygame.draw.rect(tela, "white", bloco, 2)
            if jogador.colliderect(bloco):
                if jogador.bottom - vel <= bloco.top + 2:
                    jogador.bottom = bloco.top
                    y, vel, no_chao = jogador.y, 0, True
                else:
                    bateu = True

    if no_chao:
        angulo = round(angulo / 90) * 90
    else:
        angulo -= 6.5

    if bateu and not morte:
        morte, morreu = True, agora
        volta = agora + 1000
        tentativa += 1
        pygame.mixer.music.stop()
        meio = (X + 20, y + 20)
        pedacos = []
        for _ in range(20):
            vx = random.uniform(-7, 7)
            vy = random.uniform(-12, 2)
            pedacos.append([X + 15, y + 15, vx, vy])

    tela.fill((14, 12, 50), (0, CHAO, 600, 80))
    for i in range(9):
        gx = i * 80 - rolagem % 80
        pygame.draw.line(tela, (50, 45, 120), (gx, CHAO),
                         (gx, 400), 3)
    tela.fill("#00e6ff", (0, CHAO - 1, 600, 3))

    if not morte:
        img = pygame.transform.rotate(cubo, angulo)
        centro = img.get_rect(center=(X + 20, y + 20))
        tela.blit(img, centro)
    for p in pedacos:
        p[0] += p[2]
        p[1] += p[3]
        p[3] += 0.6
        tela.fill("#5aff78", (p[0], p[1], 11, 11))
    if morte and agora - morreu < 100:
        pygame.draw.circle(tela, "#fff5c8", meio, 55)

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
