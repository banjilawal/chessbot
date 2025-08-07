from chess.geometry.coordinate.coordinate import Coordinate
from chess.motion.castle.service.castle_reachable import CastleWalk
from chess.geometry.line.diagonal import Diagonal
from chess.motion.abstract.walk import Walk

class QueenWalk(Walk):

    @staticmethod
    def is_walkable(origin: Coordinate, destination: Coordinate) -> bool:
        return (
                CastleWalk.is_walkable(origin, destination) or
                Diagonal.is_diagonal(origin, destination)
        )