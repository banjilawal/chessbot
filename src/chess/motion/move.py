from abc import ABC, abstractmethod
from chess.common.geometry import Coordinate

class Move(ABC):

    def __self__(self):


    @abstractmethod
    def motion_fits_rule(self, origin: Coordinate, destination: Coordinate) -> bool:
        pass