import pygame
from random import randint
from player import main_Player, Enamy
from battle_file import start_battler
from Units import Swordman, Evilenemy, Unit, MovingCell, Evilwithard, LongBow
from welcome import start_screen
from resourses import Forest, Lawn, Mine


class big_map:
    def __init__(self, width, height):
        self.show_res_info = False, 0, 0
        self.xl, self.yl = -1, -1
        self.x_move, self.y_move = 0, 0
        self.width = width
        self.height = height
        self.cell_size = 50
        self.map = [[randint(1, 100) for q in range(width)] for _ in range(height)]
        self.create_resourses()
        self.bread_im = pygame.image.load('data/bread.png')
        self.iron_im = pygame.image.load('data/iron.png')
        self.wood_im = pygame.image.load('data/wood.png')
        self.resourses_ims = self.bread_im, self.wood_im, self.iron_im
        self.lawn = pygame.image.load('data/lawn.png').convert()
        self.forest = pygame.image.load('data/forest.png').convert()
        self.mine = pygame.image.load('data/mine.png').convert()

    def set_view(self, left, top, cell_size):
        self.x_move, self.y_move = left, top
        self.cell_size = cell_size

    def create_resourses(self):
        for i in range(self.width):
            for q in range(self.height):
                chance = self.map[q][i]
                if chance <= 55:
                    #равнина
                    self.map[q][i] = Lawn()
                elif 55 <= chance <= 93:
                    #лес
                    self.map[q][i] = Forest()
                elif 93 <= chance <= 100:
                    #шахты
                    self.map[q][i] = Mine()

    def render(self, screen):
        for i in range(self.width):
            for q in range(self.height):
                x = self.cell_size * i + self.x_move
                y = self.cell_size * q + self.y_move
                self.map[q][i].show(screen, x, y)
        if self.show_res_info:
            x, y = self.show_res_info[1:3]
            self.map[x][y].show_dialog(screen, size)

    def biutiful_arnament(self, screen, size):
        font = pygame.font.SysFont('cambria', 22)
        player_resourses = player.get_resourses()
        x, y = size
        pygame.draw.rect(screen, ('#b4b4b4'), ((0, y - 30), (x - 200, 30)))
        turn_image = pygame.image.load('data/player_turn.png')
        screen.blit(turn_image, (x - 200, y - 200))
        for i in range(3):
            resourses_info = font.render(str(player_resourses[i]), 1, (0, 0, 0))
            screen.blit(self.resourses_ims[i], (i * 200 + 200, y - 30))
            screen.blit(resourses_info, (i * 200 + 230, y - 30))
        pygame.draw.rect(screen, ('#b4b4b4'), ((x - 240, 0), (240, 200)))
        for i in range(self.width):
            for q in range(self.height):
                x_mini = i + x - (240 - 5 * i)
                y_mini = q * 5
                player_mini_x = (player.rect.x - self.x_move) / 50
                player_mini_y = (player.rect.y - self.y_move) / 50
                if player_mini_x == i and player_mini_y == q:
                    pygame.draw.rect(screen, ('#0000FF'), ((x_mini, y_mini), (5, 5)))
                else:
                    self.map[q][i].show_mini(screen, x_mini, y_mini)


    def camera_move(self, xm, ym):
        self.x_move += xm
        self.y_move += ym

    def move(self, y, x):
        y_pos = player.rect.y + y * 50
        x_pos = player.rect.x + x * 50
        """if x_pos == enamy.rect.x and y_pos == enamy.rect.y:
            swordman = Swordman(50)
            longbowman = LongBow(75)
            player_list = [swordman, longbowman, Swordman(50)]
            enamy_list = [Evilenemy(), Evilenemy(), Evilenemy(), Evilenemy()]
            start_battler(screen, player_list, enamy_list, size)"""
        if x_pos - self.x_move <= -50 or y_pos - self.y_move <= -50:
            return False
        elif x_pos + self.x_move * -1 >= self.width * 50 or y_pos + self.y_move * -1 >= self.height * 50:
            return False
        else:
            return True

    def use_resourses(self, p, buy=0, x_m=None, y_m=None):
        y = (player.rect.x - self.x_move) // 50
        x = (player.rect.y - self.y_move) // 50
        self.show_res_info = True, x, y
        if p:
            if buy:
                wight, leght = size
                if x_m >= wight - 200:
                    if 215 <= y_m <= 275:
                        self.map[x][y].start_work(player)
                    if 300 <= y_m <= 350:
                        self.map[x][y].build_barrakes(player)
            else:
                self.map[x][y].show_info()
                self.xl, self.yl = x, y
        else:
            self.map[self.xl][self.yl].hide_info()

    def new_turn(self):
        player.get_profit()

    def get_mouse(self, mouse):
        """чтобы распределять функции"""
        wight, leght = size
        x, y = mouse
        if x >= wight - 200 and y >= leght - 200:
            self.new_turn()
        else:
            map.use_resourses(1, 1, x, y)

def drow_space(screen):
    screen.fill('#000000')
    if not stars:
        for i in range(400):
            x, y = randint(0, 1500), randint(0, 800)
            stars.append((x, y))
    for x, y in stars:
        pygame.draw.rect(screen, ('#FFFFFF'), ((x, y), (2, 2)))


stars = []
if __name__ == '__main__':
    pygame.init()
    size = width, height = 50 * 30, (50 * 12) + 200
    screen = pygame.display.set_mode(size)
    map = big_map(40, 40)
    map.set_view(width // 2, height // 2, 50)
    running = True
    player = main_Player(size)
    start_screen(screen, 60, size)
    while running:
        drow_space(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    map.get_mouse(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if map.move(0, -1):
                        map.camera_move(50, 0)
                        map.use_resourses(0)
                if event.key == pygame.K_d:
                    if map.move(0, 1):
                        map.camera_move(-50, 0)
                        map.use_resourses(0)
                if event.key == pygame.K_w:
                    if map.move(-1, 0):
                        map.camera_move(0, 50)
                        map.use_resourses(0)
                if event.key == pygame.K_s:
                    if map.move(1, 0):
                        map.camera_move(0, -50)
                        map.use_resourses(0)
                if event.key == pygame.K_ESCAPE:
                    start_screen(screen, 60, size)
                if event.key == pygame.K_e:
                    map.use_resourses(1)
        map.render(screen)
        player.show(screen)
        map.biutiful_arnament(screen, size)
        pygame.display.flip()
    pygame.quit()

