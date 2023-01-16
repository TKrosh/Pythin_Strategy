import pygame
from Units import Swordman, Evilenemy, Unit, MovingCell, Evilwithard, LongBow

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


    def find_target(self):
        """поиск боту цели"""
        player_army_min_health = min([unit.health for unit in self.player_army])
        for unit in self.player_army:
            if player_army_min_health == unit.health:
                self.target = unit
                break

    def go(self):
        """передвижение"""
        #x, y = self.player_army[self.target]
        for unit in self.army:
            x, y = self.army[unit]
            unit.moving(self.board, y, x)
            if isinstance(self.board[x][y - 8], MovingCell):
                print('!')
                self.board[x][y - 8].change_position(self.board, x, y - 8, x, y, unit)
                self.play_board.clean_cell()
        for unit in self.army:
            unit.refresh()
