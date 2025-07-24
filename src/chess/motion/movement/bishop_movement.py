from typing import Optional

from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.motion.logic.geomtery_pattern import GeometryPattern
from chess.motion.logic.diagonal_pattern import DiagonalPattern
from chess.motion.logic.horizontal_pattern import HorizontalPattern
from chess.motion.logic.vertical import VerticalDefinition
from chess.motion.quadrant import Quadrant
from chess.motion.movement.movement import MovementStrategy
from chess.motion.walks import diagonal_walk, linear_walk


class BishopMovement(MovementStrategy):
    def __init__(self, motion_definitions=[DiagonalPattern]):
        super().__init__(motion_definitions)

    def path_exists(self, origin: Coordinate, destination: Coordinate, board: Board) -> Optional[GeometryPattern]:
        for definition in self.motion_definitions.values():
            if definition.line_fits_definition(origin, destination):
                return definition
        return None

    def possible_destinations(self, origin: Coordinate, board: Board) -> list[Coordinate]:
        destinations = []
        for quadrant in [Quadrant.NE, Quadrant.SW, Quadrant.SE, Quadrant.NE]:
            destinations.extend(diagonal_walk(origin, quadrant.x_delta, quadrant.y_delta, board))
        return destinations






