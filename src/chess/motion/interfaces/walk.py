from abc import ABC, abstractmethod

from chess.geometry.coordinate.coordinate import Coordinate
from chess.map.service.grid_service import GridService


class Walk(ABC):

    @staticmethod
    @abstractmethod
    def is_walkable(origin: Coordinate, destination: Coordinate, grid_service: GridService) -> bool:
        """Returns True if the move from origin to destination fits this pattern."""
        pass