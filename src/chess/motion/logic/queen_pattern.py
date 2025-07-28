from chess.motion.logic.castle_reachable import CastleReachable
from chess.motion.travel.diagonal_pattern import DiagonalPattern
from chess.motion.logic.reachable import Reachable

class QueenPattern(Reachable):

    @staticmethod
    def is_reachable(origin: Coordinate, destination: Coordinate) -> bool:
        return (
                CastleReachable.is_reachable(origin, destination) or
                DiagonalPattern.is_reachable(origin, destination)
        )