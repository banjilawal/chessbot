from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.line.diagonal import Diagonal
from chess.map.map_service import MapService
from chess.motion.walk.walk import Walk


class BishopWalk(Walk):

    @staticmethod
    def is_walkable(origin: Coordinate, destination: Coordinate, map_service: MapService) -> bool:
        return Diagonal.is_diagonal(origin, destination)