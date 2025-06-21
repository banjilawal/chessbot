from dataclasses import dataclass

from game.common.direction import Direction
from game.common.side import Side


@dataclass
class Quadilateral:
    _length: int
    _height: int

    def __post_init__(self):
        self._topSide: Side = Side(orientation=Direction.UP, dimension=self._height)
        self._bottomSide: Side = Side(orientation=Direction.DOWN, dimension=self._height)
        self._leftSide: Side = Side(orientation=Direction.LEFT, dimension=self._height)
        self._rightSide: Side = Side(orientation=Direction.RIGHT, dimension=self._height)