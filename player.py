import pygame


class main_Player:
    def __init__(self, size):
        x, y = size
        super().__init__()
        self.army = []
        self.extract_food, self.extract_wood, self.extract_mettal = 0, 0, 0
        """дерева изначально 20"""
        self.food, self.wood, self.mettal = 10, 400, 10
        self.image = pygame.image.load('data/player.png')
        self.rect = self.image.get_rect().move(
            x // 2, y // 2)

    def get_resourses(self):
        return (self.food, self.wood, self.mettal)

    def hire_warrior(self, warrior):
        self.army.append(warrior)

    def show(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def get_profit(self):
        self.food += self.extract_food
        self.wood += self.extract_wood
        self.mettal += self.extract_mettal


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