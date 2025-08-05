from chess.geometry.coordinate.coordinate import Coordinate
from chess.motion.logic.reachable import Reachable


class KingReachable(Reachable):

    @staticmethod
    def is_reachable(origin: Coordinate, destination: Coordinate) -> bool:
        return abs(origin.row - destination.row) == 1 and abs(origin.column - destination.column) == 1