import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.start_speed = 200
        self.start_health = 100
        self.health = self.start_health
        self.max_health = self.start_health

        self.image = pygame.image.load('graphics/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
