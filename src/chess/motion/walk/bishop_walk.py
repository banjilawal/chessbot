from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.line.diagonal import Diagonal
from chess.motion.walk.walk import Walk


class BishopWalk(Walk):

    @staticmethod
    def is_walkable(origin: Coordinate, destination: Coordinate) -> bool:
        return Diagonal.is_diagonal(origin, destination)