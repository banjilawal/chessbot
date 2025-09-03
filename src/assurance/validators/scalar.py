from typing import Generic, cast

from assurance.exception.validation.scalar import ScalarValidationException
from assurance.result.base import Result
from assurance.validators.base import Validator, T
from chess.common.config import BOARD_DIMENSION
from chess.exception.null.number import NullNumberException
from chess.exception.null.scalar import NullScalarException
from chess.exception.vector.scalar import ScalarBelowLowerBoundException, ScalarAboveUpperBoundException
from chess.geometry.scalar import Scalar


class ScalarValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[Scalar]:
        entity = "Scalar"
        class_name = f"{entity}Specification"
        method = f"{class_name}.is_satisfied_by"

        """
        Validates a scalar with chained exceptions for scalar meeting specifications:
            - Not null
            - value is not null
            - value is within the bounds of the chess chessboard
            - column is not null
            - column is within the bounds of the chess chessboard
        If either validators fails their exception will be encapsulated in a 
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
            
            NScalarBelowLowerBoundException: If scalar.value <= >
            
            ScalarAboveUpperBoundException: If scalar.value >= BOARD_DIMENSION
.
            ScalarValidationException: Wraps any preceding exceptions      
        """
        try:
            if t is None:
                raise NullScalarException(f"{method} NullScalarException.DEFAULT_MESSAGE")


            scalar = cast(Scalar, t)

            if scalar.value is None:
                raise NullNumberException(f"{method} {NullNumberException.DEFAULT_MESSAGE}")

            if scalar.value < -BOARD_DIMENSION:
                raise ScalarBelowLowerBoundException(
                    f"{method}: {ScalarBelowLowerBoundException.DEFAULT_MESSAGE}"
                )

            if scalar.value >= BOARD_DIMENSION:
                raise ScalarAboveUpperBoundException(
                    f"{method}: {ScalarAboveUpperBoundException.DEFAULT_MESSAGE}"
                )

            return Result(payload=scalar)

        except (
            TypeError,
            NullScalarException,
            NullNumberException,
            ScalarBelowLowerBoundException,
            ScalarAboveUpperBoundException,
        ) as e:
            raise ScalarValidationException(
                f"{method}: {ScalarValidationException.DEFAULT_MESSAGE}"
            ) from e


# def main():
#     result = ScalarSpecification.is_satisfied_by(Scalar(3))
#     if result.is_success():
#         print(f"Scalar is valid: {result.payload}")
#     else:
#         print(f"Scalar is invalid: {result.exception}")
#
# if __name__ == "__main__":
#     main()