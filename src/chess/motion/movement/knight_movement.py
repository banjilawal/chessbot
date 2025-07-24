from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.motion.orientation.diagonal import DiagonalMotion
from chess.motion.orientation.vertical import VerticalMotion
from chess.motion.movement.movement import MovementStrategy
from chess.motion.quadrant import Quadrant
from chess.motion.walks import linear_walk, diagonal_walk


class KnightMovement(MovementStrategy):
    def __init__(self, rules=[DiagonalMotion, VerticalMotion]):
        super().__init__(rules)

    def possible_destinations(self, origin: Coordinate, board: Board) -> list[Coordinate]:
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
