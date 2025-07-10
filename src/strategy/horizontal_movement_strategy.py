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
        print("strategy extracted coordinate", mover.coordinate, "from mover", mover.id)
        print("strategy calculated destination coordinate", upper_left_destination)

        print("strategy gettint target cells from grid")
        target_cells = grid.get_cells_in_entity_area(upper_left_destination, mover)
        if target_cells is None:
           print("grid sent unexpected null target cells list")
           return None
        if len(target_cells) == 0:
            print("grid sent no cells to move into")
            return None

        count = 1
        for cell in target_cells:
            print("Empty Target Cells")
            if cell.occupant is None:
                print(count, cell)
            if cell.occupant is not None:
                print(count, cell, "occupied by", cell.occupant)
                count += 1

        grid.move_entity(upper_left_destination, mover)
        return upper_left_destination


