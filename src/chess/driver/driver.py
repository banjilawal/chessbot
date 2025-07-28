from chess.geometry.coordinate import Coordinate
from chess.geometry.row import Row
from chess.geometry.column import Column


def make_coordinate(coordinate_id: int, row_number: int, column_number: int) -> Coordinate:
    """
    Builds a Coordinate object using chess-style row and column indexes.

    :param coordinate_id: Unique identifier for the coordinate.
    :param row_number: 1-based row index (1 to 8 for a standard board).
    :param column_number: 1-based column index (1 = A, 2 = B, ..., 8 = H).
    :return: Coordinate instance.
    """
    if row_number < 1 or row_number > 8:
        raise ValueError("Row number must be between 1 and 8")
    if column_number < 1 or column_number > 8:
        raise ValueError("Column number must be between 1 and 8")

    row = Row(row_number)
    column_letter = chr(ord("A") + column_number - 1)
    column = Column(column_number, column_letter)
    return Coordinate(coordinate_id=coordinate_id, row=row, column=column)


from chess.factory.grid_builder import GridBuilder
from chess.factory.piece_factory import PieceFactory
from chess.factory.rank_factory import RankFactory
from chess.geometry.board import Board
from chess.geometry.coordinate import Coordinate
from chess.rank.bishop import Bishop




def main():

    board = Board(grid=GridBuilder.build())
    ranks = RankFactory.run_factory()

    pieces = PieceFactory.run_factory(ranks)
    for piece in pieces:
        if isinstance(piece.rank, Bishop):
            print(piece)
            print()

    for rank in ranks:
        print(rank)
    piece = pieces[22]
    print(board)
    board.add_chess_piece_to_board(piece, Coordinate(coordinate_id=1, row=1, column=1) )

    print(f"{piece} {piece.current_position()}")
    print(Coordinate(coordinate_id=1, row=1, column=1))








if __name__ == "__main__":
    main()
