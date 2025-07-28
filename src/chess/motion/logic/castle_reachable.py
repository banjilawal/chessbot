from chess.motion.logic.reachable import Reachable
from chess.motion.logic.horizontal import Horizontal
from chess.motion.logic.vertical import Vertical


class CastleReachable(Reachable):

    @staticmethod
    def is_reachable(origin: Coordinate, destination: Coordinate) -> bool:
        return (
                Horizontal.is_reachable(origin, destination) or
                Vertical.is_reachable(origin, destination)
        )