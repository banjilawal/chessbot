from abc import ABC, abstractmethod

from chess.geometry.coordinate.coordinate import Coordinate


class Walk(ABC):

    @staticmethod
    @abstractmethod
    def is_walkable(origin: Coordinate, destination: Coordinate) -> bool:
        """Returns True if the move from origin to destination fits this pattern."""
        pass