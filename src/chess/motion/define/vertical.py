from chess.common.geometry import Coordinate
from chess.motion.define.definition import Definition


class VerticalDefinition(Definition):
    """Y changes while X stays the same."""
    def __init__(self):
        super().__init__(self)


    def line_fits_definition(self, origin: Coordinate, destination: Coordinate) -> bool:
        # Same column, row changes
        return origin.column == destination.column and origin.row != destination.row