from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from geometry import GridCoordinate
from grid_entity import Mover, HorizontalMover

if TYPE_CHECKING:
    from board import Board

class MoveStrategy(ABC):
    @abstractmethod
    def move(self, mover: Mover, board: 'Board', destination_coordinate: GridCoordinate) -> bool:
        pass

class HorizontalMoveStrategy(MoveStrategy):
    def move(self, mover: HorizontalMover, board: Board, destination_coordinate: GridCoordinate) -> bool :

        if mover is None:
            print("[Warning] Mover cannot be None. It cannot move.")
            return False
        if board is None:
            print("[Warning] Board cannot be None. Cannot move.")
            return False
        if mover.top_left_coordinate is None:
            print("[Warning] Mover has no top_left_coordinate. Cannot move.")
            return False
        if destination_coordinate is None:
            print("[Warning] Destination top_left_coordinate cannot be None. Cannot move.")

        if destination_coordinate.column < 0 or destination_coordinate.column >= board.dimension.length:
            print(f"[Warning] Horizontal move out of bounds: {destination_coordinate.column}")
            return False

        if destination_coordinate == mover.top_left_coordinate:
            print("[Warning] Mover is already at destination top_left_coordinate. Cannot move.")
            return False

        if destination_coordinate.row != mover.top_left_coordinate.row:
            print("[Warning] Destination top_left_coordinate is not on the same row as the mover. Cannot move.")
            return False

        destination_column = mover.top_left_coordinate.column
        print("strategy calculated destination column:", destination_column)
        return board.move_entity(destination_coordinate, mover) is not None

class DragStrategy(ABC):
    def move(self, mover: Mover, board: 'Board', destination_coordinate: GridCoordinate) -> bool:
        pass