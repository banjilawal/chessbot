from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.motion.orientation.horizontal import HorizontalMotion
from chess.motion.orientation.vertical import VerticalMotion
from chess.motion.movement.movement import MovementStrategy
from chess.motion.quadrant import Quadrant
from chess.motion.walks import linear_walk


class CastleMovement(MovementStrategy):
    def __init__(self, rules=[HorizontalMotion, VerticalMotion]):
        super().__init__(rules)

    def possible_destinations(self, origin: Coordinate, board: Board) -> list[Coordinate]:
        destinations = []
        for quadrant in [Quadrant.N, Quadrant.E, Quadrant.S, Quadrant.W]:
            destinations.extend(linear_walk(origin, quadrant.x_delta, quadrant.y_delta, board))
        return destinations