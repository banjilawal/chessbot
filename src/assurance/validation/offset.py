from typing import Generic, cast

from assurance.exception.validation.offset import OffsetValidationException
from assurance.result.base import Result
from assurance.validation.base import Specification, T
from chess.common.config import KNIGHT_STEP_SIZE
from chess.exception.offset.column import (
    DeltaColumnBelowSteppingBoundException,
    DeltaColumnAboveSteppingBoundException
)
from chess.exception.offset.row import (
    DeltaRowBelowSteppingBoundException,
    DeltaRowAboveSteppingBoundException
)
from chess.exception.null.column_offset import NullColumnOffsetException
from chess.exception.null.offset import NullOffsetException
from chess.exception.null.row_offset import NullRowOffsetException

from chess.geometry.coordinate.offset import Offset


class OffsetSpecification(Specification):

    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> Result[Offset]:
        method = "OffsetSpecification.is_satisfied_by"

        """
        Validates an Offset instance meets specifications:
            - Not null
            - delta_row is not null
            - delta_row is not greater than KNIGHT_WALKING_RANGE
            - delta_column is not null
            - delta_column is not greater than KNIGHT_WALKING_RANGE
        If any validation fails their exception will be encapsulated in 
        OffsetValidationException
            
        Args
            t (Coordinate): offset to validate
            
         Returns:
             Result[T]: A Result object containing the validated payload if 
             specification is satisfied, OffsetValidationException otherwise.
        
        Raises:

            NullOffsetException: if t is null   
            TypeError: if t is not an Offset
            
            NullRowOffsetException: if offset.delta_row is null
            NullColumnOffsetException: if offset.delta_column is null
            
            DeltaRowBelowSteppingBoundException: if 
                -offset.delta_row < -KNIGHT_STEP_SIZE
                
            DeltaRowAboveSteppingBoundException: if
            RowOffsetSizeException: if 
                abs(offset.delta_row) > KNIGHT_WALKING_RANGE
            
            NullColumnOffsetException: if offset.delta_column is null
            ColumnOffsetSizeException: if 
                abs(offset.delta_column) > KNIGHT_WALKING_RANGE
            
            OffsetValidationException: Wraps preceding exceptions:     
        """
        try:
            if t is None:
                raise NullOffsetException(
                    f"{method} NullOffSetException.DEFAULT_MESSAGE"
                )

            if not isinstance(t, Offset):
                raise TypeError(f"{method} Expected an Offset, got {type(t).__name__}")

            offset = cast(Offset, t)

            if offset.delta_row is None:
                raise NullRowOffsetException(
                    f"{method} {NullRowOffsetException.DEFAULT_MESSAGE}"
                )
            if offset.delta_row < 0 and offset.delta_row < KNIGHT_STEP_SIZE:
                raise DeltaRowBelowSteppingBoundException(
                    f"{method} {DeltaRowBelowSteppingBoundException.DEFAULT_MESSAGE}"
                )
            if offset.delta_row >= 0 and offset.delta_row > KNIGHT_STEP_SIZE:
                raise DeltaRowBelowSteppingBoundException(
                    f"{method} {DeltaRowBelowSteppingBoundException.DEFAULT_MESSAGE}"
                )

            if offset.delta_column is None:
                raise NullColumnOffsetException(
                    f"{method} {NullRowOffsetException.DEFAULT_MESSAGE}"
                )
            if offset.delta_column < 0 and offset.delta_column <  KNIGHT_STEP_SIZE:
                raise DeltaColumnBelowSteppingBoundException(
                    f"{method} {DeltaColumnBelowSteppingBoundException.DEFAULT_MESSAGE}"
                )
            if offset.delta_column >= 0 and offset.delta_column > KNIGHT_STEP_SIZE:
                raise DeltaColumnAboveSteppingBoundException(
                    f"{method} {DeltaColumnAboveSteppingBoundException.DEFAULT_MESSAGE}"
                )

            return Result(payload=offset)

        except (
                TypeError,
                NullOffsetException,
                NullRowOffsetException,
                NullColumnOffsetException,
                DeltaRowBelowSteppingBoundException,
                DeltaRowAboveSteppingBoundException,
                DeltaColumnBelowSteppingBoundException,
                DeltaColumnAboveSteppingBoundException,
        ) as e:
            raise OffsetValidationException(
                f"{method} Offset validation failed"
            ) from e


# def main():
#     result = OffsetSpecification.is_satisfied_by(Offset(2, 1))
#     if result.is_success():
#         offset = result.payload
#         print(
#             f"Offset is valid: "
#             f"delta_row={offset.delta_row}, "
#             f"delta_column={offset.delta_column}"
#         )
#     else:
#         print(f"Offset validation failed: {result.exception}")
#
#     result = OffsetSpecification.is_satisfied_by(
#         Offset(KNIGHT_STEP_SIZE + 1, 1)
#     )
#     if result.is_success():
#         offset = result.payload
#         print(
#             f"Offset is valid: "
#             f"delta_row={offset.delta_row}, "
#             f"delta_column={offset.delta_column}"
#         )
#     else:
#         print(f"Offset validation failed: {result.exception}")
#
# if __name__ == "__main__":
#     main()
