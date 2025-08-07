from abc import ABC, abstractmethod

from chess.geometry.coordinate.coordinate import Coordinate


class Walker(ABC):

    @abstractmethod
    def walk(self, destination: Coordinate):
        pass
