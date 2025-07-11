from dataclasses import dataclass, field

import pygame
from typing import TYPE_CHECKING, List
from model.grid_entity import GridEntity

if TYPE_CHECKING:
    from model.board import Board
    from model.vault import HorizontalMover

@dataclass
class Visualizer:

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    CREAM = (255, 253, 208)
    KHAKI = (240, 230, 140)
    LIGHT_GRAY = (211, 211, 211)
    DARK_GRAY = (169, 169, 169)
    SALMON = (250, 128, 114)
    BLUE = (0, 0, 255)
    BLUE_GRAY = (102, 153, 204)
    PINK = (255, 192, 203)
    GINGER = (176, 101, 0)
    CERULEAN = (0, 123, 167)
    OLIVE = (128, 128, 0)
    LIGHT_SAND = (245, 222, 179)
    SAND = (194, 178, 128)

    board: 'Board'

    cell_px: int = 60
    border_px: int = 2
    screen_width: int = 800
    screen_height: int = 800

    def __post_init__(self):
        self.screen_width = self.board.dimension.length * self.cell_px + self.border_px * 2
        self.screen_height = self.board.dimension.height * self.cell_px + self.border_px * 2

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Podscape")
        self.font = pygame.font.SysFont("monospace", 30)

    def draw_grid(self):
        self.screen.fill(self.DARK_GRAY)
        for row in range(self.board.dimension.height):
            for col in range(self.board.dimension.length):
                cell_rect = pygame.Rect(
                    col * self.cell_px + self.border_px,
                    row * self.cell_px + self.border_px,
                    self.cell_px,
                    self.cell_px
                )
                fill_color = self.DARK_GRAY

                cell = self.board.cells[row][col]
                if cell.id % 2 == 0:
                    fill_color = self.LIGHT_SAND

                # Draw filled rectangle
                pygame.draw.rect(self.screen, fill_color, cell_rect)
                # Draw an outlined rectangle
                pygame.draw.rect(self.screen, self.BLACK, cell_rect, 1)

    def draw_entities(self):
        for entity in self.board.entities:
            self.draw_entity(entity)

    def draw_entity(self, entity: 'GridEntity'):
        """Draw a single entity on the board"""
        if entity is None:
            print("[Warning] Entity cannot be None. Cannot draw a null entity to the screen.")
            return
        if entity.coordinate is None:
            print("[Warning] Entity has no coordinate. Cannot draw an entity without a coordinate to the screen.")
            return

        print(f"Drawing entity {entity.id} at coordinate {entity.coordinate}")

        # Calculate position and dimensions
        rect = pygame.Rect(
            entity.coordinate.column * self.cell_px + self.border_px,
            entity.coordinate.row * self.cell_px + self.border_px,
            entity.dimension.length * self.cell_px - self.border_px,
            entity.dimension.height * self.cell_px - self.border_px
        )

        # Draw the entity (fixed the width parameter)
        pygame.draw.rect(self.screen, self.OLIVE, rect)

        # Draw entity ID
        text_surface = self.font.render(str(entity.id), True, self.BLACK)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def update_display(self):
        self.draw_grid()
        self.draw_entities()
        pygame.display.flip()

    def close(self):
        pygame.quit()



