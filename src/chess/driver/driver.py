from typing import List

from chess.geometry.coordinate import Coordinate
from chess.geometry.row import Row
from chess.geometry.column import Column
from chess.rank.rank import Rank
from chess.utils.env import DevMode


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


def find_rank(ranks: List[Rank], rank_name: str) -> Rank:
    for rank in ranks:
        if rank.name == rank_name:
            return rank
    raise ValueError(f"Rank '{rank_name}' not found in ranks")



def main():
    DevMode._raise_errors = True  # Set to False for production
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
    try:
        board.add_piece_to_board(piece, Coordinate(row=1, column=1))
    except ValueError as e:
        DevMode.raise_or_print(f"Error adding piece to board: {e}")
    print(f"{piece} {piece.current_position()}")

    piece.move(destination=Coordinate(row=4, column=4), board=board)
    print(f"{piece} {piece.current_position()}")
    print(f"{piece.label} is exploring the board")
    places = piece.explore_destinations(board=board)
    for place in places:
        print(place)

    rank = find_rank(ranks, "CASTLE")
    print(rank)
    piece = rank.members[0]
    print(piece)
    board.add_piece_to_board(piece, Coordinate(row=4, column=7))
    print(piece)









if __name__ == "__main__":
    main()
