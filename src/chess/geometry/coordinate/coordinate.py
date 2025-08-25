from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.exception.coordinate.column_out_of_bounds import ColumnOutOfBoundsException
from chess.exception.coordinate.row_out_of_bounds import RowOutOfBoundsException
from chess.exception.null.delta_null import NullDeltaException
from chess.exception.null.null_column import NullColumnException
from chess.exception.null.null_row import NullRowException
from chess.geometry.coordinate.offset import Offset

class Coordinate:
    _row: int
    _column: int

    """
    Coordinate is a tuple of the row, and column indices of the 2x2 array which makes up a
    ChessBoard. All fields are immutable.
    
    Attributes:
        _row (int): index of row array position.
        _colum (int): index of the column array.
    """

    def __init__(self, row: int, column: int):
        method = "Coordinate.__init__()"
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


    def shift_by_offset(self, offset: Offset) -> 'Coordinate':
        method = "Coordinate.shift()"

        """
        Creates a new Coordinate shifted by row + row_delta, colum + column_delta

        Args:
            delta (Delta): vector added to coordinate's x, y values
        
        Return:
            Coordinate

        Raise:
            NullDeltaException: if delta is null.
        """

        if offset is None:
            raise NullDeltaException(f"{method} {NullDeltaException.default_message}")

        # Creating totally new values makes sure nothing
        # hinky happens creating the new shifted coordinate.
        new_row = self._row + offset.row_offset
        new_colum = self._column + offset.column_offset

        return Coordinate(row=new_row, column=new_colum)


