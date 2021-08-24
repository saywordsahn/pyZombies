import pygame

pygame.init()

screen_width = 1920
screen_height = 1280

screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit(0)
