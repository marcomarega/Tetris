import pygame

pygame.init()
FPS = 60
TICK = 0.2
clock = pygame.time.Clock()
PLAIN_SIZE = PLAIN_WIDTH, PLAIN_HEIGHT = 30, 20
CELL_SIZE = 20
SIZE = WIDTH, HEIGHT = PLAIN_HEIGHT * CELL_SIZE, PLAIN_WIDTH * CELL_SIZE
display = pygame.display.set_mode(SIZE)

GAME_NAME = "Tetris"
pygame.display.set_caption(GAME_NAME)
