from enum import Enum, auto

from chess.common.geometry import Delta


class Quadrant(Enum):
    NW = Delta(x=-1, y=1)
    NE = Delta(x=1, y=1)
    SW = Delta(x=-1, y=-1)
    SE = Delta(x=1, y=-1)
    N = Delta(x=0, y=1)
    S = Delta(x=0, y=-1)
    E = Delta(x=1, y=0)
    W = Delta(x=-1, y=0)
