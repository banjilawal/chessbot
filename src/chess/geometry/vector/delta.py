from chess.common.config import KNIGHT_STEP_SIZE
from chess.exception.null.x_dim import XComponentNullException
from chess.exception.null.y_dim import YComponentNullException
from chess.exception.offset.column import YComponentBelowLowerBoundException, YComponentAboveUpperBoundException
from chess.exception.offset.row import XComponentAboveUpperBoundException, XComponentBelowLowerBoundException




class Vector:
    _x: int
    _y: int

    """
    Offset is an immutable class is used for shifting a Coordinate by a offset. The
    Offset is just a vector added to a Coordinate vector. 

    Attributes:
        _delta_row (int): Amount added to target coordinate's row
        _delta_column (int): Amount added to target coordinate's column
    """


    def __init__(self, x: int, y: int):
        method = f"Offset__init__"

        """
        Constructs a Offset instance.
        
        Args:
            delta_row (int): value for _delta_row
            delta_column (int): value fpr delta_column
            
        Raises:
            NollChessObjectException: if either delta_row or delta_column are null.
        """

        if x is None:
            raise XComponentNullException(
                f"{method}: {XComponentNullException.DEFAULT_MESSAGE}"
            )

        if  x < -KNIGHT_STEP_SIZE:
            # print(f"delta_row: {x} knight_step_size:{-(KNIGHT_STEP_SIZE)}")
            raise XComponentBelowLowerBoundException(
                f"{method}: {XComponentBelowLowerBoundException.DEFAULT_MESSAGE}"
            )
        if x > KNIGHT_STEP_SIZE:
            raise XComponentAboveUpperBoundException(
                f"{method}: {XComponentAboveUpperBoundException.DEFAULT_MESSAGE}"
            )

        if y is None:
            raise YComponentNullException(
                f"{method} {YComponentNullException.DEFAULT_MESSAGE}"
            )

        if  y < -KNIGHT_STEP_SIZE:
            raise YComponentBelowLowerBoundException(
                f"{method}: {YComponentBelowLowerBoundException.DEFAULT_MESSAGE}"
            )
        if y > KNIGHT_STEP_SIZE:
            raise YComponentAboveUpperBoundException(
                f"{method}: {YComponentAboveUpperBoundException.DEFAULT_MESSAGE}"
            )

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
        if not isinstance(other, Vector):
            return False

        return self._x == other.x and self._y == other.y


    def __str__(self):
        return f"Vector(x={self._x}, y={self._y})"