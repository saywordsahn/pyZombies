import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, screen_width, screen_height, fps):
        pygame.sprite.Sprite.__init__(self)
        self.fps = fps
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.start_speed = 200
        self.speed = self.start_speed
        self.start_health = 100
        self.health = self.start_health
        self.max_health = self.start_health

        self.image = pygame.image.load('graphics/player.png')
        self.rect = self.image.get_rect()


    def update(self, keys):
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed / self.fps

        if keys[pygame.K_d] and self.rect.right < self.screen_width:
            self.rect.x += self.speed / self.fps

        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed / self.fps

        if keys[pygame.K_s] and self.rect.bottom < self.screen_height:
            self.rect.y += self.speed / self.fps


    def spawn(self, arena_width, arena_height):
        self.rect.x = arena_width / 2
        self.rect.y = arena_height / 2



