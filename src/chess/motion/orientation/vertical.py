from chess.common.geometry import Coordinate
from chess.motion.orientation.motion import Motion


class VerticalMotion(Motion):
    """Y changes while X stays the same."""
    def __init__(self):
        super().__init__(self)


    def motion_fits_rule(self, origin: Coordinate, destination: Coordinate) -> bool:
        # Same column, row changes
        return origin.column == destination.column and origin.row != destination.row