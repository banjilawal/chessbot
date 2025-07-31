
from chess.geometry.board.coordinate import Coordinate
from chess.geometry.horizontal import Horizontal
from chess.geometry.vertical import Vertical
from chess.motion.logic.reachable import Reachable



class CastleReachable(Reachable):

    @staticmethod
    def is_reachable(origin: Coordinate, destination: Coordinate) -> bool:
        return Vertical.is_vertical(origin, destination) or Horizontal.is_horizontal(origin, destination)
