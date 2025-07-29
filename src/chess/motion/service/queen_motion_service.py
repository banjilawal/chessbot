from typing import List

from chess.geometry.coordinate import Coordinate
from chess.geometry.board import Board
from chess.motion.logic.queen_reachable import QueenReachable

from chess.motion.service.motion_service import MotionService
from chess.motion.search.queen_search_pattern import QueenSearchPattern


class QueenMotionService(MotionService):
    def __init__(self):
        super().__init__(logic=QueenReachable(), search_pattern=QueenSearchPattern())

    def _execute_move(self, piece: 'Piece', destination: Coordinate, board: Board):
        origin = piece.current_positio()
        if not self.logic.is_reachable(origin, destination):
            raise ValueError(f"{piece.label} cannot reach destination {destination} from origin {origin}.")

        board.capture_square(piece, destination)


    def _perform_exploration(self, piece: 'Piece', board: Board) -> List[Coordinate]:
        return self.search_pattern.search(piece, board)
