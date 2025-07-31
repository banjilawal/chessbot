from chess.geometry.board.coordinate import Coordinate
from chess.geometry.diagonal import Diagonal
from chess.motion.logic.reachable import Reachable


class BishopReachable(Reachable):

    @staticmethod
    def is_reachable(origin: Coordinate, destination: Coordinate) -> bool:
        return Diagonal.is_diagonal(origin, destination)