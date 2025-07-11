from typing import TYPE_CHECKING, Optional

from common.direction import Direction
from model.grid_coordinate import GridCoordinate
from strategy.movement_strategy import MovementStrategy


if TYPE_CHECKING:
    from model.board import Board
    from model.vault import HorizontalMover

class HorizontalMovementStrategy(MovementStrategy):
    def move(self, mover: 'HorizontalMover', board: 'Board', destination_coordinate: GridCoordinate) -> bool :

        if mover is None:
            ("[Warning] Mover cannot be None. It cannot move.")
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
        #
        # match destination_coordinate:
        #     case Direction.LEFT:
        #         destination_column = mover.top_left_coordinate.column - distance
        #     case Direction.RIGHT:
        #         destination_column = mover.top_left_coordinate.column + distance
        #     case Direction.UP | Direction.DOWN:
        #         print(f"[Warning] Invalid direction for horizontal mover: {destination_coordinate}")
        #         return False
        #     case _:
        #         print(f"[Warning] Invalid direction for horizontal mover: {destination_coordinate}")
        #         return False
        #
        #
        #
        # upper_left_destination = GridCoordinate(row=mover.top_left_coordinate.row, column=destination_column)

        return board.move_entity(destination_coordinate, mover) is not None



