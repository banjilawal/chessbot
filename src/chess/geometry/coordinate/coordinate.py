from chess.common.chess_exception import ChessException, NullChessObjectException, NullDeltaeException, \
    NullDeltaException
from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.geometry.coordinate.delta import Delta


class CoordinateException(ChessException):
    default_message = "Invalid Coordinate state"

class RowOutOfRangeException(CoordinateException):
    default_message = (
        f"The coordinate row is outside ChessBoard's row range of 0 to {ROW_SIZE - 1} inclusive."
    )

class ColumnOutOfRangeException(CoordinateException):
    default_message = (
        f"The coordinate colum is outside ChessBoard's row range of 0 to {ROW_SIZE - 1} inclusive."
    )



class Coordinate:
    _row: int
    _column: int

    """
    Coordinate is a tuple of the row, and column indices of the 2x2 array which makes up a ChessBoard.
    All fields are immutable.
    
    Attributes:
        _row (int): index of row array position.
        _colum (int): index of the column array.
    """

    def __init__(self, row: int, column: int):
        method = "Coordinate.__init__()"

        """
        Creates a Coordinate instance

        Args:
            row (int): row index
            column (int): column index

        Raise:
            RowOutOfRangeException: If row is out of bounds of ROW_SIZE.
            ColumnOutOfRangeException: If column is out of bounds of COLUMN_SIZE.
            CoordinateOutOfBoundsException: If row or column are out ChessBoard's dimensions
        """

        if row is None:
            raise NullChessObjectException(
                f"{method}: row cannot be null. Coordinate instantiation failed"
            )
        if column is None:
            raise NullChessObjectException(
                f"{method}: column cannot be null. Coordinate instantiation failed"
            )

        if row < 0 or row >= ROW_SIZE:
            raise RowOutOfRangeException(RowOutOfRangeException.default_message)
        if column < 0 or column >= COLUMN_SIZE:
            raise ColumnOutOfRangeException(ColumnOutOfRangeException.default_message)

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
        return f"Coordinate(row:{self._row} column:{self._column})"


    def shift(self, delta: Delta) -> 'Coordinate':
        method = "Coordinate.shift()"

        """
        Creates a new Coordinate shifted by row + row_delta, colum + column_delta

        Args:
            delta (Delta): vector added to coordinate's x, y values

        Raise:
            NullDeltaException: if delta is null.
        """

        if delta is None:
            raise NullDeltaException(f"{method} {NullDeltaException.default_message}")

        # Creating totally new values makes sure nothing
        # hinky happens creating the new shifted coordinate.
        new_row = self._row + delta.row_delta
        new_colum = self._column + delta.column_delta

        return Coordinate(row=new_row, column=new_colum)


