import pygame
import random


def sing(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return num


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
                         ((x, y), (self.cell_size, self.cell_size)), width=6)

    def get_energy(self):
        return int(self.energy)

    def moving(self, board, y, x):
        pass

    def change_position(self, board, x, y, los_x, loc_y, other):
        other.curent_energy = self.energy
        board[x][y] = board[los_x][loc_y]
        board[los_x][loc_y] = 0


class Unit:
    """основной класс всех юнитов"""
    def __init__(self):
        self.image = pygame.image
        self.health, self.energy = 0, 0
        self.curent_energy, self.damege, self.protection, \
                          self.curent_health, self.distance, self.amount = self.energy, 0, 0, self.health, 1, 1
        self.side = 0
        self.choosen_Unit = False
        self.move = False

    def refresh(self):
        self.curent_energy = self.energy

    def show(self, screen, pos_x, pos_y):
        """показать количество юнитов одного класса"""
        font = pygame.font.SysFont('bahnschrift', 15)
        """выбрать шрифт"""
        bg_font = (170, 191, 255)
        """цвет фона"""
        amount_units = font.render(str(self.amount), bg_font, (0, 0, 0))
        """сохранение текста"""
        y, x = pos_y * 50 + 15, pos_x * 50 + 239
        screen.blit(self.image, (pos_y * 50, pos_x * 50 + 200))
        pygame.draw.rect(screen, bg_font, ((y, x), (26, 10)), width=0)
        screen.blit(amount_units, (y, x - 4))
        if self.choosen_Unit:
            self.showinfo(screen)

    def limit(self, num, lim=30):
        """чтобы ходы не просчитывались по тору"""
        if num < 0:
            return int(0)
        elif num >= lim - 1:
            return int(lim)
        else:
            return int(num)

    def showinfo(self, screen):
        self.parametres = self.curent_health, self.damege, self.curent_energy, \
                          self.protection, self.distance, self.amount
        """вывод информации о юните"""
        infoimage = pygame.image.load('data/unitinfo.png')
        screen.blit(infoimage, (0, 0))
        font = pygame.font.SysFont('cambria', 22)
        for i in range(5):
            amount_units = font.render(str(self.parametres[i]), (0, 0, 0), (0, 0, 0))
            y, x = 180, i * 40 + 10
            screen.blit(amount_units, (y, x))

    def moving(self, board, q, i):
        limy = len(board)
        limx = len(board[0])
        a = board[i][q].get_energy()
        """просчитываем все возможные ходы несколько раз проходя по доске"""
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

    def check_distance(self, other):
        distance = abs(self.x - other.x) + abs(self.y - other.y)
        if self.distance == 1:
            if distance <= self.curent_energy + 1:
                return True
            else:
                return False
        elif self.distance != 1:
            if distance <= self.distance:
                return True
            else:
                return False

    def find_empty_cell(self, other):
        """позиция защищающегося юнита"""
        xt, yt = other.x, other.y
        if yt - 1 >= 0 and not isinstance(self.board[xt][yt - 1], Unit):
            self.board[xt][yt - 1] = self.board[self.x][self.y]
            self.board[self.x][self.y] = 0
        elif xt - 1 >= 0 and not isinstance(self.board[xt - 1][yt], Unit):
            self.board[xt - 1][yt] = self.board[self.x][self.y]
            self.board[self.x][self.y] = 0
        elif xt + 1 < len(self.board) and not isinstance(self.board[xt - 1][yt], Unit):
            self.board[xt + 1][yt] = self.board[self.x][self.y]
            self.board[self.x][self.y] = 0
        elif yt + 1 < len(self.board[0]) and not isinstance(self.board[xt][yt + 1], Unit):
            self.board[xt ][yt + 1] = self.board[self.x][self.y]
            self.board[self.x][self.y] = 0
        else:
            return False

    def atack(self, other):
        if self.check_distance(other) and self.curent_energy != 0:
            self.curent_energy = 0
            """получаем суммарный урон АТАКУЮЩЕГО отряда"""
            if self.side != other.side:
                i = int(self.damege - other.protection)
                damage_koef = (1 + 0.1 * sing(i)) ** abs(i)
                damage = int((self.damege * self.amount * damage_koef) // 1)
                other.get_atacked(damage, self)

    def get_atacked(self, enamy_damage, other):
        remain_units = ((self.health * self.amount) - enamy_damage) / self.health
        if remain_units <= 0:
            self.death(other)
        else:
            if other.distance == 1:
                other.find_empty_cell(self)
            if remain_units % 1 != 0:
                remain_units = int(remain_units // 1)
                self.curent_health = self.curent_health - (enamy_damage % self.health)
                if self.curent_health <= 0:
                    remain_units -= 1
                    self.curent_health = self.health + self.curent_health
            remain_units = int(remain_units // 1)
            self.amount -= (self.amount - remain_units)

    def death(self, other):
        self.amount = 0
        self.board[self.x][self.y] = 0
        if other.distance == 1:
            self.board[self.x][self.y] = self.board[other.x][other.y]
            self.board[other.x][other.y] = 0


    """все костыли в одном месте =)"""
    def coords(self, x, y):
        self.x, self.y = x, y

    def choose(self, show):
        self.choosen_Unit = show

    def get_energy(self):
        return int(self.curent_energy)

    def get_side(self):
        return self.side

    def get_board(self, board):
        self.board = board


class Swordman(Unit):
    def __init__(self, amount):
        super().__init__()
        self.image = pygame.image.load('data/brave_sword.png')
        self.x, self.y = 0, 0
        self.side = 1
        self.health, self.energy = 20, 9
        self.curent_health, self.damege, self.curent_energy, \
                          self.protection, self.distance, self.amount = self.health, 6, self.energy, 8, 1, 123


class LongBow(Unit):
    def __init__(self, amount):
        super().__init__()
        self.side = 1
        self.image = pygame.image.load('data/longbow.png')
        self.health, self.energy = 12, 6
        self.curent_health, self.damege, self.curent_energy, \
                          self.protection, self.distance, self.amount = self.health, 8, self.energy, 4, 12, 55


class Evilenemy(Unit):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/evil_sword.png')
        self.health, self.energy = 21, 10
        self.parametres = self.curent_health, self.damege, self.curent_energy, \
                          self.protection, self.distance, self.amount = self.health, 7, self.energy, 8, 1, 75
        self.target_points = (-1, -1)


class Evilwithard(Unit):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/evil_withard.png')
        self.health, self.energy = 10, 7
        self.curent_health, self.damege, self.curent_energy, \
                self.protection, self.distance, self.amount = self.health, 12, 4, 0, 15, 25
        self.target_points = (-1, -1)

