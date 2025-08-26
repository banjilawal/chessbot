from typing import Generic, cast

from assurance.exception.validation.scalar import ScalarValidationException
from assurance.result.base import Result
from assurance.validation.base import Specification, T
from chess.common.config import BOARD_DIMENSION
from chess.exception.null.number import NullNumberException
from chess.exception.null.scalar import NullScalarException
from chess.exception.offset.mul import NegativeScalarException, ZeroScalarException, ScalarOutofBoundsException
from chess.geometry.vector.scalar import Scalar


class ScalarSpecification(Specification):

    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> Result[Scalar]:
        method = "ScalarSpecification.is_satisfied_by"

        """
        Validates a scalar with chained exceptions for scalar meeting specifications:
            - Not null
            - value is not null
            - value is within the bounds of the chess chessboard
            - column is not null
            - column is within the bounds of the chess chessboard
        If either validation fails their exception will be encapsulated in a 
        ScalarValidationException
            
        Args
            t (Scalar): scalar to validate
            
         Returns:
             Result[T]: A Result object containing the validated payload if the specification 
             is satisfied, ScalarValidationException otherwise.
        
        Raises:
            NullScalarException: if t is null   
            TypeError: if t is not Scalar
            
            NullNumberException: If scalar.value is null 
            
            NegativeScalarException: If scalar.value is negative
            
            ZeroScalarException: If scalar.value is zero
            
            ScalarOutofBoundsException: If scalar.value is outside the range
                (0, BOARD_DIMENSION - 1) inclusive
.
            ScalarValidationException: Wraps any preceding exceptions      
        """
        try:
            if t is None:
                raise NullScalarException(f"{method} NullScalarException.DEFAULT_MESSAGE")

            if not isinstance(t, Scalar):
                raise TypeError(f"{method} Expected a Scalar, got {type(t).__name__}")

            scalar = cast(Scalar, t)

            if scalar.value is None:
                raise NullNumberException(f"{method} {NullNumberException.DEFAULT_MESSAGE}")

            if scalar.value < 0:
                raise NegativeScalarException(f"{method}: {NegativeScalarException.DEFAULT_MESSAGE}")

            if scalar.value == 0:
                raise ZeroScalarException(f"{method}: {ZeroScalarException.DEFAULT_MESSAGE}")

            if scalar.value >= BOARD_DIMENSION:
                raise ScalarOutofBoundsException(
                    f"{method}: {ScalarOutofBoundsException.DEFAULT_MESSAGE}"
                )

            return Result(payload=scalar)

        except (
            TypeError,
            NullScalarException,
            NullNumberException,
            NegativeScalarException,
            ZeroScalarException,
            ScalarOutofBoundsException,
        ) as e:
            raise ScalarValidationException(
                f"{method} ScalarSpecification: Scalar validation failed"
            ) from e


# def main():
#     result = ScalarSpecification.is_satisfied_by(Scalar(5))
#     if result.is_success():
#         print(f"Valid Scalar: {result.payload}")
#     else:
#         print(f"Validation failed: {result.exception}")
#
#     result = ScalarSpecification.is_satisfied_by(Scalar(-3))
#     if result.is_success():
#         print(f"Valid Scalar: {result.payload}")
#     else:
#         print(f"Validation failed: {result.exception}")
#
#     result = ScalarSpecification.is_satisfied_by(Scalar(0))
#     if result.is_success():
#         print(f"Valid Scalar: {result.payload}")
#     else:
#         print(f"Validation failed: {result.exception}")
#
#     result = ScalarSpecification.is_satisfied_by(Scalar(BOARD_DIMENSION))
#     if result.is_success():
#         print(f"Valid Scalar: {result.payload}")
#     else:
#         print(f"Validation failed: {result.exception}")
#
# if __name__ == "__main__":
#     main()