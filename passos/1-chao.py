import pygame

pygame.init()
tela = pygame.display.set_mode((600, 400))
relogio = pygame.time.Clock()

BPM = 124
BATIDA = 60000 / BPM
VEL = 5 * 40 / BATIDA
CHAO, X = 320, 180

cubo = pygame.Surface((40, 40), pygame.SRCALPHA)
cubo.fill("black")
cubo.fill("#5aff78", (3, 3, 34, 34))
cubo.fill("black", (10, 10, 20, 20))
cubo.fill("#00e6ff", (14, 15, 4, 7))
cubo.fill("#00e6ff", (22, 15, 4, 7))

y = CHAO - 40

pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play(-1)
inicio = pygame.time.get_ticks()

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    agora = pygame.time.get_ticks()
    tempo = agora - inicio
    rolagem = tempo * VEL

    batida = 1 - tempo % BATIDA / BATIDA
    luz = int(70 * batida ** 3)
    tela.fill((40 + luz // 2, 30 + luz // 3, 130 + luz))
    for i in range(5):
        bx = (i * 160 - rolagem / 4) % 800 - 100
        cor = (70 + luz, 60 + luz, 170 + luz)
        quadrado = (bx, 30 + i % 3 * 80, 100, 100)
        pygame.draw.rect(tela, cor, quadrado, 4)

    tela.fill((14, 12, 50), (0, CHAO, 600, 80))
    for i in range(9):
        gx = i * 80 - rolagem % 80
        pygame.draw.line(tela, (50, 45, 120), (gx, CHAO),
                         (gx, 400), 3)
    tela.fill("#00e6ff", (0, CHAO - 1, 600, 3))

    tela.blit(cubo, (X, y))

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
