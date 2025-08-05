from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.line.diagonal import Diagonal
from chess.motion.abstract.reachable import Reachable


class BishopReachable(Reachable):

    @staticmethod
    def is_reachable(origin: Coordinate, destination: Coordinate) -> bool:
        return Diagonal.is_diagonal(origin, destination)