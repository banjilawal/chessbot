from chess.common.chess_exception import NollChessObjectException
from chess.common.config import COLUMN_SIZE, ROW_SIZE
from chess.geometry.coordinate.coordinate import CoordinateOutOfBoundsException, Coordinate


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
            NollChessObjectException: If p or q are null.
            CoordinateOutOfBoundsException: If p or q are out ChessBoard's dimensions
        """

        if p is None:
            raise NollChessObjectException(
                f"{method}: Coordinate p cannot be null. CoordinateDistance instantiation failed"
            )
        if q is None:
            raise NollChessObjectException(
                f"{method}: Coordinate q cannot be null. CoordinateDistance instantiation failed"
            )

        if q.row < 0 or q.row >= ROW_SIZE:
            raise CoordinateOutOfBoundsException(
                f"{method} row {q.row} is outside ChessBoard's row range."
                f"It must be between 0 and {ROW_SIZE - 1} inclusive."
            )
        if q.column < 0 or q.column >= COLUMN_SIZE:
            raise CoordinateOutOfBoundsException(
                f"{method} column {q.column} is outside ChessBoard's column range."
                f"It must be between 0 and {COLUMN_SIZE - 1} inclusive."
            )

        if p.row < 0 or p.row >= ROW_SIZE:
            raise CoordinateOutOfBoundsException(
                f"{method} row {p.row} is outside ChessBoard's row range."
                f"It must be between 0 and {ROW_SIZE - 1} inclusive."
            )
        if p.column < 0 or p.column >= COLUMN_SIZE:
            raise CoordinateOutOfBoundsException(
                f"{method} column {p.column} is outside ChessBoard's column range."
                f"It must be between 0 and {COLUMN_SIZE - 1} inclusive."
            )

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