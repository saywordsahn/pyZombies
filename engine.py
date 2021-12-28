import pygame
from player import Player


class Engine:

    def __init__(self):
        pygame.init()

        self.SCREEN_WIDTH = 1920
        self.SCREEN_HEIGHT = 1080
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN)

        self.player = Player(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.FPS)
        self.player.spawn(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)


    def run(self):

        while True:

            time = pygame.time.get_ticks()

            # Input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit(0)

            # Update
            self.player.update(pygame.key.get_pressed())

            # Draw
            self.screen.fill(pygame.color.Color('Black'))

            self.player_group.draw(self.screen)

            pygame.display.update()

            self.clock.tick(self.FPS)

