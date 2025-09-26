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
    Validates existing Vector instances that are passed around the system.

    While VectorBuilder ensures valid Vectors are created, VectorValidator
    checks Vector instances that already exist - whether they came from
    deserialization, external sources, or need re-validation after modifications.

    Use VectorBuilder for construction, VectorValidator for verification.
    """

    @staticmethod
    def validate(t: Generic[T]) -> Result[Vector]:
        """
        Validates an existing `Vector` instance meets specifications:
            - Not null
            - `x` is not null
            - `x` is not less than -KNIGHT_WALKING_RANGE
            - `x` is not greater than KNIGHT_WALKING_RANGE
            - `y` is not null
            - `y` is not less than -KNIGHT_WALKING_RANGE
            - `y` is not greater than KNIGHT_WALKING_RANGE
            
        Args
            `t` (`Vector`): Existing `Vector` instance to validate
            
         Returns:
             `Result`[`Vector`]: A `Result` object containing the validated payload if
             specification is satisfied, `VectorValidationException` otherwise.
        
        Raises:
            NullVectorException: if t is null
            TypeError: if t is not a Vector
            NullXComponentException: if Vector.x is null
            VectorBelowBoundsException: if -Vector.x < -KNIGHT_STEP_SIZE or -Vector.y < -KNIGHT_STEP_SIZE
            VectorAboveBoundException: if Vector.x > KNIGHT_STEP_SIZE or Vector.y > KNIGHT_STEP_SIZE
            NullXComponentException: if Vector.x is null
            NullYComponentException: if Vector.x is null
            
            VectorValidationException: Wraps preceding exceptions:     
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
