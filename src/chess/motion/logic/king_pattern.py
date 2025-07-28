from chess.geometry.coordinate import Coordinate
from chess.motion.logic.geomtery_pattern import GeometryPattern


class KingPattern(GeometryPattern):

    @staticmethod
    def is_reachable(origin: Coordinate, destination: Coordinate) -> bool:
        return abs(origin.row - destination.row) == 1 and abs(origin.column - destination.column) == 1