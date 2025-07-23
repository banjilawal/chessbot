from chess.board.chess_board import ChessBoard
from chess.common.geometry import Coordinate
from chess.motion.motions.diagonal import DiagonalMotion
from chess.motion.motions.horizontal import HorizontalMotion
from chess.motion.motions.vertical import VerticalMotion
from chess.motion.quadrant import Quadrant
from chess.motion.movement.movement import MovementStrategy
from chess.motion.walks import diagonal_walk, linear_walk


class BishopMovement(MovementStrategy):
    def __init__(self, rules=[DiagonalMotion]):
        super().__init__(rules)

    def possible_destinations(self, origin: Coordinate, board: ChessBoard) -> list[Coordinate]:
        destinations = []
        for quadrant in [Quadrant.NE, Quadrant.SW, Quadrant.SE, Quadrant.NE]:
            destinations.extend(diagonal_walk(origin, quadrant.x_delta, quadrant.y_delta, board))
        return destinations


class CastleMovement(MovementStrategy):
    def __init__(self, rules=[HorizontalMotion, VerticalMotion]):
        super().__init__(rules)

    def possible_destinations(self, origin: Coordinate, board: ChessBoard) -> list[Coordinate]:
        destinations = []
        for quadrant in [Quadrant.N, Quadrant.E, Quadrant.S, Quadrant.W]:
            destinations.extend(linear_walk(origin, quadrant.x_delta, quadrant.y_delta, board))
        return destinations


class KnightMovement(MovementStrategy):
    def __init__(self, rules=[DiagonalMotion, VerticalMotion]):
        super().__init__(rules)

    def possible_destinations(self, origin: Coordinate, board: ChessBoard) -> list[Coordinate]:
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

class PawnMovement(MovementStrategy):
    def __init__(self, rules=[VerticalMotion, DiagonalMotion]):
        super().__init__(rules)

    def possible_destinations(self, origin: Coordinate, board: ChessBoard) -> list[Coordinate]:
        destinations = []
        next_point = origin.shift(0, 1)
        if board.coordinate_is_valid(next_point):
            destinations.append(next_point)
        return destinations

    class KingMovement(MovementStrategy):
    class QueenMovement(MovementStrategy):