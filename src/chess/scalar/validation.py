from typing import cast, Generic, TypeVar

from chess.exception import NullNumberException
from chess.common import Result, Validator, BOARD_DIMENSION

from chess.scalar import(
    Scalar, NullScalarException, ScalarBelowBoundsException,
    ScalarAboveBoundsException, ScalarValidationException
)

T = TypeVar('T')

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
        If either validators fails their team_exception will be encapsulated in a 
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
            
            NScalarBelowLowerBoundException: If scalar.value < 0
            
            ScalarAboveBoundsException: If scalar.value >= BOARD_DIMENSION
            
            ScalarValidationException: Wraps any preceding exceptions      
        """
        try:
            if t is None:
                raise NullScalarException(f"{method} NullScalarException.DEFAULT_MESSAGE")


            scalar = cast(Scalar, t)

            if scalar.value is None:
                raise NullNumberException(f"{method} {NullNumberException.DEFAULT_MESSAGE}")

            if scalar.value < -BOARD_DIMENSION:
                raise ScalarBelowBoundsException(
                    f"{method}: {ScalarBelowBoundsException.DEFAULT_MESSAGE}"
                )

            if scalar.value >= BOARD_DIMENSION:
                raise ScalarAboveBoundsException(
                    f"{method}: {ScalarAboveBoundsException.DEFAULT_MESSAGE}"
                )

            return Result(payload=scalar)

        except (
            TypeError,
            NullScalarException,
            NullNumberException,
            ScalarBelowBoundsException,
            ScalarAboveBoundsException,
        ) as e:
            raise ScalarValidationException(
                f"{method}: {ScalarValidationException.DEFAULT_MESSAGE}"
            ) from e


# def main():
#     result = ScalarSpecification.is_satisfied_by(Scalar(3))
#     if result.is_success():
#         print(f"Scalar is valid: {result.payload}")
#     else:
#         print(f"Scalar is invalid: {result.team_exception}")
#
# if __name__ == "__main__":
#     main()