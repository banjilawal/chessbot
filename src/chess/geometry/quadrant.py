
from enum import Enum, auto

from chess.vector import Vector


class Quadrant(Enum):
  def __new__(cls, quad_id:int, vector: Vector):
    obj = object.__new__(cls)
    obj._id = quad_id
    obj._vector = vector

    return obj

  N = (auto(), Vector(x=0, y=1))
  NE = (auto(), Vector(x=1, y=1))
  E = (auto(), Vector(x=1, y=0))
  SE = (auto(), Vector(x=1, y=-1))
  S = (auto(), Vector(x=0, y=-1))
  SW = (auto(), Vector(x=-1, y=-1))
  W = (auto(), Vector(x=-1, y=0))
  NW = (auto(), Vector(x=-1, y=1))


  @property
  def id(self) -> int:
    return self._id


  @property
  def vector(self) -> Vector:
    return self._vector


  def __str__(self) -> str:
    return f"Quadrant[ id:{self._id} name:{self.name} {self._vector}"


def main():
  for quadrant in Quadrant:
    print(quadrant)

if __name__ == "__main__":
  main()
