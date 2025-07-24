from abc import ABC, abstractmethod
from chess.common.geometry import Coordinate

class Definition(ABC):

    @abstractmethod
    def line_fits_definition(self, origin: Coordinate, destination: Coordinate) -> bool:
        pass