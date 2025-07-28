from typing import List, Optional

from chess.geometry.board import Board
from chess.geometry.coordinate import Coordinate
from chess.geometry.quadrant import Quadrant
from chess.piece.piece import Piece
from chess.game.record.turn_record import TurnRecord
from chess.rank.rank import Rank


class Castle(Rank):

    def __init__(self, name: str, acronym: str, capture_value: int, territories: List['Quadrant']):
        from chess.motion.castle_motion import CastleMotion
        super().__init__(name, acronym, CastleMotion(), capture_value, territories)


    def move(self, piece: 'Piece', board: 'Board', destination: 'Coordinate') -> Optional['TurnRecord']:
        if piece is None:
            raise ValueError("Castle cannot move without a piece.")
        if piece.current_position() is None:
            raise ValueError(f"Castle cannot move {piece} when its coordinate is null. It's not even on the board.")
        if board is None:
            raise ValueError("castle cannot move without a board.")
        if destination is None:
            raise ValueError(f"Castle cannot move {piece.label} without a destination.")

        return self.motion.move(self, piece.current_position(), destination, board)


    def explore(self, piece: Piece, board: Board) -> List[Coordinate]:
        """Find all possible moves for a bishop piece."""
        if piece is None:
            raise ValueError("Bishop cannot explore without a piece.")
        if piece.current_position() is None:
            raise ValueError(f"Bishop cannot explore {piece} when its coordinate is null.")
        if board is None:
            raise ValueError("Bishop cannot explore without a board.")

        return self.motion.explore(self, piece.current_position(), board)