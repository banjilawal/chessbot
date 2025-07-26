from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.motion.search import SearchPattern
from chess.motion.walk import linear_walk, diagonal_walk


class KnightSearchPattern(SearchPattern):

    @staticmethod
    def search(piece: Knight, board: Board) -> list[Coordinate]:
        if not SearchPattern.check_basic_conditions(piece, board):
            return []

        origin = piece.current_position()
        destinations = []
        northern_coordinate = linear_walk(
            origin,
            Quadrant.N.x_delta,
            Quadrant.N.y_delta,
            board,
            2
        )[0]
        southern_coordinate = linear_walk(
            origin,
            Quadrant.S.x_delta,
            Quadrant.S.y_delta,
            board,
            2
        )[0]

        for q in [Quadrant.NE, Quadrant.NW]:
            destinations.extend(diagonal_walk(northern_coordinate, q.x_delta, q.y_delta, board, 1))

        for q in [Quadrant.SE, Quadrant.SW]:
            destinations.extend(diagonal_walk(southern_coordinate, q.x_delta, q.y_delta, board, 1))
        return destinations
