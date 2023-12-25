import pygame

from load import CELL_SIZE, BORDER_SIZE, BORDER_COLOR


class Block:
    def __init__(self, color: pygame.Color):
        self.color = color

    def draw(self, surface: pygame.Surface, pos: tuple[int, int], delta: tuple[int, int], size: tuple[int, int]):
        i, j = pos
        pi = delta[0] + i
        pj = delta[1] + j
        if not 0 <= pi < size[0] or not 0 <= pj < size[1]:
            return
        pygame.draw.rect(surface, self.color, (pj * CELL_SIZE, pi * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                         0)
        pygame.draw.rect(surface, BORDER_COLOR, (pj * CELL_SIZE, pi * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                         BORDER_SIZE)
