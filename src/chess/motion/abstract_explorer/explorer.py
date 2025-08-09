from abc import ABC
from typing import List, TYPE_CHECKING

from chess.geometry.coordinate.coordinate import Coordinate
from chess.board.map_service import MapService

if TYPE_CHECKING:
    from chess.token.piece import ChessPiece


class AbstractExplorer(ABC):

    def __init__(self):
        pass

    @staticmethod
    def discover_destinations(self, chess_piece: ChessPiece, map_service: MapService) -> List[Coordinate]:
        return map_service.find_coordinates_reachable_from_chess_piece(chess_piece)

