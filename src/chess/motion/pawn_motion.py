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

    def _perform_move(self, piece: 'Piece', destination: Coordinate, board: Board):
        origin = piece.current_positio()
        if not self.logic.is_reachable(origin, destination):
            raise ValueError(f"{piece.label} cannot reach destination {destination} from origin {origin}.")

        board.capture_square(piece, destination)


    def _perform_exploration(self, piece: 'Piece', board: Board) -> List[Coordinate]:
        return self.search_pattern.search(piece, board)
