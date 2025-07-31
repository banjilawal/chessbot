from abc import ABC, abstractmethod

from chess.geometry.board.coordinate import Coordinate


class Reachable(ABC):

    @staticmethod
    @abstractmethod
    def is_reachable(origin: Coordinate, destination: Coordinate) -> bool:
        """Returns True if the move from origin to destination fits this pattern."""
        pass