from typing import Optional, List

from chess.geometry.coordinate import Coordinate
from chess.geometry.board import Board
from chess.game.record.turn_record import TurnRecord
from chess.motion.logic.bishop_reachable import BishopReachable
from chess.motion.search.bishop_search_pattern import BishopSearchPattern
from chess.motion.motion import Motion
from chess.rank.rank import Rank


class BishopMotion(Motion):
    """Motion implementation for bishop pieces."""

    def __init__(self):
        super().__init__(logic=BishopReachable(), search_pattern=BishopSearchPattern())

    def _execute_move(self, piece: 'Piece', destination: Coordinate, board: Board):
        origin = piece.current_position()
        if not self.logic.is_reachable(origin, destination):
            raise ValueError(f"{piece.label} cannot reach destination {destination} from origin {origin}.")

        board.capture_square(piece, destination)

    def _perform_exploration(self, piece: 'Piece', board: Board) -> List[Coordinate]:
        return self.search_pattern.search(piece, board)
#
#
# class Bishop:
#     """Bishop rank implementation that inherits from Rank."""
#
#     def __init__(self, name: str, acronym: str, capture_value: int, territories: List['Quadrant']):
#         # Initialize parent class and set motion
#         self.name = name
#         self.acronym = acronym
#         self.capture_value = capture_value
#         self.territories = territories
#         # Assuming motion is set in the parent Rank class
#         # Based on your original code, motion is likely set via super().__init__()
#         from chess.motion.bishop_motion import BishopMotion
#         self.motion = BishopMotion()
#
#     def move(self, piece: 'Piece', board: 'Board', destination: 'Coordinate') -> Optional['TurnRecord']:
#         """Move a bishop piece to the specified destination."""
#         if piece is None:
#             raise ValueError("Bishop cannot move without a piece.")
#         if piece.current_position() is None:
#             raise ValueError(f"Bishop cannot move {piece} when its coordinate is null. It's not even on the board.")
#         if board is None:
#             raise ValueError("Bishop cannot move without a board.")
#         if destination is None:
#             raise ValueError(f"Bishop cannot move {piece.label} without a destination.")
#
#         origin = piece.current_position()
#         print(f"{piece.label} starting move from {origin} to {destination}")
#
#         # Call motion.move() with self as the rank parameter, but motion is an instance
#         return self.motion.move(self, origin, destination, board)
#
#     def explore(self, piece: 'Piece', board: 'Board') -> List['Coordinate']:
#         """Find all possible moves for a bishop piece."""
#         if piece is None:
#             raise ValueError("Bishop cannot explore without a piece.")
#         if piece.current_position() is None:
#             raise ValueError(f"Bishop cannot explore {piece} when its coordinate is null.")
#         if board is None:
#             raise ValueError("Bishop cannot explore without a board.")
#
#         origin = piece.current_position()
#         return self.motion.explore(self, origin, board)