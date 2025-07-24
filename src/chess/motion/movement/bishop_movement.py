from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.motion.definition.diagonal import DiagonalDefinition
from chess.motion.definition.horizontal import HorizontalDefinition
from chess.motion.definition.vertical import VerticalDefinition
from chess.motion.quadrant import Quadrant
from chess.motion.movement.movement import MovementStrategy
from chess.motion.walks import diagonal_walk, linear_walk


class BishopMovement(MovementStrategy):
    def __init__(self, motion_definitions=[DiagonalDefinition]):
        super().__init__(motion_definitions)

    def path_exists(self, origin: Coordinate, destination: Coordinate, board: Board) -> bool:
        fo

    def possible_destinations(self, origin: Coordinate, board: Board) -> list[Coordinate]:
        destinations = []
        for quadrant in [Quadrant.NE, Quadrant.SW, Quadrant.SE, Quadrant.NE]:
            destinations.extend(diagonal_walk(origin, quadrant.x_delta, quadrant.y_delta, board))
        return destinations






