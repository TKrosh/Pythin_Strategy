import pygame


class main_Player:
    def __init__(self):
        self.hourse_image = pygame.image.load('data/player.png')

    def show(self, screen, pos_x, pos_y):
        screen.blit(self.hourse_image, (pos_y * 50, pos_x * 50))