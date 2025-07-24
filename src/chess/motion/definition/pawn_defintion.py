from typing import Optional

from chess.common.geometry import Coordinate
from chess.motion.definition.definition import Definition


class PawnDefinition(Definition):
    def __init__(self, definition_id, title):
        super().__init__(definition_id, title)

    def line_fits_definition(self, origin: Coordinate, destination: Coordinate) -> bool:
        return origin.column == destination.column and origin.row + 1 == destination.row
