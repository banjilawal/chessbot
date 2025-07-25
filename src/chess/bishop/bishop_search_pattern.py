from typing import Optional

from chess.board.board import Board
from chess.common.geometry import Coordinate

from chess.motion.quadrant import Quadrant
from chess.motion.search_pattern import SearchPattern
from chess.motion.walks import diagonal_walk



class BishopSearchPattern(SearchPattern):

    @staticmethod
    def search(origin: Coordinate, board: Board) -> list[Coordinate]:
        if not SearchPattern.check_basic_conditions(origin, board):
            return []

        destinations = []
        for quadrant in [Quadrant.NE, Quadrant.SW, Quadrant.SE, Quadrant.NW]:
            destinations.extend(diagonal_walk(origin, quadrant.x_delta, quadrant.y_delta, board))
        return destinations






