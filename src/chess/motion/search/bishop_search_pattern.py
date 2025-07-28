from chess.geometry.board import Board
from chess.geometry.coordinate import Coordinate

from chess.motion.search.search_pattern import SearchPattern



class BishopSearchPattern(SearchPattern):

    @staticmethod
    def search(origin: Coordinate, board: Board) -> list[Coordinate]:
        if not SearchPattern.check_basic_conditions(origin, board):
            return []

        destinations = []
        for quadrant in [Quadrant.NE, Quadrant.SW, Quadrant.SE, Quadrant.NW]:
            destinations.extend(diagonal_walk(origin, quadrant.x_delta, quadrant.y_delta, board))
        return destinations






