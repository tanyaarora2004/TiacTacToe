import sys
import pygame
from board import Board
from settings import Settings
from ai_minimax import Ai


class TicTacToe:
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.width, self.settings.height))
        pygame.display.set_caption('Tic Tac Toe')

        self.board = Board(self)

    def run_game(self):
        while True:
            self.settings.fps_clock.tick(self.settings.FPS)
            self._check_events()
            self.settings.game_flag = self.check_win()
            if not self.settings.game_flag:
                self.draw_boards_and_symbols()
            else:
                self.draw_result()
                self.draw_text_restart()
            pygame.display.update()

    def run_game_vs_ai(self):
        while True:
            ai = Ai(self)
            self.settings.fps_clock.tick(self.settings.FPS)
            self._check_events()
            self.settings.game_flag = self.check_win()
            if not self.settings.game_flag:
                self.draw_boards_and_symbols()
            else:
                self.draw_result()
                self.draw_text_restart()
            if self.settings.curr_player == 'ai':
                ai.best_move()
            pygame.display.update()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.settings.game_flag:
                self.board.insert_symbol()
                self.settings.curr_player = 'ai'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.new_game()

    def draw_boards_and_symbols(self):
        for row in range(3):
            for column in range(3):
                self.board.draw_grid(row, column)
                self.board.draw_symbol(row, column)

    def check_win(self):
        zero = 0
        for row in self.board.mas:
            zero += row.count(0)
            if ['X']*3 == row or ['O']*3 == row:
                return row[0]
        for col in range(3):
            if self.board.mas[0][col] == self.board.mas[1][col] == self.board.mas[2][col] != 0:
                return self.board.mas[2][col]
        if self.board.mas[0][0] == self.board.mas[1][1] == self.board.mas[2][2] != 0:
            return self.board.mas[2][2]
        if self.board.mas[0][2] == self.board.mas[1][1] == self.board.mas[2][0] != 0:
            return self.board.mas[2][0]
        if zero == 0:
            return 'Tie!'

    def draw_result(self):
        self.screen.fill(self.settings.BLACK)
        font = pygame.font.SysFont('comicsans', 80)

        text = font.render(self.settings.game_flag,
                           True, self.settings.WHITE)
        text_rect = text.get_rect()
        text_x = self.screen.get_width() / 2 - text_rect.width / 2
        text_y = self.screen.get_height() / 2 - text_rect.height / 2
        self.screen.blit(text, [text_x, text_y])

    def draw_text_restart(self):
        font = pygame.font.SysFont('comicsans', 25)
        text_restart = 'Press the <space> to restart the game'
        text_render = font.render(
            text_restart, True, self.settings.WHITE)
        text_restart_rect = text_render.get_rect()
        text_restart_x = self.screen.get_width() / 2 - text_restart_rect.width / 2
        text_restart_y = self.screen.get_height() - text_restart_rect.height

        self.screen.blit(text_render, (text_restart_x, text_restart_y))

    def new_game(self):
        self.settings.game_flag = False
        self.board.mas = [[0] * 3 for i in range(3)]
        self.settings.counter = 0
        self.screen.fill(self.settings.BLACK)
        self.settings.curr_player = 'ai'


if __name__ == '__main__':
    tt_game = TicTacToe()
    # tt_game.run_game()
    tt_game.run_game_vs_ai()
