import pygame


class Board:
    def __init__(self, tt_game):

        self.screen = tt_game.screen
        self.settings = tt_game.settings
        self.screen_rect = self.screen.get_rect()
        self.mas = [[0] * 3 for i in range(3)]

    def draw_grid(self, row, column):
        self.x, self.y = self.calc_coord(row, column)
        self.color = self.choise_color(row, column)
        pygame.draw.rect(self.screen, self.color, (self.x,
                                                   self.y, self.settings.size_block, self.settings.size_block))

    def calc_coord(self, row, column):
        x = column * self.settings.size_block + \
            (column + 1) * self.settings.margin
        y = row * self.settings.size_block + (row+1) * self.settings.margin
        return x, y

    def choise_color(self, row, column):
        if self.mas[row][column] == 'X':
            color = self.settings.RED
        elif self.mas[row][column] == 'O':
            color = self.settings.BLUE
        else:
            color = self.settings.WHITE
        return color

    def insert_symbol(self):
        self.x_pos, self.y_pos = pygame.mouse.get_pos()
        self.col = self.x_pos // (self.settings.size_block +
                                  self.settings.margin)
        self.row = self.y_pos // (self.settings.size_block +
                                  self.settings.margin)
        if self.mas[self.row][self.col] == 0:
            if self.settings.counter % 2 == 0:
                self.mas[self.row][self.col] = 'X'
            else:
                self.mas[self.row][self.col] = 'O'
                self.settings.curr_player = 'ai'
            self.settings.counter += 1

    def insert_symbol_ai(self, row_i, col_j):
        if self.mas[row_i][col_j] == 0:
            self.mas[row_i][col_j] = 'X'
            self.settings.counter += 1

    def draw_symbol(self, row, column):
        x, y = self.calc_coord(row, column)
        if self.color == self.settings.RED:
            pygame.draw.line(self.screen, self.settings.WHITE, (x+10, y+10),
                             (x+self.settings.size_block - 10, y+self.settings.size_block - 10), 10)
            pygame.draw.line(self.screen, self.settings.WHITE, (x+self.settings.size_block - 10, y+10),
                             (x+10, y+self.settings.size_block - 10), 10)
        elif self.color == self.settings.BLUE:
            pygame.draw.circle(self.screen, self.settings.WHITE, (x+self.settings.size_block //
                               2, y+self.settings.size_block//2), self.settings.size_block//2 - 10, 10)
