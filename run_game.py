import os
import sys
from pathlib import Path

import pygame

from common.dimension import Dimension
from model.board import Board
from model.grid_coordinate import GridCoordinate
from model.vault import HorizontalMover

from ui.visualization import Visualizer

sys.path.append(str(Path(__file__).parent.absolute()))

def main():
    board = Board(dimension=Dimension(length=12, height=12))
    board.add_new_entity(GridCoordinate(1,1), HorizontalMover(1, 1))
    board.add_new_entity(GridCoordinate(1,2), HorizontalMover(2, 3))
    board.add_new_entity(GridCoordinate(8,8), HorizontalMover(3, 2))
    visualizer = Visualizer(board)

    visualizer.board.add_new_entity(GridCoordinate(5,0), HorizontalMover(6, 4))

    clock = pygame.time.Clock()
    frame_count = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                visualizer.handle_mouse_down(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                visualizer.handle_mouse_up(event)
            elif event.type == pygame.MOUSEMOTION:
                visualizer.handle_mouse_motion(event)

        visualizer.update_display()
        clock.tick(200)
        frame_count += 1
        if frame_count % 60== 0:
            print(f"Frame {frame_count}")
    visualizer.close()

if __name__ == "__main__":
    main()