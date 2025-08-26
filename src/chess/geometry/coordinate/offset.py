from chess.common.config import KNIGHT_WALKING_RANGE, BOARD_DIMENSION
from chess.exception.offset.zero import MultiplyByZeroException
from chess.exception.offset.negative import NegativeMultiplierException
from chess.exception.offset.overflow import OffsetMultiplicationOverflowException
from chess.exception.offset.factor import MultiplierOutOfBoundsException
from chess.exception.offset.offset_range import OffsetRangeException
from chess.exception.null.column_offset import NullColumnOffsetException
from chess.exception.null.offset_factor import NullOffSetFactor
from chess.exception.null.row_offset import NullRowOffsetException


class Offset:
    _delta_row: int
    _delta_column: int

    """
    Offset is an immutable class is used for shifting a Coordinate by a offset. The
    Offset is just a vector added to a Coordinate vector. 

    Attributes:
        _row_offset (int): Amount added to target coordinate's row
        _column_offset (int): Amount added to target coordinate's column
    """


    def __init__(self, delta_row: int, delta_column: int):
        method = f"Offset__init__"

        """
        Constructs a Offset instance.
        
        Args:
            row_offset (int): value for _row_offset
            column_offset (int): value fpr column_offset
            
        Raises:
            NollChessObjectException: if either row_offset or column_offset are null.
        """

        if delta_row is None:
            raise NullRowOffsetException(f"{method}: delta_row cannot be null")
        if abs(delta_row) > KNIGHT_WALKING_RANGE:
            raise OffsetRangeException(f"{method}: row_offset {OffsetRangeException.DEFAULT_MESSAGE}")

        if delta_column is None:
            raise NullColumnOffsetException(f"{method} {NullColumnOffsetException.DEFAULT_MESSAGE}")
        if delta_column < -KNIGHT_WALKING_RANGE or delta_column > KNIGHT_WALKING_RANGE:
            raise OffsetRangeException(f"{method}: column_offset {OffsetRangeException.DEFAULT_MESSAGE}")


        self._row_delta = delta_row
        self._delta_column = delta_column


    @property
    def delta_row(self) -> int:
        return self._row_delta


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
            self._delta_column == other.delta_column and
            self._row_delta == other.delta_row
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
            raise NegativeMultiplierException(
                f"{method}: {NegativeMultiplierException.DEFAULT_MESSAGE}"
            )

        if factor == 0:
            raise MultiplyByZeroException(
                f"{method}: {MultiplyByZeroException.DEFAULT_MESSAGE}"
            )

        if factor >= BOARD_DIMENSION:
            raise MultiplierOutOfBoundsException(
                f"{method}: scalar {MultiplierOutOfBoundsException.DEFAULT_MESSAGE}"
            )

        new_row_offset = self.delta_row * factor
        if abs(new_row_offset) >= BOARD_DIMENSION:
            raise OffsetMultiplicationOverflowException(
                f"{method}: row_offset {OffsetMultiplicationOverflowException.DEFAULT_MESSAGE}"
            )

        new_column_offset = self.delta_column * factor
        if abs(new_column_offset) >= BOARD_DIMENSION:
            raise OffsetMultiplicationOverflowException(
                f"{method}: column_offset {OffsetMultiplicationOverflowException.DEFAULT_MESSAGE}"
            )

        return Offset(delta_row=new_row_offset, delta_column=new_column_offset)


    def __str__(self):
        return f"Offset(row_offset={self._row_delta}, column_offset={self._delta_column})"