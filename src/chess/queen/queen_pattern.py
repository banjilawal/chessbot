from chess.common.geometry import Coordinate
from chess.motion.logic.diagonal_pattern import DiagonalPattern
from chess.motion.logic.geomtery_pattern import GeometryPattern
from chess.motion.logic.horizontal_pattern import HorizontalPattern
from chess.motion.logic.vertical import VerticalDefinition


class QueenPattern(GeometryPattern):

    @staticmethod
    def matches(origin: Coordinate, destination: Coordinate) -> bool:
        return (
            HorizontalPattern.matches(origin, destination) or
            VerticalDefinition.matches(origin, destination) or
            DiagonalPattern.matches(origin, destination)
        )