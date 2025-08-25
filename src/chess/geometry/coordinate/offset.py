from chess.common.config import KNIGHT_WALKING_RANGE, BOARD_DIMENSION
from chess.exception.coordinate.offset_multiplication import OffsetMultiplicationResultException
from chess.exception.coordinate.offset_multiplication_factor import OffsetMultiplicationFactorException
from chess.exception.coordinate.offset_range import OffsetRangeException
from chess.exception.null.null_column_offset import NullColumnOffsetException
from chess.exception.null.null_offset_scalar import NullOffsetMultiplicationFactorExcepetion
from chess.exception.null.null_row_offset import NullRowOffsetException


class Offset:
    _row_offset: int
    _column_offset: int

    """
    Offset is an immutable class is used for shifting a Coordinate by a offset. The
    Offset is just a vector added to a Coordinate vector. 

    Attributes:
        _row_offset (int): Amount added to target coordinate's row
        _column_offset (int): Amount added to target coordinate's column
    """


    def __init__(self, row_offset: int, column_offset: int):
        method = f"Offset__init__"

        """
        Constructs a Offset instance.
        
        Args:
            row_offset (int): value for _row_offset
            column_offset (int): value fpr column_offset
            
        Raises:
            NollChessObjectException: if either row_offset or column_offset are null.
        """

        if row_offset is None:
            raise NullRowOffsetException(f"{method}: row_offset cannot be null")
        if row_offset < -KNIGHT_WALKING_RANGE or row_offset > KNIGHT_WALKING_RANGE:
            raise OffsetRangeException(f"{method}: row_offset {OffsetRangeException.DEFAULT_MESSAGE}")

        if column_offset is None:
            raise NullColumnOffsetException(f"{method} {NullColumnOffsetException.DEFAULT_MESSAGE}")
        if column_offset < -KNIGHT_WALKING_RANGE or column_offset > KNIGHT_WALKING_RANGE:
            raise OffsetRangeException(f"{method}: column_offset {OffsetRangeException.DEFAULT_MESSAGE}")


        self._row_offset = row_offset
        self._column_offset = column_offset


    @property
    def row_offset(self) -> int:
        return self._row_offset


    @property
    def column_offset(self) -> int:
        return self._column_offset


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Offset):
            return False

        return (
                self._column_offset == other.column_offset and
                self._row_offset == other.row_offset
        )


    def __mul__(self, scalar: int) -> 'Offset':
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

        if scalar is None:
            raise NullOffsetMultiplicationFactorExcepetion(f"{method}: scalar cannot be null")

        if scalar < -BOARD_DIMENSION or scalar > BOARD_DIMENSION:
            raise OffsetMultiplicationFactorException(
                f"{method}: scalar {OffsetMultiplicationFactorException.DEFAULT_MESSAGE}"
            )

        new_row_offset = self.row_offset * scalar
        if new_row_offset <= -BOARD_DIMENSION or new_row_offset >= BOARD_DIMENSION:
            raise OffsetMultiplicationResultException(
                f"{method}: row_offset {OffsetMultiplicationResultException.DEFAULT_MESSAGE}"
            )

        new_column_offset = self.column_offset * scalar
        if new_column_offset <= -BOARD_DIMENSION or new_column_offset >= BOARD_DIMENSION:
            raise OffsetMultiplicationResultException(
                f"{method}: column_offset {OffsetMultiplicationResultException.DEFAULT_MESSAGE}"
            )

        return Offset(row_offset=new_row_offset, column_offset=new_column_offset)


    def __str__(self):
        return f"Offset(row_offset={self._row_offset}, column_offset={self._column_offset})"