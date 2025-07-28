from chess.motion.logic.reachable import Reachable
from chess.motion.travel.horizontal_pattern import HorizontalPattern
from chess.motion.travel.vertical_pattern import VerticalPatern


class CastleReachable(Reachable):

    @staticmethod
    def is_reachable(origin: Coordinate, destination: Coordinate) -> bool:
        return (
                HorizontalPattern.is_reachable(origin, destination) or
                VerticalPatern.is_reachable(origin, destination)
        )