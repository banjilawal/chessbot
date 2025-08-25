
from chess.common.config import COLUMN_SIZE, ROW_SIZE
from chess.exception.coordinate.column_out_of_bounds import ColumnOutOfBoundsException
from chess.exception.coordinate.row_out_of_bounds import RowOutOfBoundsException
from chess.exception.null.coordinate_null import NullCoordinateException
from chess.exception.null.null_column_exception import NullColumnException
from chess.exception.null.null_row_exception import NullRowException
from chess.geometry.coordinate.coordinate import Coordinate


class DistanceMagnitude:
    _p: Coordinate
    _q: Coordinate
    _magnitude: int

    """
    Gives the sqaure of Euclidean distance between coordinates p and q.
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
        """

        self._p = p
        self._q = q
        self._magnitude = ((p.row - q.row) ** 2) + ((p.column - q.column) ** 2)


    @property
    def p(self) -> Coordinate:
        return self._p


    @property
    def q(self) -> Coordinate:
        return self._q


    @property
    def magnitude(self) -> int:
        return self._magnitude