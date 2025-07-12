from dataclasses import dataclass, field

import pygame
from typing import TYPE_CHECKING, Optional, cast, OrderedDict

from colorama.ansi import clear_line

from constants import GameColor, PlacementStatus
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

    active_drags: OrderedDict[int, DragState] = field(default_factory=OrderedDict)
    is_dragging: bool = False

    def __post_init__(self):
        self.screen_width = self.board.dimension.length * self.cell_px + self.border_px * 2
        self.screen_height = self.board.dimension.height * self.cell_px + self.border_px * 2

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Podscape")
        self.font = pygame.font.SysFont("monospace", 30)

    def draw_grid(self):
        screen_color = GameColor.DARK_GRAY_1.value
        self.screen.fill(screen_color)

        cell_color = GameColor.LIGHT_SAND.value
        opposite_cell_color = screen_color

        current_cell_color = cell_color
        previous_cell_color = cell_color
        for row in range(self.board.dimension.height):
            for col in range(self.board.dimension.length):
                cell_rect = pygame.Rect(
                    col * self.cell_px + self.border_px,
                    row * self.cell_px + self.border_px,
                    self.cell_px,
                    self.cell_px
                )

                cell = self.board.cells[row][col]
                current_cell_color = cell_color if (row + col) % 2 == 0 else opposite_cell_color

                pygame.draw.rect(self.screen, current_cell_color, cell_rect)
                # Draw an outlined rectangle
                pygame.draw.rect(self.screen, GameColor.BLACK.value, cell_rect, 1)

    def draw_all_entities(self):
        # First draw board entities
        for entity in self.board.entities:
            self.draw_entity(entity)

        # Then draw any entities being dragged at their current position
        for drag_state in self.active_drags.values():
            rect = pygame.Rect(
                drag_state.current_coordinate.column * self.cell_px + self.border_px,
                drag_state.current_coordinate.row * self.cell_px + self.border_px,
                drag_state.mover.dimension.length * self.cell_px - self.border_px,
                drag_state.mover.dimension.height * self.cell_px - self.border_px
            )
            pygame.draw.rect(self.screen, GameColor.OLIVE.value, rect)
            text_surface = self.font.render(str(drag_state.mover.id), True, GameColor.BLACK.value)
            text_rect = text_surface.get_rect(center=rect.center)
            self.screen.blit(text_surface, text_rect)

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
        pygame.draw.rect(self.screen, GameColor.OLIVE.value, rect)

        # Draw mover ID
        text_surface = self.font.render(str(entity.id), True, GameColor.BLACK.value)
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
        if self.is_dragging and self.active_drags:
            mover_id = list(self.active_drags.keys())[0]
            self.update_drag(mover_id, event.pos)

    def handle_mouse_up(self, event: pygame.event.Event) -> PlacementStatus | None:
        if event.button == 1 and self.is_dragging and self.active_drags:
            mover_id = list(self.active_drags.keys())[0]
            placement_status = self.end_drag(mover_id)
            self.is_dragging = False
            return placement_status
        return PlacementStatus.RELEASED

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
        if not self.is_dragging or mover_id not in self.active_drags:
            return
        new_column = (mouse_position[0] - self.active_drags[mover_id].offset_x) // self.cell_px
        new_row = (mouse_position[1] - self.active_drags[mover_id].offset_y) // self.cell_px

        if isinstance(self.active_drags[mover_id].mover, HorizontalMover):
            new_row = self.active_drags[mover_id].original_coordinate.row

        new_coordinate = GridCoordinate(row=new_row, column=new_column)
        self.active_drags[mover_id] = self.active_drags[mover_id].with_updated_position(new_coordinate)
        print("mover", mover_id, "dragging updated to", self.active_drags[mover_id].current_coordinate)

    def end_drag(self, mover_id: int) -> PlacementStatus:
        if not self.is_dragging or mover_id not in self.active_drags:
            return PlacementStatus.RELEASED

        drag_state = self.active_drags.pop(mover_id)
        if drag_state.current_coordinate == drag_state.original_coordinate:
            return PlacementStatus.RELEASED

        moved_entity = self.board.move_entity(entity=drag_state.mover, upper_left_destination= drag_state.current_coordinate)
        if moved_entity is not None:
            return PlacementStatus.PLACED
        else:
            drag_state.mover.coordinate = drag_state.original_coordinate
            return PlacementStatus.BLOCK

    def move_handler(self, entity: GridEntity, destination_coordinate: GridCoordinate) -> bool:
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
        self.draw_all_entities()
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