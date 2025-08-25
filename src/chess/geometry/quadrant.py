

from chess.geometry.coordinate.coordinate import Offset
from enum import Enum, auto
from typing import Optional

from chess.common.config import BOARD_DIMENSION


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

    N = (Offset(column_offset=0, row_offset=1), auto(), "north", -1, 0)
    NE = (Offset(column_offset=1, row_offset=1), auto(), "northeast")
    E = (Offset(column_offset=1, row_offset=0), auto(), "east")
    SE = (Offset(column_offset=1, row_offset=-1), auto(), "southeast")
    S = (Offset(column_offset=0, row_offset=-1), auto(), "south", 1, BOARD_DIMENSION - 1)
    SW = (Offset(column_offset=-1, row_offset=-1), auto(), "southwest")
    W = (Offset(column_offset=-1, row_offset=0), auto(), "west")
    NW = (Offset(column_offset=-1, row_offset=1), auto(), "northwest")

    @property
    def delta(self) -> Offset:
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


    def enemy_quadrant(self) -> Optional['Quadrant']:
        if self == Quadrant.N:
            return Quadrant.S
        return Quadrant.N

    def __str__(self) -> str:
        row_id_str = ""
        if self in [Quadrant.N, Quadrant.S]:
            row_id_str = f"self._row_id"
        return (
            f"Quadrant[name:"
            f"{self._name} "
            f"row_id:{row_id_str}"
            f"forward_step:{self._forward_step} "
            f"]"
        )