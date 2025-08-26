
from enum import Enum, auto
from typing import Optional

from chess.common.config import BOARD_DIMENSION
from chess.geometry.vector.delta import Vector
from chess.geometry.vector.scalar import Scalar


class Quadrant(Enum):
    def __new__(cls, quad_id: int, vector: Vector, scalar: Scalar=Scalar(value=0), row: Optional[int]=None):
        obj = object.__new__(cls)
        obj._id = quad_id
        obj._vector = vector
        obj._scalar = scalar
        obj._row = row
        return obj

    N = (auto(), Vector(x=0, y=1), Scalar(value=-1), 0)
    NE = (auto(), Vector(x=1, y=1))
    E = (auto(), Vector(x=1, y=0))
    SE = (auto(), Vector(x=1, y=-1))
    S = (auto(), Vector(x=0, y=-1), Scalar(value=1), BOARD_DIMENSION - 1)
    SW = (auto(), Vector(x=-1, y=-1))
    W = (auto(), Vector(x=-1, y=0))
    NW = (auto(), Vector(x=-1, y=1))


    @property
    def id(self) -> int:
        return self._id


    @property
    def vector(self) -> Vector:
        return self._vector


    @property
    def scalar(self) -> Optional[Scalar]:
        return self._scalar


    @property
    def row(self) -> Optional[int]:
        return self._row


    def enemy_quadrant(self) -> Optional['Quadrant']:
        if self == Quadrant.N:
            return Quadrant.S
        return Quadrant.N


    def __str__(self) -> str:
        scalar_str = f", {self._scalar}" if self.scalar != Scalar(value=0) else f""
        row_str = f", row={self._row}" if self._row is not None else ""
        return (
            f"Quadrant[name:{self.name}, "
            f"id:{self._id}, "
            f"{self._vector}"
            f"{scalar_str}"
            f"{row_str}]"
        )


def main():
    for quadrant in Quadrant:
        print(quadrant)

if __name__ == "__main__":
    main()
