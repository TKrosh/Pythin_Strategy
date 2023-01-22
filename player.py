import pygame


class main_Player:
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('data/player.png')
        self.rect = self.image.get_rect().move(
            50 * pos_x, 50 * pos_y)

    def show(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Enamy:
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('data/enamy_tile.png')
        self.rect = self.image.get_rect().move(
            50 * pos_x, 50 * pos_y)

    def show(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))