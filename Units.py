import pygame


class MovingCell:
    """класс Клекти на которые может ходить конкрентый юнит"""
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

    def change_position(self, board, x, y, los_x, loc_y):
        board[x][y] = board[los_x][loc_y]
        board[los_x][loc_y] = 0


class Unit:
    """основной класс всех юнитов"""
    def __init__(self):
        self.image = pygame.image
        self.energy = 0
        self.move = False

    def show(self, screen, pos_x, pos_y):
        screen.blit(self.image, (pos_y * 50, pos_x * 50 + 200))

    def get_energy(self):
        return int(self.energy)

    def limit(self, num, lim=30):
        """чтобы ходы не просчитывались по тору"""
        if num < 0:
            return int(0)
        elif num >= lim - 1:
            return int(lim)
        else:
            return int(num)

    def moving(self, board, q, i):
        limy = len(board)
        limx = len(board[0])
        a = board[i][q].get_energy()
        """просчитываем все возможные ходы несколько раз проходя по доске"""
        print(self.limit(q + a, limx))
        for _ in range(a - 1):
            for x in range(self.limit(i - a - 1), self.limit(i + a, limy)):
                for y in range(self.limit(q - a - 1), self.limit(q + a, limx)):
                    if (board[x][y] != 0 and not isinstance(board[x][y], Unit)) or (x == i and y == q):
                        amount = board[x][y].get_energy()
                        """использыем try, чтобы не делать ещё по 4 проверки на выход за границы поля"""
                        try:
                            """если на месте просчитываемой клетке ничего нет, тогда заменяем значение"""
                            if board[self.limit(x - 1)][y] == 0 and (amount - 1) > 0:
                                board[self.limit(x - 1)][y] = MovingCell(amount - 1)
                            if board[self.limit(x + 1, limx)][y] == 0 and (amount - 1) > 0:
                                board[self.limit(x + 1, limx)][y] = MovingCell(amount - 1)
                            if board[x][self.limit(y - 1)] == 0 and (amount - 1) > 0:
                                board[x][self.limit(y - 1)] = MovingCell(amount - 1)
                            if board[x][self.limit(y + 1)] == 0 and (amount - 1) > 0:
                                board[x][self.limit(y + 1)] = MovingCell(amount - 1)
                        except Exception:
                            pass


class Swordman(Unit):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/brave_sword.png')
        self.energy = 5


class longBow(Unit):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/longbow.png')
        self.energy = 5


class Evilwithard(Unit):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/evil_withard.png')
        self.energy = 8


class Evilenemy(Unit):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/evil_sword.png')
        self.energy = 8

