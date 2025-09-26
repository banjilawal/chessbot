from typing import Generic, cast, TypeVar

from chess.common import Result, Validator, KNIGHT_STEP_SIZE
from chess.vector import (
    Vector, NullVectorException,
    NullXComponentException, NullYComponentException,
    VectorBelowBoundsException, VectorAboveBoundsException,
    VectorValidationException
)

T = TypeVar('T')

class VectorValidator(Validator):
    """
    Validates existing `Vector` instances that are passed around the system.

    While `VectorBuilder` ensures valid Vectors are created, `VectorValidator`
    checks `Vector` instances that already exist - whether they came from
    deserialization, external sources, or need re-validation after modifications.
    
    Usage:
        ```python
        # Validate an existing vector
        vector_validation = VectorValidator.validate(candidate)    
        if not vector_validation.is_success():
            raise vector_validation.exception
        vector = cast(Vector, vector_validation.payload)
        ```

    Use VectorBuilder for construction, VectorValidator for verification.
    """

    @staticmethod
    def validate(t: Generic[T]) -> Result[Vector]:
        """
          Validates that an existing `Vector` instance meets all specifications.

          Performs comprehensive validation on a `Vector` instance that already exists,
          checking type safety, null values, and component bounds. Unlike VectorBuilder
          which creates new valid Vectors, this validator verifies existing `Vector`
          instances from external sources, deserialization, or after modifications.

          Args:
              t (Generic[T]): The object to validate, expected to be a Vector instance.
                            Must not be None and must be within component bounds
                            [-KNIGHT_STEP_SIZE, KNIGHT_STEP_SIZE].

          Returns:
              Result[Vector]: A Result containing either:
                  - On success: The validated Vector instance in the payload
                  - On failure: Error information and exception details

          Raises:
              VectorValidationException: Wraps any specification violations including:
                  - NullVectorException: if input is None
                  - TypeError: if input is not a Vector instance
                  - NullXComponentException: if Vector.x is None
                  - NullYComponentException: if Vector.y is None
                  - VectorBelowBoundsException: if x or y < -KNIGHT_STEP_SIZE
                  - VectorAboveBoundsException: if x or y > KNIGHT_STEP_SIZE

          Note:
              Use VectorBuilder for creating new Vectors with validation,
              use VectorValidator for verifying existing Vector instances.

          Example:
              ```python
              # Validate an existing vector
              result = VectorValidator.validate(some_vector)
              if result.is_success():
                  validated_vector = result.payload
              else:
                  # Handle validation failure
                  pass
              ```
          """
        method = "VectorValidator.validate"

        try:
            if t is None:
                raise NullVectorException(
                    f"{method} NullVectorException.DEFAULT_MESSAGE"
                )

            if not isinstance(t, Vector):
                raise TypeError(f"{method} Expected an Vector, got {type(t).__name__}")

            vector = cast(Vector, t)

            if vector.x is None:
                raise NullXComponentException(f"{method}: {NullXComponentException.DEFAULT_MESSAGE}")

            if vector.x < -KNIGHT_STEP_SIZE:
                # print(f"x: {x} knight_step_size:{-KNIGHT_STEP_SIZE}")
                raise VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}")

            if vector.x > KNIGHT_STEP_SIZE:
                raise VectorAboveBoundsException( f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}" )

            if vector.y is None:
                raise NullYComponentException(f"{method} {NullYComponentException.DEFAULT_MESSAGE}")

            if vector.y < -KNIGHT_STEP_SIZE:
                raise VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}"
                                                 )
            if vector.y > KNIGHT_STEP_SIZE:
                raise VectorAboveBoundsException(f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}" )

            return Result(payload=vector)

        except (
                TypeError,
                NullVectorException,
                NullYComponentException,
                NullXComponentException,
                VectorBelowBoundsException,
                VectorAboveBoundsException
        ) as e:
            raise VectorValidationException(f"{method}: f{VectorValidationException.DEFAULT_MESSAGE}") from e

        # This block catches any unexpected exceptions
        # You might want to log the error here before re-raising
        except Exception as e:
            raise VectorValidationException(f"An unexpected error occurred during validation: {e}") from e
#
#
# def main():
#     vector = Vector(x=2, y=1)
#     specification_result = VectorValidator.validate(vector)
#     if specification_result.is_success():
#         print("Vector specification satisfied.")
#     else:
#         print("Vector specification not satisfied.")
#
# if __name__ == "__main__":
#     main()
