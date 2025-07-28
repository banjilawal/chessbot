from chess.geometry.coordinate import Coordinate
from chess.motion.logic.geomtery_pattern import GeometryPattern


class DiagonalPattern(GeometryPattern):
    """
    A DiagonalPattern is a rule that defines a diagonal motion. Diagonal motion is:
    forward Xj, Yj <= Xi, Yi = Xi-1, Yi+1
    backward Xj, Yj>=Xi, Yi = Xi+1, Yi+1
    """

    @staticmethod
    def is_reachable(origin: Coordinate, destination: Coordinate) -> bool:
        # Row and column difference equal (non-zero)
        return (origin != destination and
            abs(origin.row - destination.row) == abs(destination.column - origin.column))


