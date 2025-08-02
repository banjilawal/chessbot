from typing import List

from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.board import ChessBoard
from chess.motion.logic.bishop_reachable import BishopReachable
from chess.motion.search.bishop_search_pattern import BishopSearchPattern
from chess.motion.service.motion_service import MotionService
from chess.transaction.old_transaction_result import OldTransactionResult


class BishopMotionService(MotionService):
    """MotionService implementation for bishop pieces."""

    def __init__(self):
        super().__init__(logic=BishopReachable(), search_pattern=BishopSearchPattern())

    def _execute_move(self, piece: 'ChessPiece', destination: Coordinate, board: ChessBoard) -> OldTransactionResult:
        origin = piece.current_coordinate()
        if not self.logic.is_reachable(origin, destination):
            raise ValueError(f"{piece.label} cannot reach destination {destination} from origin {origin}.")

        return board.capture_square(piece, destination)

    def _perform_exploration(self, piece: 'ChessPiece', board: ChessBoard) -> List[Coordinate]:
        return self.search_pattern.search(piece, board)