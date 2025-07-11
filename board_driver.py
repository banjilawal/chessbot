from common.dimension import Dimension
from common.direction import Direction
from model.board import Board
from model.grid_coordinate import GridCoordinate

if __name__ == "__main__":
    board = Board(dimension=Dimension(length=11, height=11))
    for cell in board.cells:
        print(cell)
    print("board dimensions:", board.dimension)
    # print("total empty cells:", len(board.empty_cells()))
    # print("total occupied cells:", len(board.occupied_cells()))

    mover_a = HorizontalMover(mover_id=1, height=1, coordinate=None)
    print("moverA coord:", mover_a.top_left_coordinate)
    board.add_new_entity(GridCoordinate(row=9, column=9), mover_a)
    print("moverA coord", mover_a.top_left_coordinate)

    mover_a_cells = board.get_cells_occupied_by_entity(mover_a)
    print("moverA cells:", mover_a_cells)

    mover_a.move(board, GridCoordinate(row=9, column=12))
    print("moverA coord", mover_a.top_left_coordinate)

    mover_b = HorizontalMover(mover_id=2, height=1)
    print("moverB coord:", mover_b.top_left_coordinate)
    board.add_new_entity(GridCoordinate(row=0, column=0), mover_b)
    print("moverB coord", mover_b.top_left_coordinate)
    mover_b.move(board, GridCoordinate(row=0, column=1))
    print("moverB coord", mover_b.top_left_coordinate)


