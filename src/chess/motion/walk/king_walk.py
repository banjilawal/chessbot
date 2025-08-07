from chess.geometry.coordinate.coordinate import Coordinate
from chess.motion.walk.walk import Walk


class KingWalk(Walk):

    @staticmethod
    def is_walkable(origin: Coordinate, destination: Coordinate) -> bool:
        return abs(origin.row - destination.row) == 1 and abs(origin.column - destination.column) == 1