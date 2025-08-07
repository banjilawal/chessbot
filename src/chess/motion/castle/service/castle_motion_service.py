from typing import List

from chess.geometry.board.board import ChessBoard
from chess.geometry.coordinate.coordinate import Coordinate
from chess.motion.castle.service.castle_walk import CastleWalk

from chess.motion.interfaces.motion_service import MotionService
from chess.motion.castle.service.castle_search_pattern import CastleMoveGenerator


class CastleMotionService(MotionService):

    """MotionService implementation for bishop pieces."""

    def __init__(self):
        super().__init__(logic=CastleWalk(), search_pattern=CastleMoveGenerator())


    def _execute_move(self, piece: 'ChessPiece', destination: Coordinate, board: ChessBoard):
        origin = piece.current_coordinate()
        if not self.logic.is_walkable(origin, destination):
            raise ValueError(f"{piece.label} cannot reach destination {destination} from origin {origin}.")

        board.capture_square(piece, destination)


    def _perform_exploration(self, piece: 'ChessPiece', board: ChessBoard) -> List[Coordinate]:
        return self.search_pattern.search(piece, board)
