from typing import TYPE_CHECKING, Optional

from common.direction import Direction
from model.grid_coordinate import GridCoordinate
from strategy.movement_strategy import MovementStrategy


if TYPE_CHECKING:
    from model.grid import Grid
    from model.vault import HorizontalMover

class HorizontalMovementStrategy(MovementStrategy):
    def move(self, mover: 'HorizontalMover', grid: 'Grid', direction: Direction, distance: int = 1) -> Optional[GridCoordinate] :

        if mover is None:
            ("[Warning] Mover cannot be None. It cannot move.")
            return
        if grid is None:
            print("[Warning] Grid cannot be None. Cannot move.")
            return
        if mover.coordinate is None:
            print("[Warning] Mover has no coordinate. Cannot move.")
            return

        destination_column = mover.coordinate.column
        print("strategy calculated destination column:", destination_column)

        match direction:
            case Direction.LEFT:
                destination_column = mover.coordinate.column - distance
            case Direction.RIGHT:
                destination_column = mover.coordinate.column + distance
            case Direction.UP | Direction.DOWN:
                print(f"[Warning] Invalid direction for horizontal mover: {direction}")
                return None
            case _:
                print(f"[Warning] Invalid direction for horizontal mover: {direction}")
                return None

        if destination_column < 0 or destination_column >= grid.dimension.length:
            print(f"[Warning] Horizontal move out of bounds: {destination_column}")
            return None

        upper_left_destination = GridCoordinate(row=mover.coordinate.row, column=destination_column)

        grid.move_entity(upper_left_destination, mover.id)
        return upper_left_destination



