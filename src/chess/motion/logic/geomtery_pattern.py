from abc import ABC, abstractmethod
from chess.common.geometry import Coordinate

class GeometryPattern(ABC):
    _id: int
    _title: str

    def __init__(self, definition_id: int, title: str):
        self._id = id
        self._title = title

    @property
    def id(self) -> int:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, GeometryPattern):
            return False
        return self._id == other.id and self._title == other.title


    @abstractmethod
    def line_fits_definition(self, origin: Coordinate, destination: Coordinate) -> bool:
        pass