import pygame


class Screen:

    def __init__(self):
        self.width = 600
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bg = (18, 18, 19)
        self.border_color = (58, 58, 60)
        self.field_squares = list()
        self.n_sq = 5
        self.n_rows = 6

        self.sq_size = self.width / self.n_sq

    def draw(self):
        self.draw_background()
        self.draw_field()

    def draw_background(self):
        pygame.init()
        pygame.display.set_caption('Wordle')
        self.screen.fill(self.bg)

    def draw_field(self):
        for i in range(self.n_rows):
            for j in range(self.n_sq):
                rect = pygame.Rect(self.sq_size * j, self.sq_size * i, self.sq_size, self.sq_size)
                self.field_squares.append(rect)
                pygame.draw.rect(self.screen, self.border_color, rect, 2, 50)
                pygame.display.flip()


