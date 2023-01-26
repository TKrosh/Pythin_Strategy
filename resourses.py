import pygame
from Units import Swordman, Evilenemy, Unit, MovingCell, Evilwithard, LongBow

class Resourses:
    def __init__(self):
        self.isbarak = False
        self.font = pygame.font.SysFont('cambria', 20)
        self.used_res = pygame.image.load('data/wood.png')
        self.return_res = 0
        self.image = pygame.image
        self.info = ''
        self.color = '#000000'
        self.show_d = False
        self.show_warriors = False

    def show(self, screen, x, y):
        screen.blit(self.image, (x, y))

    def show_mini(self, screen, x, y):
        pygame.draw.rect(screen, self.color, ((x, y), (5, 5)))

    def show_info(self):
        if self.show_d:
            self.show_d = False
        else:
            self.show_d = True

    def hide_info(self):
        self.show_d = False

    def show_dialog(self, screen, size):
        x, y = size
        if self.show_d:
            pygame.draw.rect(screen, ('#C6B472'), ((x - 200, 210), (200, 200)))
            for i in range(len(self.info)):
                back = self.font.render(self.info[i], 1, '#000000')
                screen.blit(back, (x - 200, (210 + 20 * i)))
            if self.color == '#35BA41':
                screen.blit(self.used_res, (x - 150, 320))
                back = self.font.render(str(self.barraks_cost), 1, '#000000')
                screen.blit(back, (x - 120, 325))
            screen.blit(self.used_res, (x - 150, 240))
            back = self.font.render(str(self.cost), 1, '#000000')
            screen.blit(back, (x - 120, 245))

    def build_barrakes(self):
        pass


class Forest(Resourses):
    def __init__(self):
        super().__init__()
        self.return_res = 3
        self.image = pygame.image.load('data/forest.png').convert()
        self.color = '#1E6631'
        self.not_using = True
        self.cost = 20
        self.info = ['посторить лесопилку', 'цена:']

    def start_work(self, other):
        if other.wood >= self.cost and self.not_using:
            self.not_using = False
            other.wood -= self.cost
            self.image = pygame.image.load('data/using_forest.png').convert()
            other.extract_wood += self.return_res


class Lawn(Resourses):
    def __init__(self):
        super().__init__()
        self.return_res = 5
        self.image = pygame.image.load('data/lawn.png').convert()
        self.cost = 10
        self.not_using = True
        self.barraks_cost = 200
        self.color = '#35BA41'
        self.info = ['посторить ферму', 'цена:', '', '', '' 'посторить казармы', 'цена:']

    def start_work(self, other):
        if other.wood >= self.cost and self.not_using:
            self.not_using = False
            other.wood -= self.cost
            self.image = pygame.image.load('data/farm.png').convert()
            other.extract_food += self.return_res

    def build_barrakes(self, other):
        if other.wood >= self.barraks_cost and self.not_using:
            self.isbarak = True
            self.not_using = False
            other.wood -= self.barraks_cost
            self.image = pygame.image.load('data/barraks.png').convert()

    def hire_warriors(self, screen, size):
        x, y = size
        self.show_d = True
        used_res = pygame.image.load('data/iron.png')
        pygame.draw.rect(screen, ('#C6B472'), ((x - 200, 210), (200, 200)))
        screen.blit(used_res, (x - 150, 320))
        back = self.font.render('3', 1, '#000000')
        screen.blit(back, (x - 120, 325))
        screen.blit(used_res, (x - 150, 240))
        back = self.font.render('5', 1, '#000000')
        screen.blit(back, (x - 120, 245))
        warriors = ['нанять меника', 'нанять лучника']
        for i in range(len(warriors)):
            back = self.font.render(warriors[i], 1, '#000000')
            screen.blit(back, (x - 200, (210 + 80 * i)))


    def buy_swordman(self, other):
        if other.mettal >= 3 and other.food > 0:
            other.mettal -= 5
            other.eating_bread += 2
            if list(filter(lambda unit: isinstance(unit, Swordman), other.army)):
                other.add_sword()
            else:
                other.get_unit(Swordman())

    def buy_bowman(self, other):
        if other.mettal >= 3 and other.food > 0:
            other.mettal -= 3
            other.eating_bread += 1
            if list(filter(lambda unit: isinstance(unit, LongBow), other.army)):
                other.add_bow()
            else:
                other.get_unit(LongBow())


class Mine(Resourses):
    def __init__(self):
        super().__init__()
        self.return_res = 3
        self.image = pygame.image.load('data/mine.png').convert()
        self.color = '#738595'
        self.cost = 60
        self.using = True
        self.info = ['активировать шахту', 'цена:']

    def start_work(self, other):
        if other.wood >= self.cost and self.using:
            self.not_using = False
            other.wood -= self.cost
            self.image = pygame.image.load('data/usingmine.png').convert()
            other.extract_mettal += self.return_res
