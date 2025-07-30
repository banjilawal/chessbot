from typing import List

from chess.geometry.coordinate import Coordinate
from chess.geometry.board import ChessBoard
from chess.motion.logic.knight_reachable import KnightReachable

from chess.motion.service.motion_service import MotionService
from chess.motion.search.knight_search_pattern import KnightSearchPattern
from chess.transaction.transaction_result import TransactionResult


class KnightMotionService(MotionService):
    def __init__(self):
        super().__init__(logic=KnightReachable(), search_pattern=KnightSearchPattern())


    def _execute_move(self, piece: 'ChessPiece', destination: Coordinate, board: ChessBoard) -> TransactionResult :
        origin = piece.current_coordinate()
        if not self.logic.is_reachable(origin, destination):
            raise ValueError(f"B{piece.label} cannot reach destination {destination} from origin {origin}.")

        board.capture_square(piece, destination)


    def _perform_exploration(self, piece: 'ChessPiece', board: ChessBoard) -> List[Coordinate]:
        return self.search_pattern.search(piece, board)
