from chess.common.geometry import Coordinate
from chess.motion.move import Move


class HorizontalMove(Move):
    """X changes while Y stays the same."""
    def __init__(self):
        super().__init__(self)


    def motion_fits_rule(self, origin: Coordinate, destination: Coordinate) -> bool:
        # Same row, column changes
        return origin.row == destination.row and origin.column != destination.column