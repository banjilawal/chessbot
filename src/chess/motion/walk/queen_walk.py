from chess.geometry.coordinate.coordinate import Coordinate
from chess.motion.walk.castle_walk import CastleWalk
from chess.geometry.line.diagonal import Diagonal
from chess.motion.walk.walk import Walk

class QueenWalk(Walk):

    @staticmethod
    def is_walkable(origin: Coordinate, destination: Coordinate) -> bool:
        return (
            CastleWalk.is_walkable(origin, destination) or
            Diagonal.is_diagonal(origin, destination)
        )