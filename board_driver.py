from common.dimension import Dimension
from common.direction import Direction
from model.grid import Grid
from model.grid_coordinate import GridCoordinate
from model.vault import HorizontalMover

if __name__ == "__main__":
    board = Grid(dimension=Dimension(length=21, height=21))
    print("board dimensions:", board.dimension)
    # print("total empty cells:", len(board.empty_cells()))
    # print("total occupied cells:", len(board.occupied_cells()))

    mover_a = HorizontalMover(mover_id=1, height=1, coordinate=None)
    print("moverA coord:", mover_a.coordinate)
    board.add_new_entity(GridCoordinate(row=11, column=11), mover_a)
    print("moverA coord", mover_a.coordinate)

    mover_a_cells = board.get_cells_occupied_by_entity(mover_a.id)
    print("moverA cells:", mover_a_cells)

    mover_a.move(board, Direction.RIGHT, 1)


