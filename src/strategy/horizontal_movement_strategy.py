from typing import TYPE_CHECKING, Optional

from common.direction import Direction
from model.grid_coordinate import GridCoordinate
from strategy.movement_strategy import MovementStrategy


if TYPE_CHECKING:
    from model.board import Board
    from model.vault import HorizontalMover

class HorizontalMovementStrategy(MovementStrategy):
    def move(self, mover: 'HorizontalMover', grid: 'Board', direction: Direction, distance: int = 1) -> bool :

        if mover is None:
            ("[Warning] Mover cannot be None. It cannot move.")
            return False
        if grid is None:
            print("[Warning] Board cannot be None. Cannot move.")
            return False
        if mover.coordinate is None:
            print("[Warning] Mover has no coordinate. Cannot move.")
            return False

        destination_column = mover.coordinate.column
        print("strategy calculated destination column:", destination_column)

        match direction:
            case Direction.LEFT:
                destination_column = mover.coordinate.column - distance
            case Direction.RIGHT:
                destination_column = mover.coordinate.column + distance
            case Direction.UP | Direction.DOWN:
                print(f"[Warning] Invalid direction for horizontal mover: {direction}")
                return False
            case _:
                print(f"[Warning] Invalid direction for horizontal mover: {direction}")
                return False

        if destination_column < 0 or destination_column >= grid.dimension.length:
            print(f"[Warning] Horizontal move out of bounds: {destination_column}")
            return False

        upper_left_destination = GridCoordinate(row=mover.coordinate.row, column=destination_column)

        return grid.move_entity(upper_left_destination, mover) is not None



