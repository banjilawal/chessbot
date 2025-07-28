from typing import Optional, List

from chess.geometry.coordinate import Coordinate
from chess.geometry.board import Board
from chess.game.record.turn_record import TurnRecord

from chess.motion.logic.pawn_reachable import PawnReachable
from chess.motion.motion import Motion
from chess.motion.search.pawn_search_pattern import PawnSearchPattern
from chess.rank.rank import Rank


class PawnMotion(Motion):
    def __init__(self):
        super().__init__(logic=PawnReachable(), search_pattern=PawnSearchPattern())


    def _perform_move(
        self,
        rank: Rank,
        origin: Coordinate,
        destination: Coordinate,
        board: Board
    ) -> Optional[TurnRecord]:

        if not self.logic.is_reachable(origin, destination):
            raise ValueError(f"Bishop cannot reach destination {destination} from origin {origin}.")

        # Get the piece at the origin
        piece = board.get_piece_by_coordinate(origin)
        if piece is None:
            raise ValueError("No piece found at origin to move.")

        return board.capture_square(piece, destination)


    def _perform_exploration(
        self,
        rank: Rank,
        origin: Coordinate,
        board: Board
    ) -> List[Coordinate]:
        return self.search_pattern.search(rank, origin, board)
