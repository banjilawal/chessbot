from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.motion.define.diagonal import DiagonalDefine
from chess.motion.define.horizontal import HorizontalDefine
from chess.motion.define.vertical import VerticalDefine
from chess.motion.quadrant import Quadrant
from chess.motion.movement.movement import MovementStrategy
from chess.motion.walks import diagonal_walk, linear_walk


class BishopMovement(MovementStrategy):
    def __init__(self, rules=[DiagonalDefine]):
        super().__init__(rules)

    def path_exists(self, origin: Coordinate, destination: Coordinate, board: Board) -> bool:


    def possible_destinations(self, origin: Coordinate, board: Board) -> list[Coordinate]:
        destinations = []
        for quadrant in [Quadrant.NE, Quadrant.SW, Quadrant.SE, Quadrant.NE]:
            destinations.extend(diagonal_walk(origin, quadrant.x_delta, quadrant.y_delta, board))
        return destinations






