from dataclasses import dataclass
from typing import Optional
from chess.common.piece import Piece

class Column:
    _letter: str
    _index: int
    def __init__(self, letter:str):
        self.__letter = letter

    @property
    def letter(self) -> str:
        return self._letter

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Column):
            return False
        return self._letter == other.letter

class Row:
    _id: int
    def __int__(self, row_id: int):
        self._id = row_id

    @property
    def id(self) -> int:
        return self._id


@dataclass(Frozen=True)
class Delta:
    x: int
    y: int

    def __mul__(self, scalar: int) -> 'Delta':
        return Delta(x=self.x * scalar, y=self.y * scalar)

class Coordinate:
    _row: Row
    _column: Column

    def __init__(self, row: Row, column: Column):
        if row is None:
            print("A coordinate cannot have a null row")
            return
        if column is None:
            print("A coordinate cannot have a null column")
            return
        self._row = row
        self._column = column

    @property
    def row(self) -> Row:
        return self._row

    @property
    def column(self) -> Column:
        return self._column

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Coordinate):
            return False
        return self._row == other.row and self._column == other.column

    def __hash__(self):
        return hash((self.row, self.column))

    def shift(self, delta: Delta) -> 'Coordinate':
        return Coordinate(row=self.row.id + delta.y, column=self.column.index + delta.x)


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
