
# from assurance.validators.coord import CoordinateSpecification
from assurance.validators.vector import VectorValidator
from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.exception.coordinate.column import ColumnOutOfBoundsException
from chess.exception.coordinate.row import RowOutOfBoundsException
from chess.exception.null.column import NullColumnException
from chess.exception.null.row import NullRowException
from chess.geometry.vector.delta import Vector


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

        if row is None:
            raise NullRowException(f"{method} {NullRowException.DEFAULT_MESSAGE}")
        if row < 0 or row >= ROW_SIZE:
            raise RowOutOfBoundsException(
                f"{method} Row value {row} is out of bounds. "
                f"Must be between 0 and {ROW_SIZE - 1} inclusive."
            )
        if column is None:
            raise NullColumnException(f"{method} {NullColumnException.DEFAULT_MESSAGE}")
        if column < 0 or column >= COLUMN_SIZE:
            raise ColumnOutOfBoundsException(
                f"{method} Column value {column} is out of bounds. "
                f"Must be between 0 and {COLUMN_SIZE - 1} inclusive."
            )
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


    def add_vector(self, vector: Vector) -> 'Coordinate':
        method = "add_vector"

        """
        Returns the coordinate: Coordinate( self._row + vectory.y, self._column + vector.x)

        Args:
            vector (Vector): vector added to coordinate's x, y values
        
        Return:
            Coordinate

        Raise:
            VectorValidationException: if vector fails validators.
            CoordinateValidationException: if 
        """

        result = VectorValidator.validate(vector)
        if result.is_failure():
            raise result.exception

        v = result.payload
        return Coordinate(row = self._row + v.y, column = self._column + v.x)
        # candidate = Coordinate(row = self._row + v.y, column = self._column + v.x)
        #
        # result = CoordinateSpecification.is_satisfied_by(Coordinate(candidate))
        # if not result.is_success():
        #     raise result.exception
        #
        # return result.payload


