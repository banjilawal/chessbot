from enum import Enum

# Made move.Direction enum to indicate the direction of movement on an XY axis on a unit circle. Either;
# LEFT(-1,0) = 0,
# UP(0,1)
# RIGHT(1,0),
# DOWN(0-1)."
class BoardDirection(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3


    @property
    def coordinate(self) -> tuple[int, int]:
        mapping = {
            BoardDirection.LEFT: (-1, 0),
            BoardDirection.UP: (0, 1),
            BoardDirection.RIGHT: (1, 0),
            BoardDirection.DOWN: (0, -1),
        }
        return mapping[self]