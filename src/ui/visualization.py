from dataclasses import dataclass, field

import pygame
from typing import TYPE_CHECKING, List, Optional, cast

from model.grid_coordinate import GridCoordinate
from model.grid_entity import GridEntity
from model.vault import HorizontalMover

if TYPE_CHECKING:
    from model.board import Board

@dataclass
class VisualizerColor:
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

@dataclass(frozen=True)
class DragState:
    entity: Optional[GridEntity]
    original_coord: Optional[GridCoordinate]
    current_coord: Optional[GridCoordinate]
    offset_x: int = 0
    offset_y: int = 0

    def with_updated_position(self, new_coordinate: GridCoordinate) -> 'DragState':
        return DragState(
            entity=self.entity,
            original_coord=self.original_coord,
            current_coord=new_coordinate,
            offset_x=self.offset_x,
            offset_y=self.offset_y
        )





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

    dragging: DragState = field(default_factory=lambda: DragState(entity=None, original_coord=None, offset_x=0, offset_y=0))

    is_dragging: bool = False
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

        # print(f"Drawing entity {entity.id} at coordinate {entity.coordinate}")

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
            print("Mouse is outside the game board. Cannot get an entity at a position outside the board.")
            return None

        return self.board.cells[coordinate.row][coordinate.column].occupant

    def handle_mouse_down(self, event: pygame.event.Event):
        if event.button == 1:  # Left mouse button
            entity = self.get_entity_at_mouse_position(event.pos)
            if entity is not None:
                self.start_dragging(entity, event.pos)

    def handle_mouse_motion(self, event: pygame.event.Event):
        if self.is_dragging:
            self.update_drag(event.pos)

    def handle_mouse_up(self, event: pygame.event.Event):
        if event.button == 1 and self.is_dragging:  # Left mouse button
            self.end_dragging(event.pos)

    def start_dragging(self, entity: GridEntity, mouse_position: tuple):
        self.is_dragging = True
        self.dragged_entity = entity
        self.original_position = entity.coordinate

        self.dragging = DragState(
            entity=entity,
            original_coord=entity.coordinate,  # Store the original coordinate
            offset_x=mouse_position[0] - (entity.coordinate.column * self.cell_px + self.border_px),
            offset_y=mouse_position[1] - (entity.coordinate.row * self.cell_px + self.border_px)
        )

        entity_screen_x = entity.coordinate.column * self.cell_px + self.border_px
        entity_screen_y = entity.coordinate.row * self.cell_px + self.border_px
        self.drag_offset_x = mouse_position[0] - entity_screen_x
        self.drag_offset_y = mouse_position[1] - entity_screen_y
        print(
            f"Starting dragging entity {entity.id} at {entity.coordinate} with offset ({self.drag_offset_x}, {self.drag_offset_y})")

    def update_drag(self, mouse_position: tuple):
        if not self.is_dragging or not self.dragged_entity:
            return

        # Update the visual position of the entity during drag
        current_column = (mouse_position[0] - self.border_px - self.drag_offset_x) // self.cell_px
        current_row = (mouse_position[1] - self.border_px - self.drag_offset_y) // self.cell_px

        # Temporarily update the coordinate for visual feedback
        self.dragged_entity.coordinate = GridCoordinate(row=current_row, column=current_column)

    def end_dragging(self, mouse_position: tuple):
        if not self.is_dragging or not self.dragged_entity:
            return

        current_column = (mouse_position[0] - self.border_px) // self.cell_px
        current_row = (mouse_position[1] - self.border_px) // self.cell_px
        destination_coordinate = GridCoordinate(row=self.dragging.original_coord.row, column=current_column)

        # Try to move the entity
        if not self.move_handler(self.dragged_entity, destination_coordinate):
            # If move fails, return to original position
            self.dragged_entity.coordinate = self.original_position

        # Reset is_dragging state
        self.is_dragging = False
        self.drag_offset_x = 0
        self.drag_offset_y = 0
        self.dragged_entity = None
        self.original_position = None

    def move_handler(self, entity: GridEntity, destination_coordinate: GridCoordinate) -> bool:
        if entity is None:
            print("[Warning] Entity cannot be None. Cannot move null entity.")
            return False
        if destination_coordinate is None:
            print(
                "[Warning] Destination coordinate cannot be None. Cannot move entity without a destination coordinate.")
            return False
        if self.board is None:
            print("[Warning] Board cannot be None. Cannot move on a nonexistent board.")
            return False
        if entity.coordinate is None:
            print("[Warning] Entity has no coordinate. Cannot move an entity without a coordinate.")
            return False

        # Fix the isinstance check - remove quotes around HorizontalMover
        from model.vault import HorizontalMover  # Make sure this import is at the top of the file
        if not isinstance(entity, HorizontalMover):
            print(f"[Warning] Entity {entity.id} is not a horizontal mover. Cannot move.")
            return False

        # Remove the first horizontal_mover argument as it's redundant
        return entity.move(self.board, destination_coordinate)

    def move_handler(self, entity: GridEntity, destination_coordinate) -> bool:
        if entity is None:
            print("[Warning] Entity cannot be None. Cannot move null entity.")
            return False
        if destination_coordinate is None:
            print("[Warning] Destination coordinate cannot be None. Cannot move entity without a destination coordinate.")

        if self.board is None:
            print("[Warning] Board cannot be None. Cannot move on a nonexistent board.")
            return False
        if entity.coordinate is None:
            print("[Warning] Entity has no coordinate. Cannot move an entity without a coordinate.")
            return False
        if entity.coordinate is None:
            print("[Warning] Entity has no coordinate. Cannot move an entity without a coordinate.")
            return False
        if not isinstance(entity, HorizontalMover):
            print(f"[Warning] Entity {entity.id} is not a horizontal mover. Cannot move.")
            return False

        print(f"Debug: Moving entity {entity.id}")
        print(f"Debug: From coordinate: row={entity.coordinate.row}, column={entity.coordinate.column}")
        print(f"Debug: To coordinate: row={destination_coordinate.row}, column={destination_coordinate.column}")

        horizontal_mover = cast(HorizontalMover, entity)
        move_result = horizontal_mover.move(self.board, destination_coordinate)
        if not move_result:
            print(f"[Warning] Move failed - Movement might be restricted to top row only")
        return move_result

    def update_display(self):
        self.draw_grid()
        self.draw_entities()
        pygame.display.flip()

    def grid_coordinate_at_mouse_position(self, mouse_position: tuple) -> Optional[GridCoordinate]:
        column = mouse_position[0] // self.cell_px
        row = mouse_position[1] // self.cell_px

        if column < 0 or column >= self.board.dimension.length:
            print(f"[Warning] Mouse id outside the game board at: {column}")
            return None
        if row < 0 or row >= self.board.dimension.height:
            print(f"[Warning] Mouse id outside the game board at: {row}")
            return None
        return GridCoordinate(row=row, column=column)

    def close(self):
        pygame.quit()



