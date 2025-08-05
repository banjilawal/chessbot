from chess.geometry.coordinate.coordinate import Coordinate
from chess.motion.castle.service.castle_reachable import CastleReachable
from chess.geometry.diagonal import Diagonal
from chess.motion.abstract.reachable import Reachable

class QueenReachable(Reachable):

    @staticmethod
    def is_reachable(origin: Coordinate, destination: Coordinate) -> bool:
        return (
                CastleReachable.is_reachable(origin, destination) or
                Diagonal.is_diagonal(origin, destination)
        )