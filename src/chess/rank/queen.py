from typing import List, Optional

from chess.geometry.board import Board
from chess.geometry.coordinate import Coordinate
from chess.geometry.quadrant import Quadrant

from chess.piece.piece import Piece
from chess.game.record.turn_record import TurnRecord
from chess.rank.rank import Rank


class Queen(Rank):

    def __init__(self, name: str, acronym: str, capture_value: int, territories: List[Quadrant]):

        from chess.motion.queen_motion import QueenMotion

        super().__init__(name, acronym, QueenMotion, capture_value, territories)

    #
    # def move(self, piece: Piece, board: 'Board', destination: 'Coordinate'):
    #     """Move a piece to the specified destination."""
    #     if piece is None:
    #         raise ValueError("Cannot move a null piece")
    #     if piece.current_position() is None:
    #         raise ValueError(f"{piece.label} when its coordinate is null. It's not even on the board.")
    #     if board is None:
    #         raise ValueError(f"{piece.label} cannot move without a board.")
    #     if destination is None:
    #         raise ValueError(f"{piece.label} without a destination.")
    #
    #     origin = piece.current_position()
    #     print(f"{piece.label} starting move from {origin} to {destination}")
    #
    #     # Call motion.move() with keyword arguments to ensure proper parameter alignment
    #     self.motion.move(piece, destination, board)
    #
    #
    # def explore(self, piece: Piece, board: Board) -> List[Coordinate]:
    #     origin = piece.current_position()
    #     if origin is None:
    #         return []
    #     return self.motion.explore(self, origin, board)