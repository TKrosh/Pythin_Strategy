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
                         ((x, y), (self.cell_size, self.cell_size)), width=6)

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
        self.parametres = self.energy, self.damege, self.protection, \
                          self.heath, self.distance, self.amount = 0, 0, 0, 0, 1, 1
        self.player_side = 0
        self.choosen_Unit = False
        self.move = False

    def show(self, screen, pos_x, pos_y):
        self.screen = screen
        """показать количество юнитов одного класса"""

        font = pygame.font.SysFont('', 22)
        """выбрать шрифт"""
        bg_font = (170, 191, 255)
        """цвет фона"""
        amount_units = font.render(str(self.amount), bg_font, (0, 0, 0))
        """сохранение текста"""
        y, x = pos_y * 50 + 15, pos_x * 50 + 239
        screen.blit(self.image, (pos_y * 50, pos_x * 50 + 200))
        pygame.draw.rect(screen, bg_font, ((y, x), (26, 10)), width=0)
        screen.blit(amount_units, (y, x))
        if self.choosen_Unit:
            self.showinfo(screen)

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

    def choose(self, show):
        self.choosen_Unit = show

    def showinfo(self, screen):
        infoimage = pygame.image.load('data/unitinfo.png')
        screen.blit(infoimage, (0, 0))
        for i in range(5):
            font = pygame.font.SysFont('', 22)
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

    def atack(self, other):
        """получаетм сумму здоровья и брони всего отряда НА который напали"""
        enamy_summary_HP = other.health * other.amount + other.protection * other.amount
        """получаем суммарный урон АТАКУЮЩЕГО отряда"""
        self_damage = self.damege * self.amount
        enamy_sum_HP_after_fight = enamy_summary_HP - self_damage
        if enamy_sum_HP_after_fight <= 0:
            other.death()
        else:
            """если отряд не убавает сразу, то получаем оставшихся в живых членов отряда 
            + те которые имеют какие-то повреждения"""
            one_unit_parametres = other.health + other.protection
            enamy_amount_after_fight = enamy_sum_HP_after_fight // (one_unit_parametres)
            if enamy_sum_HP_after_fight % one_unit_parametres != 0:
                other.get_atacked(enamy_amount_after_fight + 1)
            else:
                other.get_atacked(enamy_amount_after_fight)

    def get_atacked(self, remain):
        """расчёт оставшихся параметров ХП и брони"""
        self.amount = remain

    def death(self):
        self.amount = 0


class Swordman(Unit):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/brave_sword.png')
        self.parametres = self.health, self.damege, self.energy, \
                          self.protection, self.distance, self.amount = 10, 4, 8, 3, 1, 10


class longBow(Unit):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/longbow.png')
        self.parametres = self.health, self.damege, self.energy, \
                          self.protection, self.distance, self.amount = 5, 8, 0, 10, 12, 1


class Evilwithard(Unit):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/evil_withard.png')
        self.parametres = self.health, self.damege, self.energy, \
                          self.protection, self.distance, self.amount = 5, 12, 0, 7, 7, 1


class Evilenemy(Unit):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/evil_sword.png')
        self.parametres = self.health, self.damege, self.energy, \
                          self.protection, self.distance, self.amount = 10, 4, 8, 3, 1, 10

