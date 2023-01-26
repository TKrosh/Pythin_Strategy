import pygame
from Units import Swordman, Evilenemy, Unit, MovingCell, Evilwithard, LongBow
from random import randint

class main_Player:
    def __init__(self, size):
        x, y = size
        super().__init__()
        self.army = []
        self.extract_food, self.extract_wood, self.extract_mettal = 0, 0, 0
        self.eating_bread = 0
        self.food, self.wood, self.mettal = 40, 200, 40
        self.image = pygame.image.load('data/player.png')
        self.rect = self.image.get_rect().move(
            x // 2, y // 2)

    def get_resourses(self):
        return (self.food, self.wood, self.mettal)

    def hire_warrior(self, warrior):
        self.army.append(warrior)

    def delete_group(self):
        for unit in range(len(self.army)):
            if self.army[unit].amount == 0:
                self.army.pop(unit)

    def show(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def get_profit(self):
        self.food += self.extract_food - self.eating_bread
        if self.food < 0 and self.army:
            self.unit_dead()
        self.wood += self.extract_wood
        self.mettal += self.extract_mettal

    def unit_dead(self):
        for u in range(len(self.army)):
            self.eating_bread -= self.army[u].eating
            self.army[u].unit_dead()
            self.delete_group()
            break

    """после боя учитывать потери"""
    def alive_army(self, alive_warrior):
        self.army = alive_warrior

    def get_unit(self, unit):
        self.army.append(unit)

    def add_sword(self):
        for u in self.army:
            if isinstance(u, Swordman):
                u.add_warrior()

    def add_bow(self):
        for u in self.army:
            if isinstance(u, LongBow):
                u.add_warrior()



class Enamy:
    def __init__(self, pos_x, pos_y, army):
        super().__init__()
        self.x, self.y = pos_x, pos_y
        self.army = army
        self.image = pygame.image.load('data/enamy_tile.png')
        self.rect = self.image.get_rect().move(
            50 * pos_x, 50 * pos_y)

    def get_coords(self):
        return self.x, self.y

    def __len__(self):
        return len(self.army)

    def __getitem__(self, index):
        return self.army[index]

    def show(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def get_stronger(self):
        self.army[randint(0, 3)].add_warrior()