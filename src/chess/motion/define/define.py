from abc import ABC, abstractmethod
from chess.common.geometry import Coordinate

class Define(ABC):

    @abstractmethod
    def motion_fits_rule(self, origin: Coordinate, destination: Coordinate) -> bool:
        pass