from chess.system_config import ROW_SIZE, COLUMN_SIZE


class Delta:
    _delta_column: int
    _delta_row: int

    def __init__(self, delta_column: int, delta_row: int):
        self._delta_column = delta_column
        self._delta_row = delta_row

    @property
    def delta_column(self) -> int:
        return self._delta_column

    @property
    def delta_row(self) -> int:
        return self._delta_row

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Delta):
            return False

        return self._delta_column == other.delta_column and self._delta_row == other.delta_row

    def __mul__(self, scalar: int) -> 'Delta':
        new_column_delta = self.delta_column * scalar
        new_row_delta = self.delta_row * scalar

        return Delta(delta_column=new_column_delta, delta_row=new_row_delta)



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
        return f"[{self._column}, {self._row}]"


    def shift(self, delta: Delta) -> 'Coordinate':
        return Coordinate(row=self._row + delta.delta_row, column=self._column + delta.delta_column)