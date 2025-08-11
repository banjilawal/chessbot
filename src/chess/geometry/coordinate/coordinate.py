
from chess.common.config import ROW_SIZE, COLUMN_SIZE








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
        return hash((self._row, self._column))


    def __str__(self):
        return f"(row:{self._row} column:{self._column})"


    def shift(self, delta: Delta) -> 'Coordinate':
        return Coordinate(
            row=self._row + delta.delta_row,
            column=self._column + delta.column_delta
        )

class CartesianDistance:
    _p: Coordinate
    _q: Coordinate
    _distance: int

    def __init__(self, p: Coordinate, q: Coordinate):
        self._p = p
        self._q = q
        self._distance = ((p.row - q.row) ** 2) + ((p.column - q.column) ** 2)

    @property
    def p(self) -> Coordinate:
        return self._p

    @property
    def q(self) -> Coordinate:
        return self._q

    @property
    def distance(self) -> int:
        return self._distance


