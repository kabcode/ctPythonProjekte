import pygame, sys, katzensolo

F_BREITE, F_HOEHE = 1000, 600

pygame.init()
fenster = pygame.display.set_mode((F_BREITE, F_HOEHE))
sprites = pygame.sprite.Group()
katze = katzensolo.Katze(F_BREITE, F_HOEHE)
sprites.add(katze)
uhr = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    fenster.fill((0, 100, 50))
    sprites.update()
    sprites.draw(fenster)

    pygame.display.flip()
    uhr.tick(30)