import pygame
from random import randint
from player import main_Player, Enamy
from battle_file import start_battler
from Units import Swordman, Evilenemy, Unit, MovingCell, Evilwithard, LongBow
from welcome import start_screen


class resourses:
    def __init__(self):
        pass


class big_map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cell_size = 50
        self.map = [[randint(1, 100) for q in range(width)] for _ in range(height)]
        self.lawn = pygame.image.load('data/lawn.png').convert()
        self.forest = pygame.image.load('data/forest.png').convert()
        self.mine = pygame.image.load('data/mine.png').convert()

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for q in range(self.height):
                x = self.cell_size * i + self.left
                y = self.cell_size * q + self.top
                chance = self.map[q][i]
                if chance <= 55:
                    #равнина
                    screen.blit(self.lawn, (x, y))
                elif 55 <= chance <= 93:
                    #лес
                    screen.blit(self.forest, (x, y))
                elif 93 <= chance <= 100:
                    #шахты
                    screen.blit(self.mine, (x, y))

def atack(y, x):
    y_pos = player.rect.y + y * 50
    x_pos = player.rect.x + x * 50
    if x_pos == enamy.rect.x and y_pos == enamy.rect.y:
        swordman = Swordman(50)
        longbowman = LongBow(75)
        player_list = [swordman, longbowman, Swordman(50)]
        enamy_list = [Evilenemy(), Evilenemy(), Evilenemy(), Evilenemy()]
        start_battler(screen, player_list, enamy_list, size)
    else:
        return True


if __name__ == '__main__':
    pygame.init()
    size = width, height = 50 * 31, (50 * 30)
    screen = pygame.display.set_mode(size)
    map = big_map(30, 20)
    map.set_view(0, 0, 50)
    running = True
    player = main_Player(5, 5)
    enamy = Enamy(6, 5)
    start_screen(screen, 60, size)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if atack(0, -1):
                        player.rect.x -= 50
                if event.key == pygame.K_RIGHT:
                    if atack(0, 1):
                        player.rect.x += 50
                if event.key == pygame.K_UP:
                    if atack(-1, 0):
                        player.rect.y -= 50
                if event.key == pygame.K_DOWN:
                    if atack(1, 0):
                        player.rect.y += 50
                if event.key == pygame.K_ESCAPE:
                    start_screen(screen, 60, size)
        map.render(screen)
        player.show(screen)
        enamy.show(screen)
        pygame.display.flip()
    pygame.quit()

