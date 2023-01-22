import pygame
from Units import Swordman, Evilenemy, Unit, MovingCell, Evilwithard, LongBow, sing


class Intelligence():
    def __init__(self, board):
        self.play_board = board
        self.target = 0
        self.win = False

    def get_situation(self, board):
        """где находятся юниты игрока и бота"""
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
            if self.player_army:
                player_army_health = sorted(self.player_army, key=lambda unit: unit.health)
                self.target = player_army_health[0]
            else:
                print('!')

    def go(self):
        """передвижение"""
        for unit in self.army:
            x, y = self.army[unit]
            """переменные повторяются, чтобы различать от куда и куда шёл юнит"""
            x_way, y_way = x, y
            xt, yt = self.player_army[self.target]
            distance = abs(x - xt) + abs(y - yt)
            if unit.curent_energy < distance - 1:
                x_way, y_way = self.find_way(unit)
                unit.moving(self.board, y, x)
                if isinstance(self.board[x_way][y_way], MovingCell):
                    self.board[x_way][y_way].change_position(self.board, x_way, y_way, x, y, unit)
                    self.play_board.clean_cell()
            else:
                self.target.coords(xt, yt)
                self.target.get_board(self.board)
                """если юнит убил другого юнита, то self.board[self.U_x][self.U_y] = 0"""
                if isinstance(self.board[x][y], Unit):
                    unit.get_board(self.board)
                    unit.coords(x, y)
                    if self.board[xt][yt].side == 1:
                        unit.atack(self.target)
                    else:
                        self.find_target()
            self.play_board.movement(unit)

    def find_way(self, unit):
        x, y = self.army[unit]
        xt, yt = self.player_army[self.target]
        move_x = abs((x - xt) // 2)
        move_y = unit.curent_energy - 1 - move_x
        while move_y < 0:
            move_y += 1
        return x + move_x * sing(xt - x), \
            y + move_y * sing(yt - y)
