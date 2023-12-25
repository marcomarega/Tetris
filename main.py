from time import time

import pygame

from core import Game, Figure0, Figure1, Figure2, Figure3, Figure4, Figure5, Figure6
from load import *

if __name__ == "__main__":
    game = Game(
        plain_size=PLAIN_SIZE,
        figures=[Figure0, Figure1, Figure2, Figure3, Figure4, Figure5, Figure6],
        colors=[pygame.Color("red"), pygame.Color("green"), pygame.Color("blue"), pygame.Color("yellow")]
    )
    running = True
    previous_time = time()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game.game_over():
                continue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                if event.key == pygame.K_RIGHT:
                    game.move_right()
                if event.key == pygame.K_UP:
                    game.rotate_left()
                if event.key == pygame.K_DOWN:
                    game.rotate_right()
                if event.key == pygame.K_SPACE:
                    game.force_down()
        game.update_figure()
        if time() - previous_time > TICK:
            game.down()
            previous_time = time()
        display.fill((0, 0, 0))
        game.draw(display)
        pygame.display.flip()
