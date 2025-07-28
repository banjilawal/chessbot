from typing import List, Optional

from chess.rank.rank import Rank
from chess.geometry.board import Board
from chess.geometry.coordinate import Coordinate
from chess.geometry.quadrant import Quadrant

from chess.piece.piece import Piece
from chess.game.record.turn_record import TurnRecord



class Bishop(Rank):
    """Bishop rank implementation that inherits from Rank."""

    def __init__(self, name: str, acronym: str, capture_value: int, territories: List['Quadrant']):
        from chess.motion.bishop_motion import BishopMotion
        super().__init__(name, acronym, BishopMotion(), capture_value, territories)

    # def __init__(self, name: str, acronym: str, capture_value: int, territories: List['Quadrant']):
    #     # Initialize parent class and set motion
    #     self.name = name
    #     self.acronym = acronym
    #     self.capture_value = capture_value
    #     self.territories = territories
    #     # Assuming motion is set in the parent Rank class
    #     # Based on your original code, motion is likely set via super().__init__()
    #     from chess.motion.bishop_motion import BishopMotion
    #     self.motion = BishopMotion()

    def move(self, piece: 'Piece', board: 'Board', destination: 'Coordinate') -> Optional['TurnRecord']:
        """Move a bishop piece to the specified destination."""
        if piece is None:
            raise ValueError("Bishop cannot move without a piece.")
        if piece.current_position() is None:
            raise ValueError(f"Bishop cannot move {piece} when its coordinate is null. It's not even on the board.")
        if board is None:
            raise ValueError("Bishop cannot move without a board.")
        if destination is None:
            raise ValueError(f"Bishop cannot move {piece.label} without a destination.")

        origin = piece.current_position()
        print(f"{piece.label} starting move from {origin} to {destination}")

        # Call motion.move() with keyword arguments to ensure proper parameter alignment
        return self.motion.move(rank=self, origin=origin, destination=destination, board=board)

    def explore(self, piece: 'Piece', board: 'Board') -> List['Coordinate']:
        """Find all possible moves for a bishop piece."""
        if piece is None:
            raise ValueError("Bishop cannot explore without a piece.")
        if piece.current_position() is None:
            raise ValueError(f"Bishop cannot explore {piece} when its coordinate is null.")
        if board is None:
            raise ValueError("Bishop cannot explore without a board.")

        origin = piece.current_position()
        return self.motion.explore(rank=self, origin=origin, board=board)