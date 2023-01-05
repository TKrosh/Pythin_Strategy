import pygame


class Cell:
    def __init__(self, energy):
        self.height, self.weight = 50, 50
        self.energy = energy
        self.cell_size = 50

    def show(self, screen, q, i):
        x = self.cell_size * i
        y = 200 + self.cell_size * q
        pygame.draw.rect(screen, (255, 255, 255),
                         ((x, y), (self.cell_size, self.cell_size)), width=5)

    def get_energy(self):
        return int(self.energy)

    def moving(self, board, y, x):
        pass


class Unit:
    def __init__(self):
        self.image = pygame.image
        self.energy = 0

    def show(self, screen, pos_x, pos_y):
        screen.blit(self.image, (pos_y * 50, pos_x * 50 + 200))

    def get_energy(self):
        return int(self.energy)

    def limit(self, num, lim=30):
        if num < 0:
            return int(0)
        elif num >= lim:
            return int(lim - 1)
        else:
            return int(num)

    def moving(self, board, q, i):
        limx = len(board)
        limy = len(board[0])
        a = board[i][q].get_energy()
        for _ in range(4):
            for x in range(self.limit(q - a), self.limit(q + a + 1, limx)):
                for y in range(self.limit(i - a), self.limit(i + a + 1, limy)):
                    if board[x][y] != 0:
                        amount = board[x][y].get_energy()
                        try:
                            if board[self.limit(x - 1)][y] == 0 and (amount - 1) > 0:
                                board[self.limit(x - 1)][y] = Cell(amount - 1)
                            if board[self.limit(x + 1, limx)][y] == 0 and (amount - 1) > 0:
                                board[self.limit(x + 1, limx)][y] = Cell(amount - 1)
                            if board[x][self.limit(y - 1)] == 0 and (amount - 1) > 0:
                                board[x][self.limit(y - 1)] = Cell(amount - 1)
                            if board[x][self.limit(y + 1)] == 0 and (amount - 1) > 0:
                                board[x][self.limit(y + 1)] = Cell(amount - 1)
                        except Exception:
                            pass
        for i in range(len(board)):
            for q in range(len(board[i])):
                if board[i][q] != 0:
                    print(board[i][q].get_energy(), end='')
                else:
                    print(0, end='')
            print()


class Swordman(Unit):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/brave_sword.png')
        self.energy = 5


class Evilenemy(Unit):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/evil_sword.png')
        self.energy = 8

