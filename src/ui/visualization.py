from dataclasses import dataclass, field

import pygame
from typing import TYPE_CHECKING, List
from model.grid_entity import GridEntity

if TYPE_CHECKING:
    from model.board import Board
    from model.vault import HorizontalMover

@dataclass
class Visualizer:
    board: 'Board'

    cell_px: int = 60
    border_px: int = 2
    screen_width: int = 800
    screen_height: int = 800

    background_color: pygame.Color = field(default_factory=lambda: pygame.Color('black'))
    cell_color: pygame.Color = field(default_factory=lambda: pygame.Color('white'))
    horizontal_mover_color: pygame.Color = field(default_factory=lambda: pygame.Color('red'))

    def __post_init__(self):
        self.screen_width = self.board.dimension.length * self.cell_px + self.border_px * 2
        self.screen_height = self.board.dimension.height * self.cell_px + self.border_px * 2

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Podscape")
        self.font = pygame.font.SysFont("monospace", 15)

    def draw_grid(self):
        self.screen.fill(self.background_color)
        for row in range(self.board.dimension.height):
            for col in range(self.board.dimension.length):
                cell_rect = pygame.Rect(
                    col * self.cell_px + self.border_px,
                    row * self.cell_px + self.border_px,
                    self.cell_px,
                    self.cell_px
                )
                # Draw filled rectangle
                pygame.draw.rect(self.screen, self.cell_color, cell_rect)
                # Draw an outlined rectangle
                pygame.draw.rect(self.screen, self.background_color, cell_rect, 1)

    def update_display(self):
        self.draw_grid()
        pygame.display.flip()

    def close(self):
        pygame.quit()



