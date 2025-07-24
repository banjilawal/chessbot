from chess.common.geometry import Coordinate
from chess.motion.define.define import Define


class HorizontalDefine(Define):
    """X changes while Y stays the same."""
    def __init__(self):
        super().__init__(self)


    def line_fits_definition(self, origin: Coordinate, destination: Coordinate) -> bool:
        # Same row, column changes
        return origin.row == destination.row and origin.column != destination.column