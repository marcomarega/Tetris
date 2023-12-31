from core.block import Block
from core.figure import Figure
from functions import fill_of_none


class Plain:
    def __init__(self, size: tuple[int, int]):
        self.size = size
        self.blocks: list[list[Block]] = fill_of_none(size)

    def clear(self):
        self.blocks: list[list[Block]] = fill_of_none(self.size)

    def matches(self, pos: tuple[int, int], figure: Figure) -> bool:
        for i in range(figure.size[0]):
            for j in range(figure.size[1]):
                if figure.blocks[i][j] is None:
                    continue
                block_i = pos[0] + i
                block_j = pos[1] + j
                if block_i < 0:
                    continue
                if not block_i < self.size[0] or not 0 <= block_j < self.size[1] or\
                        self.blocks[block_i][block_j] is not None:
                    return False
        return True

    def can_down(self, pos: tuple[int, int], figure: Figure) -> bool:
        pos = pos[0] + 1, pos[1]
        return self.matches(pos, figure)

    def can_move_left(self, pos: tuple[int, int], figure: Figure) -> bool:
        pos = pos[0], pos[1] - 1
        return self.matches(pos, figure)

    def can_move_right(self, pos: tuple[int, int], figure: Figure) -> bool:
        pos = pos[0], pos[1] + 1
        return self.matches(pos, figure)

    def paint(self, pos: tuple[int, int], figure: Figure):
        for i in range(figure.size[0]):
            for j in range(figure.size[1]):
                if figure.blocks[i][j] is None:
                    continue
                block_i = pos[0] + i
                block_j = pos[1] + j
                if block_i < 0:
                    continue
                self.blocks[block_i][block_j] = figure.blocks[i][j]

    def full(self) -> bool:
        return any(self.blocks[0])

    def pop(self) -> int:
        pops_count = 0
        row_indexes: list[int] = list()
        for i in range(self.size[0]):
            if not all(self.blocks[i]):
                row_indexes.append(i)
            else:
                pops_count += 1
        blocks: list[list[Block]] = list()
        while len(blocks) + len(row_indexes) < self.size[0]:
            blocks.append([None for j in range(self.size[1])])
        for i in row_indexes:
            blocks.append(self.blocks[i])
        self.blocks = blocks
        return pops_count
