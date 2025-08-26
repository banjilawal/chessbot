from typing import Generic, cast

from assurance.exception.validation.vector import VectorValidationException
from assurance.result.base import Result
from assurance.validation.base import Specification, T
from chess.common.config import KNIGHT_STEP_SIZE
from chess.exception.Vector.column import (
    YVectorBelowMinValueException,
    YVectorAboveMaxValueException
)
from chess.exception.Vector.row import (
    XVectorBelowMinValueException,
    XVectorAboveMaxValueException
)
from chess.exception.null.x_dim import XComponentNullException
from chess.exception.null.vector import NullVectorException
from chess.exception.null.y_dim import YComponentNullException

from chess.geometry.vector.delta import Vector


class VectorSpecification(Specification):

    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> Result[Vector]:
        method = "VectorSpecification.is_satisfied_by"

        """
        Validates an Vector instance meets specifications:
            - Not null
            - delta_row is not null
            - delta_row is not greater than KNIGHT_WALKING_RANGE
            - delta_column is not null
            - delta_column is not greater than KNIGHT_WALKING_RANGE
        If any validation fails their exception will be encapsulated in 
        VectorValidationException
            
        Args
            t (Vector): Vector to validate
            
         Returns:
             Result[T]: A Result object containing the validated payload if 
             specification is satisfied, VectorValidationException otherwise.
        
        Raises:

            NullVectorException: if t is null   
            TypeError: if t is not an Vector
            
            NullRowVectorException: if Vector.delta_row is null
            NullColumnVectorException: if Vector.delta_column is null
            
            DeltaRowBelowSteppingBoundException: if 
                -Vector.delta_row < -KNIGHT_STEP_SIZE
                
            DeltaRowAboveSteppingBoundException: if
            RowVectorSizeException: if 
                abs(Vector.delta_row) > KNIGHT_WALKING_RANGE
            
            NullColumnVectorException: if Vector.delta_column is null
            ColumnVectorSizeException: if 
                abs(Vector.delta_column) > KNIGHT_WALKING_RANGE
            
            VectorValidationException: Wraps preceding exceptions:     
        """
        try:
            if t is None:
                raise NullVectorException(
                    f"{method} NullVectorException.DEFAULT_MESSAGE"
                )

            if not isinstance(t, Vector):
                raise TypeError(f"{method} Expected an Vector, got {type(t).__name__}")

            Vector = cast(Vector, t)

            if Vector.delta_row is None:
                raise YComponentNullException(
                    f"{method} {YComponentNullException.DEFAULT_MESSAGE}"
                )
            if Vector.delta_row < 0 and Vector.delta_row < KNIGHT_STEP_SIZE:
                raise XVectorBelowMinValueException(
                    f"{method} {XVectorBelowMinValueException.DEFAULT_MESSAGE}"
                )
            if Vector.delta_row >= 0 and Vector.delta_row > KNIGHT_STEP_SIZE:
                raise XVectorBelowMinValueException(
                    f"{method} {XVectorBelowMinValueException.DEFAULT_MESSAGE}"
                )

            if Vector.delta_column is None:
                raise XComponentNullException(
                    f"{method} {YComponentNullException.DEFAULT_MESSAGE}"
                )
            if Vector.delta_column < 0 and Vector.delta_column <  KNIGHT_STEP_SIZE:
                raise YVectorBelowMinValueException(
                    f"{method} {YVectorBelowMinValueException.DEFAULT_MESSAGE}"
                )
            if Vector.delta_column >= 0 and Vector.delta_column > KNIGHT_STEP_SIZE:
                raise YVectorAboveMaxValueException(
                    f"{method} {YVectorAboveMaxValueException.DEFAULT_MESSAGE}"
                )

            return Result(payload=Vector)

        except (
                TypeError,
                NullVectorException,
                YComponentNullException,
                XComponentNullException,
                XVectorBelowMinValueException,
                XVectorAboveMaxValueException,
                YVectorBelowMinValueException,
                YVectorAboveMaxValueException,
        ) as e:
            raise VectorValidationException(
                f"{method} Vector validation failed"
            ) from e


# def main():
#     result = VectorSpecification.is_satisfied_by(Vector(2, 1))
#     if result.is_success():
#         Vector = result.payload
#         print(
#             f"Vector is valid: "
#             f"delta_row={Vector.delta_row}, "
#             f"delta_column={Vector.delta_column}"
#         )
#     else:
#         print(f"Vector validation failed: {result.exception}")
#
#     result = VectorSpecification.is_satisfied_by(
#         Vector(KNIGHT_STEP_SIZE + 1, 1)
#     )
#     if result.is_success():
#         Vector = result.payload
#         print(
#             f"Vector is valid: "
#             f"delta_row={Vector.delta_row}, "
#             f"delta_column={Vector.delta_column}"
#         )
#     else:
#         print(f"Vector validation failed: {result.exception}")
#
# if __name__ == "__main__":
#     main()
