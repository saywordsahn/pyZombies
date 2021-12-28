import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.START_SPEED = 200
        self.START_HEALTH = 100
        self.image = pygame.image.load('graphics/player.png')


