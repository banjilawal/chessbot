
from chess.geometry.coordinate import Delta
from enum import Enum
from typing import Optional

from chess.system_config import BOARD_DIMENSION


class Quadrant(Enum):
    def __new__(cls, delta, id_value, name, forward_step=None, row_id=None):
        obj = object.__new__(cls)
        obj._value_ = delta
        obj._delta = delta
        obj._id = id_value
        obj._name = name
        obj._forward_step = forward_step
        obj._row_id = row_id
        return obj

    N = (Delta(x=0, y=1), 0, "north", 1, 0)
    NE = (Delta(x=1, y=1), 1, "northeast")
    E = (Delta(x=1, y=0), 2, "east")
    SE = (Delta(x=1, y=-1), 3, "southeast")
    S = (Delta(x=0, y=-1), 4, "south", -1, BOARD_DIMENSION - 1)
    SW = (Delta(x=-1, y=-1), 5, "southwest")
    W = (Delta(x=-1, y=0), 6, "west")
    NW = (Delta(x=-1, y=1), 7, "northwest")

    @property
    def delta(self) -> Delta:
        return self._delta

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def forward_step(self) -> Optional[int]:
        return self._forward_step

    @property
    def row_id(self) -> Optional[int]:
        return self._row_id