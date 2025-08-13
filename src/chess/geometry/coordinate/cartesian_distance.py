
from chess.common.config import COLUMN_SIZE, ROW_SIZE
from chess.exception.coordinate.column_out_of_bounds import ColumnOutOfBoundsException
from chess.exception.coordinate.row_out_of_bounds import RowOutOfBoundsException
from chess.exception.null.coordinate_null import NullCoordinateException
from chess.geometry.coordinate.coordinate import Coordinate


class CartesianDistance:
    _p: Coordinate
    _q: Coordinate
    _distance: int

    """
    Gives the absolute value of the Euclidean distance between coordinates p and q.
    Useful in sorting coordinates by distance from some origin. All fields are immutable.

    Attributes:
        _p (Coordinate): One of the points in the tuple
        _q (Coordinate): Other point in the tuple
        _distance (int): Absolute value of length of a straight line between p and q. Only the scale matters
            the square root is not calculated. 
    """

    def __init__(self, p: Coordinate, q: Coordinate):
        method = "CartesianDistance.__init__()"

        """
        Creates a CartesianDistance instance. _distance is calculated inside the constructor

        Args:
            p (Coordinate): One coordinate in the pair
            q (Coordinate): Other coordinate in the pair

        Raise:
            NullCoordinateException: If p or q are null.
            RowOutOfRangeException: If p or q rows are out of bounds
            ColumnOutOfRangeException: if p or q columns are out of bounds
        """

        if p is None:
            raise NullCoordinateException(f"{method} {NullCoordinateException.default_message}")
        if q is None:
            raise NullCoordinateException(f"{method} {NullCoordinateException.default_message}")

        if p.row < 0 or p.row >= ROW_SIZE:
            raise RowOutOfBoundsException(f"{method} {p.row} {RowOutOfBoundsException.default_message}")
        if p.column < 0 or p.column >= COLUMN_SIZE:
            raise ColumnOutOfBoundsException(f"{method} {p.column} {ColumnOutOfBoundsException.default_message}")

        if q.row < 0 or q.row >= ROW_SIZE:
            raise RowOutOfBoundsException(f"{method} {q.row} {RowOutOfBoundsException.default_message}")
        if q.column < 0 or q.column >= COLUMN_SIZE:
            raise ColumnOutOfBoundsException(f"{method} {q.column} {ColumnOutOfBoundsException.default_message}")

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