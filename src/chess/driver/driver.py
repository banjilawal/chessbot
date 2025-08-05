from typing import List

from chess.motion.abstract.motion_controller import MotionController
from chess.utils.env import DevMode

from chess.factory.grid_builder import GridBuilder
from chess.factory.old.piece_factory import PieceFactory
from chess.factory.old.expired_rank_factory import RankFactoryAntiPattern
from chess.geometry.board import ChessBoard
from chess.geometry.coordinate.coordinate import Coordinate
from chess.motion.bishop.bishop import Bishop


def find_rank(ranks: List[MotionController], rank_name: str) -> MotionController:
    for rank in ranks:
        if rank.name == rank_name:
            return rank
    raise ValueError(f"Rank '{rank_name}' not found in ranks")



def main():
    DevMode._raise_errors = True  # Set to False for production
    board = ChessBoard(grid=GridBuilder.build())
    ranks = RankFactoryAntiPattern.run_factory()

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
        DevMode.raise_or_print(f"Error adding chess_piece to board: {e}")
    print(f"{piece} {piece.current_coordinate()}")

    piece.forward_move_request(destination=Coordinate(row=4, column=4), chess_board=board)
    print(f"{piece} {piece.current_coordinate()}")
    print(f"{piece.label} is exploring the board")
    places = piece.explore_destinations(board=board)
    for place in places:
        print(place)

    rank = find_rank(ranks, "CASTLE")
    print(rank)
    piece = rank.members[0]
    print("New chess_piece:", piece)
    board.add_piece_to_board(piece, Coordinate(row=4, column=7))
    print(piece)
    for coordinate in piece.coordinate_stack:
        print(coordinate)

    castle_places = piece.explore_destinations(board=board)
    for castle_place in castle_places:
        print(castle_place)

    piece.forward_move_request(destination=Coordinate(row=4, column=4), chess_board=board)
    piece.forward_move_request(destination=Coordinate(row=6, column=4), chess_board=board)

    knight_piece = find_rank(ranks, "KNIGHT").members[0]
    print(knight_piece)
    board.add_piece_to_board(knight_piece, Coordinate(row=3, column=3))
    knight_piece.forward_move_request(destination=Coordinate(row=5, column=4), chess_board=board)
    # knight_piece.forward_move_request(destination=Coordinate(row=3, column=6), chess_board=chess_board)
    print(knight_piece)









if __name__ == "__main__":
    main()
