from chess.motion.logic.castle_pattern import CastlePattern
from chess.motion.logic.diagonal_pattern import DiagonalPattern
from chess.motion.logic.geomtery_pattern import GeometryPattern

class QueenPattern(GeometryPattern):

    @staticmethod
    def points_match_pattern(origin: Coordinate, destination: Coordinate) -> bool:
        return (
            CastlePattern.points_match_pattern(origin, destination) or
            DiagonalPattern.points_match_pattern(origin, destination)
        )