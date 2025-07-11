from dataclasses import dataclass, field

import pygame
from typing import TYPE_CHECKING, List, Optional

from model.grid_coordinate import GridCoordinate
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

    dragging: bool = False
    drag_offset_x: int = 0
    drag_offset_y: int = 0
    dragged_entity: Optional['GridEntity'] = None
    original_position: Optional[GridCoordinate] = None
    dragged_entity_coordinate: Optional[GridCoordinate] = None

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

    def get_entity_at_mouse_position(self, mouse_position: tuple) -> Optional['GridEntity']:
        if mouse_position is None:
            print("[Warning] Mouse position cannot be None. Cannot get an entity at a null position.")
            return None

        coordinate = self.grid_coordinate_at_mouse_position(mouse_position)
        if coordinate is None:
            print("Mouse is outside the game grid. Cannot get an entity at a position outside the grid.")
            return None

        return self.board.cells[coordinate.row][coordinate.column].occupant

    def handle_mouse_down(self, event: pygame.event.Event):
        if event.button == 1:
            entity = self.get_entity_at_mouse_position(event.pos)
            if entity is not None:
                self.dragging = True
                self.dragged_entity = entity
                self.original_position = entity.coordinate
                self.dragged_entity_coordinate = entity.coordinate




    def update_display(self):
        self.draw_grid()
        self.draw_entities()
        pygame.display.flip()

    def grid_coordinate_at_mouse_position(self, mouse_position: tuple) -> Optional[GridCoordinate]:
        column = mouse_position[0] // self.cell_px
        row = mouse_position[1] // self.cell_px

        if column < 0 or column >= self.board.dimension.length:
            print(f"[Warning] Mouse id outside the game grid at: {column}")
            return None
        if row < 0 or row >= self.board.dimension.height:
            print(f"[Warning] Mouse id outside the game grid at: {row}")
            return None
        return GridCoordinate(row=row, column=column)

    def close(self):
        pygame.quit()



