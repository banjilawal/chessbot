from dataclasses import dataclass, field

import pygame
from typing import TYPE_CHECKING, Optional, cast

from constants import GameColor
from geometry import GridCoordinate
from grid_entity import GridEntity, Mover, HorizontalMover

if TYPE_CHECKING:
    from board import Board

@dataclass(frozen=True)
class DragState:
    mover: Mover
    original_coordinate: GridCoordinate
    current_coordinate: GridCoordinate
    offset_x: int = 0
    offset_y: int = 0

    def with_updated_position(self, new_coordinate: GridCoordinate) -> 'DragState':
        return DragState(
            mover=self.mover,
            original_coordinate=self.original_coordinate,
            current_coordinate=new_coordinate,
            offset_x=self.offset_x,
            offset_y=self.offset_y
        )

@dataclass
class GameDisplay:
    board: 'Board'
    cell_px: int = 60
    border_px: int = 2
    screen_width: int = 800
    screen_height: int = 800

    active_drags: dict[int, DragState] = field(default_factory=dict)
    is_dragging: bool = False

    def __post_init__(self):
        self.screen_width = self.board.dimension.length * self.cell_px + self.border_px * 2
        self.screen_height = self.board.dimension.height * self.cell_px + self.border_px * 2

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Podscape")
        self.font = pygame.font.SysFont("monospace", 30)

    def draw_grid(self):
        screen_color = GameColor.DARK_GRAY
        self.screen.fill(screen_color)
        for row in range(self.board.dimension.height):
            for col in range(self.board.dimension.length):
                cell_rect = pygame.Rect(
                    col * self.cell_px + self.border_px,
                    row * self.cell_px + self.border_px,
                    self.cell_px,
                    self.cell_px
                )

                cell = self.board.cells[row][col]
                cell_color = screen_color
                if cell.id % 2 == 0:
                    cell_color = GameColor.LIGHT_SAND
                # Draw filled rectangle
                pygame.draw.rect(self.screen, cell_color, cell_rect)
                # Draw an outlined rectangle
                pygame.draw.rect(self.screen, GameColor.BLACK, cell_rect, 1)

    def draw_entities(self):
        for entity in self.board.entities:
            self.draw_entity(entity)

    def draw_entity(self, entity: 'GridEntity'):
        """Draw a single mover on the board"""
        if entity is None:
            print("[Warning] Entity cannot be None. Cannot draw a null mover to the screen.")
            return
        if entity.top_left_coordinate is None:
            print("[Warning] Entity has no top_left_coordinate. Cannot draw an mover without a top_left_coordinate to the screen.")
            return

        # print(f"Drawing mover {mover.mover_id} at top_left_coordinate {mover.top_left_coordinate}")
        # Calculate position and dimensions
        rect = pygame.Rect(
            entity.top_left_coordinate.column * self.cell_px + self.border_px,
            entity.top_left_coordinate.row * self.cell_px + self.border_px,
            entity.dimension.length * self.cell_px - self.border_px,
            entity.dimension.height * self.cell_px - self.border_px
        )
        # Draw the mover (fixed the width parameter)
        pygame.draw.rect(self.screen, self.OLIVE, rect)

        # Draw mover ID
        text_surface = self.font.render(str(entity.id), True, self.BLACK)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def get_entity_at_mouse_position(self, mouse_position: tuple) -> Optional['GridEntity']:
        if mouse_position is None:
            print("[Warning] Mouse position cannot be None. Cannot get an mover at a null position.")
            return None
        coordinate = self.grid_coordinate_at_mouse_position(mouse_position)
        if coordinate is None:
            print("Mouse is outside the game board. Cannot get an mover at a position outside the board.")
            return None
        return self.board.cells[coordinate.row][coordinate.column].occupant

    def handle_mouse_down(self, event: pygame.event.Event):
        if event.button == 1:  # Left mouse button
            entity = self.get_entity_at_mouse_position(event.pos)
            if entity is not None:
                self.start_drag(entity, event.pos)

    def handle_mouse_motion(self, event: pygame.event.Event):
        if self.is_dragging:
            self.update_drag(event.pos)

    def handle_mouse_up(self, event: pygame.event.Event):
        if event.button == 1 and self.is_dragging:  # Left mouse button
            self.end_drag(event.pos)

    def start_drag(self, mover: Mover, mouse_position: tuple[int, int]) -> None:
        self.active_drags[mover.id] = DragState(
            mover=mover,
            original_coordinate=mover.top_left_coordinate,
            current_coordinate=mover.top_left_coordinate,
            offset_x=mouse_position[0] - (mover.top_left_coordinate.column * self.cell_px),
            offset_y=mouse_position[1] - (mover.top_left_coordinate.row * self.cell_px)
        )
        self.is_dragging = True
        print("mover", mover.id, "dragging started at", self.active_drags[mover.id].original_coordinate)

    def update_drag(self, mover_id: int, mouse_position: tuple[int, int]) -> None:
        if not self.is_dragging or mover_id not in
            return
        new_column = (mouse_position[0] - self.active_drags[mover_id].offset_x) // self.cell_px
        new_row = (mouse_position[1] - self.active_drags[mover_id].offset_y) // self.cell_px

        if isinstance(self.active_drags[mover_id].mover, HorizontalMover):
            new_row = self.active_drags[mover_id].original_coordinate.row

        new_coordinate = GridCoordinate(row=new_row, column=new_column)
        self.active_drags[mover_id] = self.active_drags[mover_id].with_updated_position(new_coordinate)
        print("mover", mover_id, "dragging updated to", self.active_drags[mover_id].current_coordinate)

    def end_drag(self, mouse_position: tuple):
        if not self.is_dragging or not self.dragged_entity:
            return

        current_column = (mouse_position[0] - self.border_px) // self.cell_px
        current_row = (mouse_position[1] - self.border_px) // self.cell_px
        destination_coordinate = GridCoordinate(row=self.dragging.original_coordinate.row, column=current_column)

        # Try to move the mover
        if not self.move_handler(self.dragged_entity, destination_coordinate):
            # If move fails, return to original position
            self.dragged_entity.top_left_coordinate = self.original_position

        # Reset is_dragging state
        self.is_dragging = False
        self.drag_offset_x = 0
        self.drag_offset_y = 0
        self.dragged_entity = None
        self.original_position = None

    def move_handler(self, entity: GridEntity, destination_coordinate: GridCoordinate) -> bool:
        if entity is None:
            print("[Warning] Entity cannot be None. Cannot move null mover.")
            return False
        if destination_coordinate is None:
            print(
                "[Warning] Destination top_left_coordinate cannot be None. Cannot move mover without a destination top_left_coordinate.")
            return False
        if self.board is None:
            print("[Warning] Board cannot be None. Cannot move on a nonexistent board.")
            return False
        if entity.top_left_coordinate is None:
            print("[Warning] Entity has no top_left_coordinate. Cannot move an mover without a top_left_coordinate.")
            return False

        # Fix the isinstance check - remove quotes around HorizontalMover
 # Make sure this import is at the top of the file
        if not isinstance(entity, HorizontalMover):
            print(f"[Warning] Entity {entity.id} is not a horizontal mover. Cannot move.")
            return False

        # Remove the first horizontal_mover argument as it's redundant
        return entity.move(self.board, destination_coordinate)

    def move_handler(self, entity: GridEntity, destination_coordinate) -> bool:
        if entity is None:
            print("[Warning] Entity cannot be None. Cannot move null mover.")
            return False
        if destination_coordinate is None:
            print("[Warning] Destination top_left_coordinate cannot be None. Cannot move mover without a destination top_left_coordinate.")

        if self.board is None:
            print("[Warning] Board cannot be None. Cannot move on a nonexistent board.")
            return False
        if entity.top_left_coordinate is None:
            print("[Warning] Entity has no top_left_coordinate. Cannot move an mover without a top_left_coordinate.")
            return False
        if entity.top_left_coordinate is None:
            print("[Warning] Entity has no top_left_coordinate. Cannot move an mover without a top_left_coordinate.")
            return False
        if not isinstance(entity, HorizontalMover):
            print(f"[Warning] Entity {entity.id} is not a horizontal mover. Cannot move.")
            return False

        print(f"Debug: Moving mover {entity.id}")
        print(f"Debug: From top_left_coordinate: row={entity.top_left_coordinate.row}, column={entity.top_left_coordinate.column}")
        print(f"Debug: To top_left_coordinate: row={destination_coordinate.row}, column={destination_coordinate.column}")

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

Abstract Mover etity chas three subclases; HorizontalMover, VeritcalMover and  UniversalMover. For moving in the grid they
either use HorizontalMovementStrategy, VerticalMovementStrategy, or UniversalMovementStrategy. The models and strategies
work on the correctly in Board. I am using pygame to create the GameDisplay. I found out the easiet way for the display
to implement the business rules is with MouseDrag events. With my current handlers I can drag items around. There are
two problems. 1) The most important problem is I want a HorizontalMover instance mosue drag to either restrict movement to
the row. What is probably easier is no matter how they move the mouse a HOrizontalMover('s final position is going to be '
'on the same row but a different column, IN other words if intial_coord(x0, y0) then final_coord(xf, y0). 2) The second
problem is no matter where I drag the entity it ends up back in its original position. I suspec the second problem will
be fixed once I use DragState in the mouseHandlers. Problem 1 is more important. Problem 2 might b easier to solve. Which
should I start with.

The HorizontalMover ais already restricted to movingon the same y-coord through HorizontalMovementStrategy.
The problem is that if the cell contains a HorizontalMover I want to restrict mouse movement to the y-coord
