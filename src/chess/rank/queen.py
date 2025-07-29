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


    def move(self, piece: Piece, board: Board, destination: Coordinate):
        origin = piece.current_position()
        if origin is None:
            raise ValueError("Bishop has no known current position.")
        return self.motion.move(self, origin, destination, board)


    def explore(self, piece: Piece, board: Board) -> List[Coordinate]:
        origin = piece.current_position()
        if origin is None:
            return []
        return self.motion.explore(self, origin, board)