import pygame

import core
from load import BORDER_COLOR, CELL_SIZE, BORDER_SIZE, PLAIN_SIZE


def draw_block(self, surface: pygame.Surface, pos: tuple[int, int], delta: tuple[int, int], size: tuple[int, int]):
    i, j = pos
    pi = delta[0] + i
    pj = delta[1] + j
    if not 0 <= pi < size[0] or not 0 <= pj < size[1]:
        return
    pygame.draw.rect(surface, self.color, (pj * CELL_SIZE, pi * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                     0)
    pygame.draw.rect(surface, BORDER_COLOR, (pj * CELL_SIZE, pi * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                     BORDER_SIZE)


core.Block.draw = draw_block


def draw_figure(self, surface: pygame.Surface, pos: tuple[int, int], size: tuple[int, int]):
    for i in range(self.size[0]):
        for j in range(self.size[1]):
            if self.blocks[i][j] is not None:
                self.blocks[i][j].draw(surface, (i, j), pos, size)


core.Figure.draw = draw_figure


def draw_plain(self, surface: pygame.Surface):
    for i in range(self.size[0]):
        for j in range(self.size[1]):
            if self.blocks[i][j] is not None:
                self.blocks[i][j].draw(surface, (i, j), (0, 0), self.size)


core.Plain.draw = draw_plain


def draw_game(self, surface: pygame.Surface):
    self.plain.draw(surface)
    if self.figure is not None:
        self.figure.draw(surface, self.pos, PLAIN_SIZE)


core.Game.draw = draw_game
