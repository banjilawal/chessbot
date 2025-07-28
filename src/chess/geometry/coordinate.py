from chess.geometry.column import Column
from chess.geometry.row import Row
from chess.system_config import ROW_SIZE, COLUMN_SIZE


class Delta:
    _x: int
    _y: int

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Delta):
            return False
        return self._x == other.x and self._y == other.y

    def __mul__(self, scalar: int) -> 'Delta':
        return Delta(x=self.x * scalar, y=self.y * scalar)



class Coordinate:
    _row: int
    _column: int

    def __init__(self, row: int, column: int):
        if row < 0 or row >= ROW_SIZE:
            raise ValueError("A row must be between 0 and 7 inclusive.")
            return
        if column < 0 or column >= COLUMN_SIZE:
            raise ValueError("A column must be between 0 and 7 inclusive.")
            return

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
        return self._row == other.row and self._column == other.column


    def __hash__(self):
        return hash((self.row, self.column))


    def __str__(self):
        return f"[{self._column}, {self._row}]"


    def shift(self, delta: Delta) -> 'Coordinate':
        return Coordinate(row=self._row + delta.y, column=self._column+ delta.x)