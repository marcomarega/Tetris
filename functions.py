def fill_of_none(size: tuple[int, int]) -> list[list]:
    return [
        [None for j in range(size[1])]
        for i in range(size[0])
    ]


def rotate_left(matrix: list[list]) -> list[list]:
    rotated_matrix = [
        [matrix[i][j] for i in range(len(matrix))]
        for j in range(len(matrix[0]))
    ]
    rotated_matrix.reverse()
    return rotated_matrix


def rotate_right(matrix: list[list]) -> list[list]:
    rotated_matrix = [
        [matrix[i][j] for i in range(len(matrix))]
        for j in range(len(matrix[0]))
    ]
    for row in rotated_matrix:
        row.reverse()
    return rotated_matrix
