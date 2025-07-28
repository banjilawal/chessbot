from chess.motion.logic.diagonal_pattern import DiagonalPattern
from chess.motion.logic.geomtery_pattern import GeometryPattern
from chess.motion.logic.horizontal_pattern import HorizontalPattern
from chess.motion.logic.vertical_pattern import VerticalPatern


class CastleReachable(GeometryPattern):

    @staticmethod
    def points_match_pattern(origin: Coordinate, destination: Coordinate) -> bool:
        return (
            HorizontalPattern.points_match_pattern(origin, destination) or
            VerticalPatern.points_match_pattern(origin, destination)
        )