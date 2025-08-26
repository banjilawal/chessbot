from chess.common.config import BOARD_DIMENSION, KNIGHT_STEP_SIZE
from chess.exception.null.column_offset import NullColumnOffsetException
from chess.exception.null.row_offset import NullRowOffsetException
from chess.exception.offset.column import DeltaColumnBelowSteppingBoundException, DeltaColumnAboveSteppingBoundException
from chess.exception.offset.mul import NegativeMultiplicationException, ZeroMultiplicationException, \
    MultiplierOutOfBoundsException, OffsetMultiplicationOverflowException, RowDeltaOverflowExceptioDn, \
    ColumnDeltaOverflowExceptioDn
from chess.exception.offset.row import DeltaRowAboveSteppingBoundException, DeltaRowBelowSteppingBoundException

from chess.exception.null.offset_factor import NullOffSetFactor



class Offset:
    _delta_row: int
    _delta_column: int

    """
    Offset is an immutable class is used for shifting a Coordinate by a offset. The
    Offset is just a vector added to a Coordinate vector. 

    Attributes:
        _delta_row (int): Amount added to target coordinate's row
        _delta_column (int): Amount added to target coordinate's column
    """


    def __init__(self, delta_row: int, delta_column: int):
        method = f"Offset__init__"

        """
        Constructs a Offset instance.
        
        Args:
            delta_row (int): value for _delta_row
            delta_column (int): value fpr delta_column
            
        Raises:
            NollChessObjectException: if either delta_row or delta_column are null.
        """

        if delta_row is None:
            raise NullRowOffsetException(
                f"{method}: {NullRowOffsetException.DEFAULT_MESSAGE}"
            )

        if  delta_row < 0 and delta_row < -(KNIGHT_STEP_SIZE):
            print(f"delta_row: {delta_row} knight_step_size:{-(KNIGHT_STEP_SIZE)}")
            raise DeltaRowBelowSteppingBoundException(
                f"{method}: {DeltaRowBelowSteppingBoundException.DEFAULT_MESSAGE}"
            )
        if delta_row >= 0 and delta_row > KNIGHT_STEP_SIZE:
            raise DeltaRowAboveSteppingBoundException(
                f"{method}: {DeltaRowAboveSteppingBoundException.DEFAULT_MESSAGE}"
            )

        if delta_column is None:
            raise NullColumnOffsetException(
                f"{method} {NullColumnOffsetException.DEFAULT_MESSAGE}"
            )

        if  delta_column < 0 and delta_column < -KNIGHT_STEP_SIZE:
            raise DeltaColumnBelowSteppingBoundException(
                f"{method}: {DeltaColumnBelowSteppingBoundException.DEFAULT_MESSAGE}"
            )
        if delta_column >= 0 and delta_column > KNIGHT_STEP_SIZE:
            raise DeltaColumnAboveSteppingBoundException(
                f"{method}: {DeltaColumnAboveSteppingBoundException.DEFAULT_MESSAGE}"
            )

        self._delta_row = delta_row
        self._delta_column = delta_column


    @property
    def delta_row(self) -> int:
        return self._delta_row


    @property
    def delta_column(self) -> int:
        return self._delta_column


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Offset):
            return False

        return (
            self._delta_row == other.delta_row and 
            self._delta_column == other.delta_column
        )


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
            raise NullOffSetFactor(f"{method}: scalar cannot be null")

        if factor < 0:
            raise NegativeMultiplicationException(
                f"{method}: {NegativeMultiplicationException.DEFAULT_MESSAGE}"
            )

        if factor == 0:
            raise ZeroMultiplicationException(
                f"{method}: {ZeroMultiplicationException.DEFAULT_MESSAGE}"
            )

        if factor >= BOARD_DIMENSION:
            raise MultiplierOutOfBoundsException(
                f"{method}: scalar {MultiplierOutOfBoundsException.DEFAULT_MESSAGE}"
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
        return (
            f"Offset(delta_row={self._delta_row}, "
            f"delta_column={self._delta_column})"
        )

def main():
    offset = Offset(-3, 1)
    print(offset)
    # scaled_offset = offset * 3
    # print(scaled_offset)

if __name__ == "__main__":
    main()