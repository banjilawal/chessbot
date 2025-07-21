from entity_factory import EntityFactory
from geometry import Dimension, GridCoordinate
from board import Board

from grid_entity import HorizontalMover, VerticalMover, BrickPallet
from id_factory import id_factory

if __name__ == "__main__":
    board = Board(dimension=Dimension(length=21, height=21))
    for cell in board.cells:
        print(cell)
    print("board dimensions:", board.dimension)
    # print("total empty cells:", len(board.empty_cells()))
    # print("total occupied cells:", len(board.occupied_cells()))

    brick_pallet = BrickPallet(dimension=Dimension(length=10, height=5), top_left_coordinate=None)
    board.add_new_entity(GridCoordinate(row=0, column=0), brick_pallet)
    print("brick pallet coord:", brick_pallet.top_left_coordinate)

    horizontal_mover_a = HorizontalMover(mover_id=id_factory.mover_id(), height=1, top_left_coordinate=None)
    print("moverA coord:", horizontal_mover_a.top_left_coordinate)
    board.add_new_entity(GridCoordinate(row=11, column=13), horizontal_mover_a)
    print("moverA coord", horizontal_mover_a.top_left_coordinate)

    mover_a_cells = board.get_cells_occupied_by_entity(horizontal_mover_a)
    print("moverA cells:", mover_a_cells)

    horizontal_mover_a.move(board, GridCoordinate(row=12, column=8))
    print("moverA coord", horizontal_mover_a.top_left_coordinate)

    horizontal_mover_b = HorizontalMover(mover_id=id_factory.mover_id(), height=1)
    print("moverB coord:", horizontal_mover_b.top_left_coordinate)
    board.add_new_entity(GridCoordinate(row=0, column=13), horizontal_mover_b)
    print("moverB coord", horizontal_mover_b.top_left_coordinate)
    horizontal_mover_b.move(board, GridCoordinate(row=0, column=15))
    print("moverB coord", horizontal_mover_b.top_left_coordinate)

    vertical_mover_u = VerticalMover(mover_id=id_factory.mover_id(), length=4)
    print("moverU coord:", vertical_mover_u.top_left_coordinate)
    board.add_new_entity(GridCoordinate(row=6, column=15), vertical_mover_u)
    print("moverU coord:", vertical_mover_u.top_left_coordinate)
    vertical_mover_u.move(board, GridCoordinate(row=7, column=6))
    print("moverU coord:", vertical_mover_u.top_left_coordinate)
    vertical_mover_u.move(board, GridCoordinate(row=9, column=4))
    print("moverU coord:", vertical_mover_u.top_left_coordinate)

    vertical_mover_v = VerticalMover(mover_id=id_factory.mover_id(), length=2)
    print("moverV coord:", vertical_mover_v.top_left_coordinate)
    board.add_new_entity(GridCoordinate(row=7, column=6), vertical_mover_v)
    print("moverV coord:", vertical_mover_v.top_left_coordinate)

    board.move_entity(GridCoordinate(row=2, column=6), vertical_mover_v)
    print("moverV coord:", vertical_mover_v.top_left_coordinate)

    # brick_pallet = BrickPallet(dimension=Dimension(length=10, height=5), top_left_coordinate=None)
    # board.add_new_entity(GridCoordinate(row=10, column=10), brick_pallet)
    # print("brick pallet coord:", brick_pallet.top_left_coordinate)


