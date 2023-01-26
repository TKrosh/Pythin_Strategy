import pygame
import sys


def terminate():
    pygame.quit()
    sys.exit()




tile_width = tile_height = 50


class Window:
    def __init__(self):
        self.do = 1

    def render(self, screen, size):
        if self.do == 1:
            self.main_window(screen, size)
        if self.do == 3:
            self.settings(screen, size)
        if self.do == 4:
            self.upload(screen, size)

    def main_window(self, screen, size):
        intro_text = ["Начать игру", "Обучение", "Загрузить",
                           "выйти"]
        image = pygame.image.load('data/main_screen.jpg')
        font = pygame.font.SysFont('cambria', 35)
        fon = pygame.transform.scale(image, size)
        screen.blit(fon, (0, 0))
        for i in range(len(intro_text)):
            string_rendered = font.render(intro_text[i], 1, '#000000')
            screen.blit(string_rendered, (650, i * 100 + 250))

    def settings(self, screen, size):
        intro_text = ["В игре вы можете нажать esc и выйти в  гланое меню",
                      "у вас есть 3 вида русурсов они показаны в нижней части экрана",
                      "передвижение осуществляется на кнопки WASD",
                      "чтобы взаимодействовать с клеткой нажмите E",
                      "чтобы посторит что-нибудь нажмите на надпись или на цену в открывшемся окне",
                      "колличество простивников с каждым ходом увеличивается на 1 в каждом из 4х отрядов",
                      "если вы проиграли бой, вы продолжаете играть, но теперь вам нужно заново набирать армию",
                      "в игре присутствует мини карта со всеми ресурсами",
                      "сохранений пока нет, но будут в патче 1.1",
                      "ВАЖНО! Каждый ваш солдат потребляет единицу еды, в случае, если она кончиться,"
                      "каждый новый ход будет умирать 1 онит из случайного отряда",
                      "пока не будет хватать еды",
                      "время в игре очень важно, ибо калличество полей ограничено, а колличество врагов нет",
                      "после боя их кол-во восполняется полностью и ПродолжаЕт расти",
                      "проятной игрыБ приношу свои извинения за недоработки"]
        image = pygame.image.load('data/main_screen.jpg')
        font = pygame.font.SysFont('cambria', 35)
        fon = pygame.transform.scale(image, size)
        screen.blit(fon, (0, 0))
        back = font.render('←--', 1, '#000000')
        screen.blit(back, (0, 0))
        for i in range(len(intro_text)):
            string_rendered = font.render(intro_text[i], 1, '#FFFFFF')
            screen.blit(string_rendered, (0, i * 50 + 30))

    def upload(self, screen, size):
        image = pygame.image.load('data/main_screen.jpg')
        font = pygame.font.SysFont('cambria', 35)
        fon = pygame.transform.scale(image, size)
        screen.blit(fon, (0, 0))
        back = font.render('←--', 1, '#000000')
        screen.blit(back, (0, 0))

    def do_button(self, coords):
        x, y = coords
        if self.do == 1:
            if x >= 650 and x <= 850:
                if y >= 260 and y <= 300:
                    self.do = 2
                elif y >= 360 and y <= 400:
                    self.do = 3
                elif y >= 460 and y <= 500:
                    self.do = 4
                elif y >= 560 and y <= 600:
                    terminate()
        elif self.do == 3:
            print(x, y)
            if x <= 50 and y <= 50:
                self.do = 1
            elif x >= 240:
                if y >= 250 and y <= 300:
                    print('!')
                if y >= 350 and y <= 400:
                    print('!')
        elif self.do == 4:
            print(x, y)
            if x <= 50 and y <= 50:
                self.do = 1

    def start_game(self):
        if self.do == 2:
            return True
        else:
            return False

def upload():
    """тут должны были бы быть сохнанения ((("""
    pass

def end(screen, size):
    screen
    intro_text = [" Вы победили", "Спасибо за игру"]
    image = pygame.image.load('data/main_screen.jpg')
    font = pygame.font.SysFont('cambria', 35)
    fon = pygame.transform.scale(image, size)
    screen.blit(fon, (0, 0))
    for i in range(len(intro_text)):
        string_rendered = font.render(intro_text[i], 1, '#000000')
        screen.blit(string_rendered, (650, i * 100 + 250))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        pygame.display.flip()

def start_screen(screen, FPS, size):
    window = Window()
    clock = pygame.time.Clock()
    do = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    window.do_button(event.pos)
                if window.start_game():
                    return True
        window.render(screen, size)
        pygame.display.flip()
        clock.tick(FPS)