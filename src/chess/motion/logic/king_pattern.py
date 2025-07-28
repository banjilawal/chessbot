from chess.geometry.coordinate import Coordinate
from chess.motion.logic.geomtery_pattern import GeometryPattern


class KingPattern(GeometryPattern):

    @staticmethod
    def points_match_pattern(origin: Coordinate, destination: Coordinate) -> bool:
        return abs(origin.row - destination.row) == 1 and abs(origin.column - destination.column) == 1