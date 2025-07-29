from typing import Optional, List

from chess.geometry.coordinate import Coordinate
from chess.geometry.board import Board
from chess.game.record.turn_record import TurnRecord
from chess.motion.logic.castle_reachable import CastleReachable

from chess.motion.motion_service import Motion
from chess.motion.search.castle_search_pattern import CastleSearchPattern
from chess.rank.rank import Rank


class CastleMotion(Motion):

    """Motion implementation for bishop pieces."""

    def __init__(self):
        super().__init__(logic=CastleReachable(), search_pattern=CastleSearchPattern())


    def _execute_move(self, piece: 'Piece', destination: Coordinate, board: Board):
        origin = piece.current_position()
        if not self.logic.is_reachable(origin, destination):
            raise ValueError(f"{piece.label} cannot reach destination {destination} from origin {origin}.")

        board.capture_square(piece, destination)


    def _perform_exploration(self, piece: 'Piece', board: Board) -> List[Coordinate]:
        return self.search_pattern.search(piece, board)
