from chess.geometry.coordinate import Coordinate
from chess.geometry.diagonal import Diagonal
from chess.motion.logic.reachable import Reachable
from chess.geometry.horizontal import Horizontal
from chess.geometry.vertical import Vertical


class BishopReachable(Reachable):

    @staticmethod
    def is_reachable(origin: Coordinate, destination: Coordinate) -> bool:
        return Diagonal.is_diagonal(origin, destination)