import pygame
from Units import Swordman, Evilenemy, Unit, MovingCell, Evilwithard, longBow


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 50
        self.U_x, self.U_y = 0, 0

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

    def change(self, pos_x, pos_y, obj):
        self.board[pos_y][pos_x] = obj

    def get_cell(self, mounse_pos):
        x, y = mounse_pos
        x = (x - self.left) // self.cell_size
        y = (y - self.top) // self.cell_size
        if 0 <= x <= self.width - 1 and 0 <= y <= self.height - 1:
            return x, y
        else:
            return False

    def get_click(self, mouse_pos, go):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell, go)

    def on_click(self, coords, go):
        if coords:
            y, x = coords
            if isinstance(self.board[x][y], Unit) and not go:
                self.clean_cell()
                """self.U_x, self.U_y - переменные обозначающие с каким юнитом работают"""
                if isinstance(self.board[self.U_x][self.U_y], Unit):
                    self.board[self.U_x][self.U_y].choose(False)
                self.U_x, self.U_y = x, y
                self.board[x][y].choose(True)
                self.board[x][y].moving(self.board, y, x)
            elif isinstance(self.board[x][y], Unit) and go and (x != self.U_x or y != self.U_y):
                self.clean_cell()
                """self.U_x, self.U_y - переменные обозначающие с каким юнитом работают"""
                if isinstance(self.board[self.U_x][self.U_y], Unit):
                    self.board[self.U_x][self.U_y].choose(False)
                    self.clean_cell()
                self.board[self.U_x][self.U_y].atack(self.board[x][y])
            elif isinstance(self.board[x][y], MovingCell) and go:
                self.board[x][y].change_position(self.board, x, y, self.U_x, self.U_y)
                self.clean_cell()
            else:
                if isinstance(self.board[self.U_x][self.U_y], Unit) and (x != self.U_x or y != self.U_y):
                    self.board[self.U_x][self.U_y].choose(False)


    def clean_cell(self):
        """очищаем поле от клеток на которые может ходить другой юнит"""
        for x in range(self.height):
            for y in range(self.width):
                if isinstance(self.board[x][y], MovingCell):
                    self.board[x][y] = 0


if __name__ == '__main__':
    pygame.init()
    size = width, height = 50 * 30, (50 * 12) + 200
    bg = pygame.image.load('data/battle_fon.png')
    prepared_bg = pygame.transform.scale(bg, (width, height))
    screen = pygame.display.set_mode(size)
    board = Board(30, 12)
    board.set_view(0, 200, 50)
    swordman, evilswordman = Swordman(), Evilenemy()
    board.change(5, 5, swordman)
    board.change(6, 5, evilswordman)
    running = True
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
    pygame.quit()