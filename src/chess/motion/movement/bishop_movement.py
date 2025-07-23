from chess.board.board import Board
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

    def possible_destinations(self, origin: Coordinate, board: Board) -> list[Coordinate]:
        destinations = []
        for quadrant in [Quadrant.NE, Quadrant.SW, Quadrant.SE, Quadrant.NE]:
            destinations.extend(diagonal_walk(origin, quadrant.x_delta, quadrant.y_delta, board))
        return destinations






