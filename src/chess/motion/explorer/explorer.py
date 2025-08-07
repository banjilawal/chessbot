
from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING

from chess.geometry.coordinate.coordinate import Coordinate
from chess.map.map_service import MapService

if TYPE_CHECKING:
    from chess.team.model.piece import ChessPiece


class Explorer(ABC):

    def __init__(self):
        pass


    @staticmethod
    @abstractmethod
    def discover_destinations(self, chess_piece: ChessPiece,  map_service: MapService) -> List[Coordinate]:
        pass
        """Returns a list of coordinates that the chess_piece can reach from its current position."""



