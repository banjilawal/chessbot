from chess.geometry.coordinate import Coordinate
from chess.motion.logic.reachable import Reachable
from chess.geometry.horizontal import Horizontal
from chess.geometry.vertical import Vertical


class CastleReachable(Reachable):

    @staticmethod
    def is_reachable(origin: Coordinate, destination: Coordinate) -> bool:
        return (
            Horizontal.is_horizontal(origin, destination) or
            Vertical.is_vertical(origin, destination)
        )