import pygame

pygame.init()
FPS = 60
TICK = 0.3
clock = pygame.time.Clock()
PLAIN_SIZE = PLAIN_WIDTH, PLAIN_HEIGHT = 20, 10
CELL_SIZE = 30
SIZE = WIDTH, HEIGHT = PLAIN_WIDTH * CELL_SIZE, PLAIN_HEIGHT * CELL_SIZE
display = pygame.display.set_mode(SIZE)

GAME_NAME = "Tetris"
pygame.display.set_caption(GAME_NAME)
