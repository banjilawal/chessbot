from abc import ABC, abstractmethod

from chess.geometry.coordinate.coordinate import Coordinate
from chess.map.service.map_service import MapService


class Walk(ABC):

    @staticmethod
    @abstractmethod
    def is_walkable(origin: Coordinate, destination: Coordinate, grid_service: MapService) -> bool:
        """Returns True if the move from origin to destination fits this pattern."""
        pass