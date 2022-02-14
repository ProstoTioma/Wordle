import pygame
from screen import Screen
import random


class Game:
    def __init__(self):
        self.screen = Screen()
        self.words_list = ['Гиена', 'Петух']
        self.word = random.choice(self.words_list)
        self.alphabet = 'йцукенгшщзхъфывапролджэячсмитьбю'
        self.index = 0

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
                    if len(self.letters) < 5:
                        if event.unicode in self.alphabet and event.unicode is not '':
                            field = self.screen.field_squares
                            if self.index < len(field):
                                sq = field[self.index]
                                font = pygame.font.Font('futur.ttf', int(self.screen.sq_size // 2))
                                letter = font.render(event.unicode.upper(), True, (255, 255, 255),
                                                     self.screen.bg)
                                letter_rect = letter.get_rect()
                                letter_rect.center = sq.center

                                self.letters.append([event.unicode.upper(), letter_rect])
                                self.index += 1
                                print(self.letters[self.index - 1][0])

                    if event.key == pygame.K_BACKSPACE:
                        if self.index > 0:
                            self.letters[self.index - 1][0] = '    '
                            self.index -= 1
                            print(self.letters[self.index - 1][0])

                    if event.key == pygame.K_RETURN:
                        self.check_word()

            pygame.display.flip()

    def blit_letters(self):
        for letter in self.letters:
            letter_rect = letter[1]
            font = pygame.font.Font('futur.ttf', int(self.screen.sq_size // 2))
            let = font.render(letter[0], True, (255, 255, 255), self.screen.bg)
            self.screen.screen.blit(let, letter_rect)

    def check_word(self):
        for i in range(len(self.letters)):
            if self.letters[i] == self.word[i].upper():
                rect = self.screen.field_squares[i]
                pygame.draw.rect(self.screen.screen, (0, 255, 0), rect, 1)
                pygame.display.flip()
