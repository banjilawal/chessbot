from common.direction import Direction
from model.grid import Grid
from model.grid_coordinate import GridCoordinate
from model.vault import HorizontalMover
from strategy.movement_strategy import MovementStrategy


class HorizontalMovementStrategy(MovementStrategy):
    def move(self, mover: HorizontalMover, grid: Grid, direction: Direction, distance: int = 1):

        destination_column = mover.coordinate.column

        match direction:
            case Direction.LEFT:
                destination_column = mover.coordinate.column - distance
            case Direction.RIGHT:
                destination_column = mover.coordinate.column + distance
            case Direction.UP | Direction.DOWN:
                print(f"[Warning] Invalid direction for horizontal mover: {direction}")
                return
            case _:
                print(f"[Warning] Invalid direction for horizontal mover: {direction}")
                return

        if destination_column < 0 or destination_column >= grid.dimension.length:
            print(f"[Warning] Horizontal move out of bounds: {destination_column}")
            return

        upper_left_destination = GridCoordinate(row=mover.coordinate.row, column=destination_column)
        target_cells = grid.get_cells_in_entity_area(upper_left_destination, mover)
        if target_cells is None:
           print("unexpected null target cells list")
           return
        if len(target_cells) == 0:
            print("no cells are available to move to")
            return

        grid.place_on_grid(upper_left_destination, mover)


