import pygame
from Units import Swordman, Evilenemy, Unit, MovingCell, Evilwithard, LongBow, sing

class Intelligence():
    def __init__(self, board):
        self.play_board = board
        self.target = 0

    def get_situation(self, board):
        """где находятся июниты игрока и бота"""
        self.board = board
        self.army = {}
        self.player_army = {}
        diap_y, diap_x = len(board), len(board[0])
        for x in range(diap_y):
            for y in range(diap_x):
                cell = board[x][y]
                if isinstance(cell, Unit):
                    if cell.side != 0:
                        self.player_army[cell] = (x, y)
                    else:
                        self.army[cell] = (x, y)
        self.find_target()
        self.go()

    def find_target(self, close=False):
        """поиск боту цели"""
        if close:
            pass
        else:
            player_army_health = sorted(self.player_army, key=lambda unit: unit.health)
            self.target = player_army_health[0]

    def go(self):
        """передвижение"""

        for unit in self.army:
            x, y = self.army[unit]
            x_way, y_way = self.find_way(unit)
            unit.moving(self.board, y, x)
            if isinstance(self.board[x_way][y_way], MovingCell):
                self.board[x_way][y_way].change_position(self.board, x_way, y_way, x, y, unit)
                self.play_board.clean_cell()
                self.play_board.movement(unit)

    def find_way(self, unit):
        x, y = self.army[unit]
        xt, yt = self.player_army[self.target]
        distance = abs(x - xt) + abs(y - yt)
        if unit.curent_energy < distance - 1:
            move_x = abs((x - xt) // 2)
            move_y = unit.curent_energy - 1 - move_x
            while move_y < 0:
                move_y += 1
            return x + move_x * sing(xt - x), \
                y + move_y * sing(yt - y)
        #else:


    def atack_close_enamy(self):
        xt, yt = self.player_army[self.target]
