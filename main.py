import pygame
from Units import Swordman, Evilenemy, Unit, MovingCell, Evilwithard, LongBow
from bot import Intelligence
from welcome import start_screen


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.turn = 1
        self.cell_size = 50
        self.used_units = []
        self.enamy_turn_button_image = pygame.image.load('data/enamy_turn.png').convert()
        self.player_turn_button_image = pygame.image.load('data/player_turn.png').convert()
        self.U_x, self.U_y = -1, 0

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for q in range(self.height):
                x = self.left + self.cell_size * i
                y = self.top + self.cell_size * q
                pygame.draw.rect(screen, (255, 255, 255),
                                 ((x, y), (self.cell_size, self.cell_size)), width=1)
                if self.board[q][i] != 0:
                    self.board[q][i].show(screen, q, i)
                if self.turn == 1:
                    screen.blit(self.player_turn_button_image, (650, 0))
                else:
                    screen.blit(self.enamy_turn_button_image, (650, 0))

    def change(self, pos_x, pos_y, obj):
        self.board[pos_y][pos_x] = obj

    def get_cell(self, mounse_pos):
        x, y = mounse_pos
        x = (x - self.left) // self.cell_size
        y = (y - self.top) // self.cell_size
        if 0 <= x <= self.width - 1 and 0 <= y <= self.height - 1:
            return x, y, True
        else:
            return mounse_pos, False

    def get_click(self, mouse_pos, go):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell, go)

    def on_click(self, coords, go):
        if coords[-1]:
            y, x = coords[:2]
            if isinstance(self.board[x][y], Unit):
                self.clean_cell()
                """проверка нужна, чтобы при переключениии между юнитами спарйты с информацией 
                не накладывалиь друг на друга"""
                if self.U_x != -1:
                    if isinstance(self.board[self.U_x][self.U_y], Unit):
                        self.delete_info(self.board[self.U_x][self.U_y])
                if not go:
                    """выбрать юнита, вывод информации о нём"""
                    """self.U_x, self.U_y - переменные обозначающие с каким юнитом работают"""
                    self.U_x, self.U_y = x, y
                    """вывод информации о юните"""
                    self.board[x][y].choose(True)
                    if self.board[x][y].get_side() == self.turn:
                        self.board[x][y].moving(self.board, y, x)
                if self.board[self.U_x][self.U_y].get_side() == self.turn:
                    if go and (x != self.U_x or y != self.U_y):
                        """в условии начинается обработка атаки"""
                        """записать то, что юнита использовали"""
                        self.movement(self.board[self.U_x][self.U_y])
                        self.board[x][y].coords(x, y)
                        self.board[x][y].get_board(self.board)
                        """если унит убил другого унита то в self.board[self.U_x][self.U_y] = 0"""
                        if isinstance(self.board[self.U_x][self.U_y], Unit):
                            self.board[self.U_x][self.U_y].get_board(self.board)
                            self.board[self.U_x][self.U_y].coords(self.U_x, self.U_y)
                            self.board[self.U_x][self.U_y].atack(self.board[x][y])
                        self.check_winner()
                """перемещение юнита"""
            elif isinstance(self.board[x][y], MovingCell) and go:
                if self.board[self.U_x][self.U_y].get_side() == self.turn:
                    self.movement(self.board[self.U_x][self.U_y])
                    self.board[x][y].change_position(self.board, x, y, self.U_x, self.U_y, self.board[self.U_x][self.U_y])
                    if isinstance(self.board[x][y], Unit):
                        self.delete_info(self.board[x][y])
                    self.U_x, self.U_y = x, y
                self.clean_cell()
            else:
                if isinstance(self.board[self.U_x][self.U_y], Unit) and (x != self.U_x or y != self.U_y):
                    self.delete_info(self.board[self.U_x][self.U_y])
                self.clean_cell()
        else:
            x, y = coords[0]
            if y <= 200 and x >= 650 and x <= 849:
                self.turns()

    def check_winner(self):
        if not any([unit.amount for unit in enamy_list]):
            print('protivnik umer')
        if not any([unit.amount for unit in player_list]):
            print('igrok umer')


    def delete_info(self, other):
        other.choose(False)

    def movement(self, other):
        self.used_units.append(other)

    def turns(self):
        self.clean_cell()
        if isinstance(self.board[self.U_x][self.U_y], Unit):
            self.delete_info(self.board[self.U_x][self.U_y])
        for unit in self.used_units:
            unit.refresh()
        self.used_units.clear()
        if self.turn == 1:
            Galtran.get_situation(self.board)
            self.turn = 0
        else:
            self.turn = 1

    def clean_cell(self):
        """очищаем поле от клеток на которые может ходить другой юнит"""
        for x in range(self.height):
            for y in range(self.width):
                if isinstance(self.board[x][y], MovingCell):
                    self.board[x][y] = 0


if __name__ == '__main__':
    pygame.init()
    size = width, height = 50 * 30, (50 * 12) + 200
    print(size)
    bg = pygame.image.load('data/battle_fon.png')
    prepared_bg = pygame.transform.scale(bg, (width, height))
    screen = pygame.display.set_mode(size)
    board = Board(30, 12)
    board.set_view(0, 200, 50)
    """временно создаём юинитов здесь"""
    swordman = Swordman(50)
    longbowman = LongBow(75)
    player_list = [swordman, longbowman, Swordman(50)]
    enamy_list = [Evilenemy(), Evilenemy(), Evilenemy(), Evilenemy()]
    for p_unit in range(len(player_list)):
        board.change(0, p_unit * 2, player_list[p_unit])
    for e_unit in range(len(enamy_list)):
        board.change(-1, e_unit * 2, enamy_list[e_unit])
    running = True
    """Галтран - имя полководца противника"""
    Galtran = Intelligence(board)
    FPS = 60
    clock = pygame.time.Clock()
    start_screen(screen,FPS)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    """0 - выбор юнита, 1 - ход юнитом"""
                    board.get_click(event.pos, 0)
                if event.button == 3:
                    board.get_click(event.pos, 1)
        screen.blit(prepared_bg, (0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
