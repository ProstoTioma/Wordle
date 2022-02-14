import pygame
from screen import Screen
import random


class Game:
    def __init__(self):
        self.screen = Screen()
        self.word = random.choice(open("data", encoding='utf8').read().split('\n'))
        self.alphabet = 'йцукенгшщзхъфывапролджэячсмитьбюё'
        self.index = 0
        print(self.word)

        self.row_ind = 1

        self.letters = list()

    def start(self):
        self.screen.draw()

        while True:
            self.blit_letters()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

                if event.type == pygame.KEYDOWN:
                    removed_blanks = self.letters.copy()

                    for i in range(len(self.letters)):
                        if self.letters[i][0] == '    ':
                            try:
                                removed_blanks.remove([self.letters[i][0], self.letters[i][1]])
                            except ValueError:
                                pass
                    self.letters = removed_blanks
                    if len(self.letters) < 5 * self.row_ind:
                        if event.unicode in self.alphabet and event.unicode is not '':
                            field = self.screen.field_squares
                            if self.index < len(field):
                                sq = field[self.index]
                                font = pygame.font.Font('futur.ttf', int(self.screen.sq_size // 3))
                                letter = font.render(event.unicode.upper(), True, (255, 255, 255),
                                                     self.screen.bg)
                                letter_rect = letter.get_rect()
                                letter_rect.center = sq.center

                                self.letters.append([event.unicode.upper(), letter_rect])
                                self.index += 1
                                # print(self.letters[self.index - 1][0])

                    if event.key == pygame.K_BACKSPACE:
                        if self.index > 0 and self.index > (5 * (self.row_ind - 1)):
                            self.letters[self.index - 1][0] = '    '
                            self.index -= 1
                            # print(self.letters[self.index - 1][0])

                    if event.key == pygame.K_RETURN and len(self.letters) == 5 * self.row_ind:
                        self.check_word()
                        self.row_ind += 1
                        # self.letters.clear()

            pygame.display.flip()

    def blit_letters(self):
        for letter in self.letters:
            letter_rect = letter[1]
            font = pygame.font.Font('futur.ttf', int(self.screen.sq_size // 3))
            let = font.render(letter[0], True, (255, 255, 255), self.screen.bg)
            self.screen.screen.blit(let, letter_rect)

    def check_word(self):
        for i in range(5):
            if self.letters[i + 5 * (self.row_ind - 1)][0] == self.word[i].upper():
                rect = self.screen.field_squares[i + 5 * (self.row_ind - 1)]
                pygame.draw.rect(self.screen.screen, (0, 255, 0), rect, 1)
                pygame.display.flip()
            elif self.letters[i + 5 * (self.row_ind - 1)][0] in self.word.upper():
                rect = self.screen.field_squares[i + 5 * (self.row_ind - 1)]
                pygame.draw.rect(self.screen.screen, (220, 197, 31), rect, 1)
                pygame.display.flip()
