import pygame
from math import inf


class Ai:
    def __init__(self, tt_game):
        self.tt_game = tt_game
        self.settings = tt_game.settings
        self.board = tt_game.board

        self.scores = {'X': 1, 'O': -1, 'Tie!': 0}
        self.row_i, self.col_j = 0, 0

    def best_move(self):
        best_score = -inf
        for i in range(3):
            for j in range(3):
                if self.board.mas[i][j] == 0:
                    self.board.mas[i][j] = 'X'
                    score = self.minimax(self.board.mas, False)
                    self.board.mas[i][j] = 0
                    if score > best_score:
                        best_score = score
                        self.row_i, self.col_j = i, j
        self.board.insert_symbol_ai(self.row_i, self.col_j)
        self.settings.curr_player = 'human'

    def minimax(self, mas_board, next_move_is_max):
        self.result = self.tt_game.check_win()
        if self.result != None:
            return self.scores[self.result]

        if next_move_is_max:
            great_move = self.min_or_max(-inf, 'X', False, max)
        else:
            great_move = self.min_or_max(inf, 'O', True, min)
        return great_move

    def min_or_max(self, infin, symbol, g_boole, foo_min_or_max):
        best_score = infin
        for i in range(3):
            for j in range(3):
                if self.board.mas[i][j] == 0:
                    self.board.mas[i][j] = symbol
                    score = self.minimax(self.board.mas, g_boole)
                    self.board.mas[i][j] = 0
                    best_score = foo_min_or_max(score, best_score)
        return best_score
