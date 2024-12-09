import pygame

pygame.init()
windows = pygame.display.set_mode(size=(1024, 768))

while True:

    # todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # fechar janela
            quit()
