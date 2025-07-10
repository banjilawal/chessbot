import os
import sys
from pathlib import Path

import pygame

from model.board import Board

from ui.visualization import Visualizer

sys.path.append(str(Path(__file__).parent.absolute()))

def main():
    board = Board()
    visualizer = Visualizer()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        visualizer.update_display()
    visualizer.close()

if __name__ == "__main__":
    main()


