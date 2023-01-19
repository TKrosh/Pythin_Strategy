import pygame
from battle_file import start_battler, Board
from bot import Intelligence
from Units import Swordman, Evilenemy, Unit, MovingCell, Evilwithard, LongBow
from random import randint
from player import main_Player

class big_map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cell_size = 50
        self.map = [[randint(1, 2) for q in range(width)] for _ in range(height)]
        """НЕ ЗАБЫТЬ ИСПРАВИТЬ И УБРАТЬ ОТСЯДА ГЕРОЯ"""
        self.lawn = pygame.image.load('data/lawn.png').convert()
        self.forest = pygame.image.load('data/forest.png').convert()

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for q in range(self.height):
                x = self.cell_size * i
                y = self.cell_size * q
                pygame.draw.rect(screen, (255, 255, 255),
                                 ((x, y), (self.cell_size, self.cell_size)), width=1)
                if self.map[q][i] == 1:
                    screen.blit(self.lawn, (x, y))
                elif self.map[q][i] == 2:
                    screen.blit(self.forest, (x, y))

if __name__ == '__main__':
    pygame.init()
    size = width, height = 50 * 30, (50 * 12) + 200
    screen = pygame.display.set_mode(size)
    map = big_map(30, 20)
    map.set_view(0, 0, 50)
    running = True
    player = main_Player()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        map.render(screen)
        player.show(screen, 10, 10)
        pygame.display.flip()
    pygame.quit()

    """временно создаём юинитов здесь
    swordman = Swordman(50)
    longbowman = LongBow(75)
    player_list = [swordman, longbowman, Swordman(50)]
    enamy_list = [Evilenemy(), Evilenemy(), Evilenemy(), Evilenemy()]
    start_battler(screen, player_list, enamy_list, size)"""

