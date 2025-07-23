from enum import Enum, auto


class Quadrant(Enum):
    NW = (-1, -1)
    NE = (-1, 1)
    SW = (1, -1)
    SE = (1, 1)
    N = (-1, 0)
    S = (1, 0)
    E = (0, 1)
    W = (0, -1)

    @property
    def delta(self) -> tuple[int, int]:
        return self.value

    @property
    def x_delta(self) -> int:
        return self.value[0]

    @property
    def y_delta(self) -> int:
        return self.value[1]