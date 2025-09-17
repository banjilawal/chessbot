from typing import Generic, cast

from chess.common import Result, Validator, KNIGHT_STEP_SIZE
from chess.vector import Vector, NullVectorException, NullXComponentException, NullYComponentException, \
    VectorBelowBoundsException, VectorAboveBoundsException, VectorValidationException


class VectorValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[Vector]:
        entity = "Vector"
        class_name = f"{entity}Specification"
        method = f"{class_name}.is_satisfied_by"

        """
        Validates an Vector instance meets specifications:
            - Not null
            - x is not null
            - x is not less than -KNIGHT_WALKING_RANGE
            - x is not greater than KNIGHT_WALKING_RANGE
            - y is not null
            - y is not less than -KNIGHT_WALKING_RANGE
            - y is not greater than KNIGHT_WALKING_RANGE
        If any validators fails their team_exception will be encapsulated in 
        VectorValidationException
            
        Args
            t (Vector): Vector to validate
            
         Returns:
             Result[T]: A Result object containing the validated payload if 
             specification is satisfied, VectorValidationException otherwise.
        
        Raises:

            NullVectorException: if t is null 
              
            TypeError: if t is not an Vector
            
            NullXComponentException: if Vector.x is null
            
            VectorBelowBoundsException: if -Vector.x < -KNIGHT_STEP_SIZE or -Vector.y < -KNIGHT_STEP_SIZE
               
            VectorAboveBoundException: if Vector.x > KNIGHT_STEP_SIZE or Vector.y > KNIGHT_STEP_SIZE
            
            NullXComponentException: if Vector.x is null
            
            NullYComponentException: if Vector.x is null
            
            VectorValidationException: Wraps preceding exceptions:     
        """
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
            raise VectorValidationException(
                f"{method}: f{VectorValidationException.DEFAULT_MESSAGE}"
            ) from e


def main():
    vector = Vector(x=2, y=1)
    specification_result = VectorValidator.validate(vector)
    if specification_result.is_success():
        print("Vector specification satisfied.")
    else:
        print("Vector specification not satisfied.")

if __name__ == "__main__":
    main()
