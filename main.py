import pygame
from Units import Swordman, Evilenemy


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 50

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

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def on_click(self, coords):
        if coords:
            y, x = coords
            if self.board[x][y] != 0:
                self.board[x][y].moving(self.board, y, x)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 50 * 30, (50 * 12) + 200
    bg = pygame.image.load('data/battle_fon.png')
    prepared_bg = pygame.transform.scale(bg, (width, height))
    screen = pygame.display.set_mode(size)
    board = Board(30, 12)
    board.set_view(0, 200, 50)
    player_army, evil_army = Swordman(), Evilenemy()
    board.change(5, 5, player_army)
    board.change(-1, 0, evil_army)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.blit(prepared_bg, (0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()