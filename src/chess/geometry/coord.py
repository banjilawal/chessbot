from typing import cast

from assurance.validators.scalar import ScalarValidator
from assurance.validators.vector import VectorValidator
from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.exception.coord import ColumnBelowBoundsException
from chess.exception.coord import RowBelowBoundsException
from chess.exception.null.column import NullColumnException
from chess.exception.null.row import NullRowException
from chess.geometry.delta import Vector
from chess.geometry.scalar import Scalar


class Coord:
    _row: int
    _column: int

    """
    Coord is a tuple of the row, and column indices of the 2x2 array which makes up a
    ChessBoard. All fields are immutable.
    
    Attributes:
        _row (int): index of row array position.
        _colum (int): index of the column array.
    """

    def __init__(self, row: int, column: int):
        method = "Coord.__init__()"

        if row is None:
            raise NullRowException(f"{method} {NullRowException.DEFAULT_MESSAGE}")
        if row < 0 or row >= ROW_SIZE:
            raise RowBelowBoundsException(
                f"{method} Row value {row} is out of bounds. "
                f"Must be between 0 and {ROW_SIZE - 1} inclusive."
            )
        if column is None:
            raise NullColumnException(f"{method} {NullColumnException.DEFAULT_MESSAGE}")
        if column < 0 or column >= COLUMN_SIZE:
            raise ColumnBelowBoundsException(
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
        if not isinstance(other, Coord):
            return False
        return self._row == other.row and self._column == other.column


    def __hash__(self):
        return hash((self._row, self._column))


    def __str__(self):
        return f"Coord(row:{self._row} column:{self._column})"


    def scalar_product(self, scalar: Scalar):
        method = "scalar_product"

        validation = ScalarValidator.validate(scalar)
        if not validation.is_success():
            raise validation.exception

        c = cast(validation.payload, Scalar)
        return Coord(row=self._row * c.value, column =self._column * c.value)


    def add_vector(self, vector: Vector) -> 'Coord':
        method = "add_vector"

        """
        Returns the coord: Coord( self._row + vectory.y, self._column + vector.x)

        Args:
            vector (Vector): vector added to coord's x, y values
        
        Return:
            Coord

        Raise:
            VectorValidationException: if vector fails validators.
            CoordValidationException: if 
        """

        validation = VectorValidator.validate(vector)
        if not validation.is_success():
            raise validation.exception

        v = cast(validation.payload, Vector)
        return Coord(row =self._row + v.y, column =self._column + v.x)

