from dataclasses import dataclass
from typing import Optional
from chess.common.piece import Piece

@dataclass(Frozen=True)
class Delta:
    x: int
    y: int

    def __mul__(self, scalar: int) -> 'Delta':
        return Delta(x=self.x * scalar, y=self.y * scalar)

class Coordinate:
    _row: int
    _column: int

    def __init__(self, row: int, column: int):
        if row < 0:
            raise ValueError("Row cannot be negative")
        if column < 0:
            raise ValueError("Column cannot be negative")
        self._row = row
        self._column = column

    @property
    def row(self) -> int:
        return self._row

    @property
    def column(self) -> int:
        return self._column

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Coordinate):
            return False
        return self.row == other.row and self.column == other.column

    def __hash__(self):
        return hash((self.row, self.column))


    def shift(self, delta: Delta) -> 'Coordinate':
        return Coordinate(row=self.row + delta.y, column=self.column + delta)


class Square:
    _id: int
    _coordinate: Coordinate
    _occupant: Optional[Piece]

    def __init__(self, square_id: int, coordinate: Coordinate):
        if square_id < 0:
            raise ValueError("Square id cannot be negative.")
        if coordinate is None:
            raise ValueError("Coordinate cannot be None.")

        self._id = square_id
        self._coordinate = coordinate
        self._occupant = None

    @property
    def id(self) -> int:
        return self._id

    @property
    def coordinate(self) -> Coordinate:
        return self._coordinate

    @property
    def occupant(self) -> Optional[Piece]:
        return self._occupant

    @occupant.setter
    def occupant(self, occupant: Optional[Piece]):
        self._occupant = occupant

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Square):
            return False
        return self.id == other.id and self.coordinate == other.coordinate

    def __hash__(self):
        return hash(self.id)
