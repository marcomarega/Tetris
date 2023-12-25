import pygame

from core import block
from core.block import Block
from functions import rotate_left, rotate_right
from load import CELL_SIZE


class Figure:
    def __init__(self, size: tuple[int, int], blocks: list[list[block]]):
        self.size = size
        self.blocks = blocks

    def rotate_left(self):
        self.size = self.size[1], self.size[0]
        self.blocks = rotate_left(self.blocks)

    def rotate_right(self):
        self.size = self.size[1], self.size[0]
        self.blocks = rotate_right(self.blocks)

    def draw(self, surface: pygame.Surface, pos: tuple[int, int], size: tuple[int, int]):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                pi = pos[0] + i
                pj = pos[1] + j
                if not 0 <= pi < size[0] or not 0 <= pj < size[1]:
                    continue
                if self.blocks[i][j] is None:
                    continue
                pygame.draw.rect(surface, self.blocks[i][j].color, (pj * CELL_SIZE, pi * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                                 0)


class Figure0(Figure):
    def __init__(self, color: pygame.Color):
        size = (2, 3)
        blocks = [
            [Block(color), Block(color), Block(color)],
            [None, Block(color), None]
        ]
        super(Figure0, self).__init__(size, blocks)


class Figure1(Figure):
    def __init__(self, color: pygame.Color):
        size = (1, 4)
        blocks = [
            [Block(color), Block(color), Block(color)],
            [None, Block(color), None]
        ]
        super(Figure1, self).__init__(size, blocks)


class Figure2(Figure):
    def __init__(self, color: pygame.Color):
        size = (2, 3)
        blocks = [
            [Block(color), None, None],
            [Block(color), Block(color), Block(color)]
        ]
        super(Figure2, self).__init__(size, blocks)


class Figure3(Figure):
    def __init__(self, color: pygame.Color):
        size = (2, 3)
        blocks = [
            [Block(color), Block(color), Block(color)],
            [Block(color), None, None]
        ]
        super(Figure3, self).__init__(size, blocks)


class Figure4(Figure):
    def __init__(self, color: pygame.Color):
        size = (2, 3)
        blocks = [
            [Block(color), Block(color), None],
            [None, Block(color), Block(color)]
        ]
        super(Figure4, self).__init__(size, blocks)


class Figure5(Figure):
    def __init__(self, color: pygame.Color):
        size = (2, 3)
        blocks = [
            [None, Block(color), Block(color)],
            [Block(color), Block(color), None]
        ]
        super(Figure5, self).__init__(size, blocks)


class Figure6(Figure):
    def __init__(self, color: pygame.Color):
        size = (2, 2)
        blocks = [
            [Block(color), Block(color)],
            [Block(color), Block(color)]
        ]
        super(Figure6, self).__init__(size, blocks)
