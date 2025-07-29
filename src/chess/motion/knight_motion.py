from typing import List

from chess.geometry.coordinate import Coordinate
from chess.geometry.board import Board
from chess.motion.logic.knight_reachable import KnightReachable

from chess.motion.service.motion_service import MotionService
from chess.motion.search.knight_search_pattern import KnightSearchPattern


class KnightMotionService(MotionService):
    def __init__(self):
        super().__init__(logic=KnightReachable(), search_pattern=KnightSearchPattern())


    def _execute_move(self, piece: 'Piece', destination: Coordinate, board: Board):
        origin = piece.current_position()
        if not self.logic.is_reachable(origin, destination):
            raise ValueError(f"B{piece.label} cannot reach destination {destination} from origin {origin}.")

        board.capture_square(piece, destination)


    def _perform_exploration(self, piece: 'Piece', board: Board) -> List[Coordinate]:
        return self.search_pattern.search(piece, board)
