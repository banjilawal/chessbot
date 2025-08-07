from typing import List

from chess.geometry.board.board import ChessBoard
from chess.geometry.coordinate.coordinate import Coordinate
from chess.motion.knight.service.knight_walk import KnightWalk

from chess.motion.abstract.motion_service import MotionService
from chess.motion.knight.service.knight_search_pattern import KnightSearchPattern


class KnightMotionService(MotionService):
    def __init__(self):
        super().__init__(logic=KnightWalk(), search_pattern=KnightSearchPattern())


    def _execute_move(self, piece: 'ChessPiece', destination: Coordinate, board: ChessBoard):
        origin = piece.current_coordinate()
        if not self.logic.is_walkable(origin, destination):
            raise ValueError(f"B{piece.label} cannot reach destination {destination} from origin {origin}.")

        board.capture_square(piece, destination)


    def _perform_exploration(self, piece: 'ChessPiece', board: ChessBoard) -> List[Coordinate]:
        return self.search_pattern.search(piece, board)
