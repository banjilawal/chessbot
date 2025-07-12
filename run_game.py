import sys
from pathlib import Path

import pygame

from geometry import Dimension, GridCoordinate
from board import Board

from grid_entity import HorizontalMover, VerticalMover

from game_display import GameDisplay
from id_factory import id_factory

sys.path.append(str(Path(__file__).parent.absolute()))

def main():
    board = Board(dimension=Dimension(length=12, height=12))
    board.add_new_entity(GridCoordinate(1,1), HorizontalMover(mover_id=id_factory.mover_id(), height=1))
    board.add_new_entity(GridCoordinate(1,2), HorizontalMover(mover_id=id_factory.mover_id(), height=3))
    board.add_new_entity(GridCoordinate(8,8), HorizontalMover(mover_id=id_factory.mover_id(), height=4))

    board.add_new_entity(GridCoordinate(5,4), VerticalMover(mover_id=id_factory.mover_id(), length=6))
    board.add_new_entity(GridCoordinate(1,6), VerticalMover(mover_id=id_factory.mover_id(), length=6))
    board.add_new_entity(GridCoordinate(8,2), VerticalMover(mover_id=id_factory.mover_id(), length=1))


    visualizer = GameDisplay(board)
    visualizer.board.add_new_entity(GridCoordinate(5, 0), HorizontalMover(mover_id=id_factory.mover_id(), height=4))


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