from abc import ABC, abstractmethod
from chess.common.geometry import Coordinate

class GeometryPattern(ABC):
    @staticmethod
    @abstractmethod
    def matches(origin: Coordinate, destination: Coordinate) -> bool:
        """Returns True if the move from origin to destination fits this pattern."""
        pass