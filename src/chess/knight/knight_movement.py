from typing import Optional

from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.motion.logic.diagonal_pattern import DiagonalPattern
from chess.motion.logic.geomtery_pattern import GeometryPattern
from chess.motion.logic.vertical_pattern import VerticalPatern
from chess.motion.search import SearchPattern
from chess.motion.quadrant import Quadrant
from chess.motion.walks import linear_walk, diagonal_walk
from chess.common.piece import Piece


class KnightMovement(SearchPattern):

    def __init__(self, motion_definitions=[DiagonalPattern, VerticalPatern]):
        super().__init__(motion_definitions)

    def move(self, chess_piece: Piece, board: Board, destination: Coordinate) -> bool:
        pass

    def path_exists(self, origin: Coordinate, destination: Coordinate, board: Board) -> Optional[GeometryPattern]:
        pass



    def search(self, origin: Coordinate, board: Board) -> list[Coordinate]:
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
