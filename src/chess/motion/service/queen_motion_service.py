from typing import List

from chess.geometry.board.board import ChessBoard
from chess.geometry.coordinate.coordinate import Coordinate
from chess.motion.logic.queen_reachable import QueenReachable

from chess.motion.service.motion_service import MotionService
from chess.motion.search.queen_search_pattern import QueenSearchPattern


class QueenMotionService(MotionService):
    def __init__(self):
        super().__init__(logic=QueenReachable(), search_pattern=QueenSearchPattern())

    def _execute_move(self, piece: 'ChessPiece', destination: Coordinate, board: ChessBoard):
        origin = piece.current_positio()
        if not self.logic.is_reachable(origin, destination):
            raise ValueError(f"{piece.label} cannot reach destination {destination} from origin {origin}.")

        board.capture_square(piece, destination)


    def _perform_exploration(self, piece: 'ChessPiece', board: ChessBoard) -> List[Coordinate]:
        return self.search_pattern.search(piece, board)
