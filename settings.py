import pygame


class Settings:
    def __init__(self):
        self.size_block = 150
        self.margin = 10
        self.width = self.size_block*3 + self.margin*4
        self.height = self.size_block*3 + self.margin*4

        self.FPS = 20
        self.fps_clock = pygame.time.Clock()

        self.counter = 0

        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)

        self.game_flag = False
        self.curr_player = 'ai'
