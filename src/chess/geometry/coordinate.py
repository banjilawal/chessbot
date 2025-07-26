






class Delta:
    _x: int
    _y: int
    def __init__(self, x: int, y: int):
        if x < 0:
            print("x cannot be negative.")
            return
        if y < 0:
            print("y cannot be negative.")
            return
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

    def name(self) -> str:
        return self._column.letter.capitalize() + str(self._row.id)

    def shift(self, delta: Delta) -> 'Coordinate':
        return Coordinate(row=self.row.id + delta.y, column=self.column.index + delta.x)