from typing import Optional

from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.common.promotable import Pawn
from chess.motion.search_pattern import SearchPattern


class PawnSearchPattern(SearchPattern):

    @staticmethod
    def search(piece: Pawn, board: Board, ) -> list[Coordinate]:
        if not SearchPattern.check_basic_conditions(piece, board):
            return []

        origin = piece.current_position()
        destinations = []
        next_point = origin.shift(0, 1)
        if board.coordinate_is_valid(next_point):
            destinations.append(next_point)
        return destinations
