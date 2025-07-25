from chess.common.geometry import Coordinate
from chess.motion.logic.geomtery_pattern import GeometryPattern


class KingPattern(GeometryPattern):

    @staticmethod
    def matches(origin: Coordinate, destination: Coordinate) -> bool:
        return abs(origin.row - destination.row) == 1 and abs(origin.column - destination.column) == 1