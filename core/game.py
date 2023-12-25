import random

import pygame

from core.figure import Figure
from core.plain import Plain
from load import PLAIN_SIZE


class Game:
    def __init__(self, plain_size: tuple[int, int], colors: list[pygame.Color], figures: list):
        self.over = False
        self.plain = Plain(plain_size)
        self.colors = colors
        self.pos = None
        self.figure: Figure = None
        self.figures = figures

    def restart(self):
        self.over = False
        self.plain.clear()
        self.pos = None
        self.figure = None

    def game_over(self) -> bool:
        if self.over:
            return True
        self.over = self.plain.full()
        return self.over

    def update(self):
        if self.over:
            return
        if self.figure is None:
            self.figure = random.choice(self.figures)(random.choice(self.colors))
            self.pos = -self.figure.size[0], self.plain.size[1] // 2
        self.plain.pop()

    def move_left(self):
        if self.figure is None:
            return
        if self.plain.can_move_left(self.pos, self.figure):
            if self.pos[1] - 1 >= 0:
                self.pos = self.pos[0], self.pos[1] - 1

    def move_right(self):
        if self.figure is None:
            return
        if self.plain.can_move_right(self.pos, self.figure):
            if self.pos[1] + 1 < self.plain.size[1]:
                self.pos = self.pos[0], self.pos[1] + 1

    def rotate_left(self):
        if self.figure is None:
            return
        self.figure.rotate_left()

    def rotate_right(self):
        if self.figure is None:
            return
        self.figure.rotate_right()

    def down(self):
        if self.figure is None:
            return
        if self.plain.can_down(self.pos, self.figure):
            self.pos = self.pos[0] + 1, self.pos[1]
        else:
            self.plain.paint(self.pos, self.figure)
            self.pos = None
            self.figure = None

    def force_down(self):
        while self.figure is not None:
            self.down()

    def draw(self, surface: pygame.Surface):
        self.plain.draw(surface)
        if self.figure is not None:
            self.figure.draw(surface, self.pos, PLAIN_SIZE)
