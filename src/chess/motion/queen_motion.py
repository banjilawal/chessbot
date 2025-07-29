from typing import Optional, List

from chess.geometry.coordinate import Coordinate
from chess.geometry.board import Board
from chess.game.record.turn_record import TurnRecord
from chess.motion.logic.queen_reachable import QueenReachable

from chess.motion.motion import Motion
from chess.motion.search.queen_search_pattern import QueenSearchPattern
from chess.rank.rank import Rank


class QueenMotion(Motion):
    def __init__(self):
        super().__init__(logic=QueenReachable(), search_pattern=QueenSearchPattern())

    def _perform_move(self, piece: 'Piece', destination: Coordinate, board: Board):
        origin = piece.current_positio()
        if not self.logic.is_reachable(origin, destination):
            raise ValueError(f"{piece.label} cannot reach destination {destination} from origin {origin}.")

        board.capture_square(piece, destination)


    def _perform_exploration(
        self,
        rank: Rank,
        origin: Coordinate,
        board: Board
    ) -> List[Coordinate]:
        return self.search_pattern.search(rank, origin, board)
