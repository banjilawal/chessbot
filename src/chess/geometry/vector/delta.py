from chess.common.config import BOARD_DIMENSION, KNIGHT_STEP_SIZE
from chess.exception.null.x_dim import XComponentNullException
from chess.exception.null.y_dim import YComponentNullException
from chess.exception.offset.column import YComponentBelowLowerBoundException, YComponentAboveUpperBoundException
from chess.exception.offset.mul import NegativeScalarException, ZeroScalarException, \
    ScalarOutofBoundsException, OffsetMultiplicationOverflowException, RowDeltaOverflowExceptioDn, \
    ColumnDeltaOverflowExceptioDn
from chess.exception.offset.row import XComponentAboveUpperBoundException, XComponentBelowLowerBoundException

from chess.exception.null.scalar import NullScalarException



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

        if  x < 0 and x < -(KNIGHT_STEP_SIZE):
            print(f"delta_row: {x} knight_step_size:{-(KNIGHT_STEP_SIZE)}")
            raise XComponentBelowLowerBoundException(
                f"{method}: {XComponentBelowLowerBoundException.DEFAULT_MESSAGE}"
            )
        if x >= 0 and x > KNIGHT_STEP_SIZE:
            raise XComponentAboveUpperBoundException(
                f"{method}: {XComponentAboveUpperBoundException.DEFAULT_MESSAGE}"
            )

        if y is None:
            raise YComponentNullException(
                f"{method} {YComponentNullException.DEFAULT_MESSAGE}"
            )

        if  y < 0 and y < -KNIGHT_STEP_SIZE:
            raise YComponentBelowLowerBoundException(
                f"{method}: {YComponentBelowLowerBoundException.DEFAULT_MESSAGE}"
            )
        if y >= 0 and y > KNIGHT_STEP_SIZE:
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


    def __mul__(self, factor: int) -> 'Offset':
        method = f"Offset.__mul__"

        """
        Multiplies the Offset by scalar value.
        
        Args:
            scalar (int): Amount to multiply the offset's dimensions by.
            
        Returns: 
            Offset:
            
        Raises:
            NollChessObjectException: If scalar is None
        """

        if factor is None:
            raise NullScalarException(f"{method}: scalar cannot be null")

        if factor < 0:
            raise NegativeScalarException(
                f"{method}: {NegativeScalarException.DEFAULT_MESSAGE}"
            )

        if factor == 0:
            raise ZeroScalarException(
                f"{method}: {ZeroScalarException.DEFAULT_MESSAGE}"
            )

        if factor >= BOARD_DIMENSION:
            raise ScalarOutofBoundsException(
                f"{method}: scalar {ScalarOutofBoundsException.DEFAULT_MESSAGE}"
            )

        new_delta_row = self.delta_row * factor
        if abs(new_delta_row) >= BOARD_DIMENSION:
            raise RowDeltaOverflowExceptioDn(
                f"{method}: {RowDeltaOverflowExceptioDn.DEFAULT_MESSAGE}"
            )

        new_delta_column = self.delta_column * factor
        if abs(new_delta_column) >= BOARD_DIMENSION:
            raise ColumnDeltaOverflowExceptioDn(
                f"{method}: {ColumnDeltaOverflowExceptioDn.DEFAULT_MESSAGE}"
            )

        return Offset(delta_row=new_delta_row, delta_column=new_delta_column)


    def __str__(self):
        return f"Vector(x={self._x}, y={self._y})"

def main():
    offset = Offset(-3, 1)
    print(offset)
    # scaled_offset = offset * 3
    # print(scaled_offset)

if __name__ == "__main__":
    main()