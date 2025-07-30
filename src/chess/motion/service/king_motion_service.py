from typing import List

from chess.geometry.coordinate import Coordinate
from chess.geometry.board import Board
from chess.motion.logic.king_reachable import KingReachable

from chess.motion.service.motion_service import MotionService
from chess.motion.search.king_search_pattern import KingSearchPattern


class KingMotionService(MotionService):
    def __init__(self):
        super().__init__(logic=KingReachable(), search_pattern=KingSearchPattern())


    def _execute_move(self, piece: 'ChessPiece', destination: Coordinate, board: Board):
        origin = piece.current_position()
        if not self.logic.is_reachable(origin, destination):
            raise ValueError(f"{piece.label} cannot reach destination {destination} from origin {origin}.")
        board.capture_square(piece, destination)


    def _perform_exploration(self, piece: 'ChessPiece', board: Board) -> List[Coordinate]:
        return self.search_pattern.search(piece, board)
