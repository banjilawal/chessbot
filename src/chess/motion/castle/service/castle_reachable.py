
from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.line.horizontal import Horizontal
from chess.geometry.line.vertical import Vertical
from chess.motion.abstract.reachable import Reachable



class CastleReachable(Reachable):

    @staticmethod
    def is_reachable(origin: Coordinate, destination: Coordinate) -> bool:
        return Vertical.is_vertical(origin, destination) or Horizontal.is_horizontal(origin, destination)
