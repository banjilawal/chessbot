from typing import Generic, cast

from assurance.exception.validation.vector import VectorValidationException
from assurance.result.base import Result
from assurance.validators.base import Validator, T
from chess.common.config import KNIGHT_STEP_SIZE

from chess.exception.null.x_dim import XComponentNullException
from chess.exception.null.vector import NullVectorException
from chess.exception.null.y_dim import YComponentNullException
from chess.exception.vector.y_dim import YComponentBelowLowerBoundException, YComponentAboveUpperBoundException
from chess.exception.vector.x_dim import XComponentBelowLowerBoundException, XComponentAboveUpperBoundException

from chess.geometry.delta import Vector


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
        If any validators fails their exception will be encapsulated in 
        VectorValidationException
            
        Args
            t (Vector): Vector to validate
            
         Returns:
             Result[T]: A Result object containing the validated payload if 
             specification is satisfied, VectorValidationException otherwise.
        
        Raises:

            NullVectorException: if t is null 
              
            TypeError: if t is not an Vector
            
            XComponentNullException: if Vector.x is null
            
            XComponentBelowLowerBoundException: if -Vector.x < -KNIGHT_STEP_SIZE
               
            XComponentAboveUpperBoundException: if Vector.x > KNIGHT_STEP_SIZE
            
            XComponentNullException: if Vector.x is null
            
            YComponentBelowLowerBoundException: if -Vector.y < -KNIGHT_STEP_SIZE
            
            YComponentAboveUpperBoundException: if Vector.y > KNIGHT_STEP_SIZE
            
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
                raise XComponentNullException(
                    f"{method}: {XComponentNullException.DEFAULT_MESSAGE}"
                )

            if vector.x < -KNIGHT_STEP_SIZE:
                # print(f"x: {x} knight_step_size:{-KNIGHT_STEP_SIZE}")
                raise XComponentBelowLowerBoundException(
                    f"{method}: {XComponentBelowLowerBoundException.DEFAULT_MESSAGE}"
                )

            if vector.x > KNIGHT_STEP_SIZE:
                raise XComponentAboveUpperBoundException(
                    f"{method}: {XComponentAboveUpperBoundException.DEFAULT_MESSAGE}"
                )

            if vector.y is None:
                raise YComponentNullException(
                    f"{method} {YComponentNullException.DEFAULT_MESSAGE}"
                )

            if vector.y < -KNIGHT_STEP_SIZE:
                raise YComponentBelowLowerBoundException(
                    f"{method}: {YComponentBelowLowerBoundException.DEFAULT_MESSAGE}"
                )
            if vector.y > KNIGHT_STEP_SIZE:
                raise YComponentAboveUpperBoundException(
                    f"{method}: {YComponentAboveUpperBoundException.DEFAULT_MESSAGE}"
                )

            return Result(payload=vector)

        except (
            TypeError,
            NullVectorException,
            YComponentNullException,
            XComponentNullException,
            YComponentBelowLowerBoundException,
            YComponentAboveUpperBoundException,
            XComponentBelowLowerBoundException,
            XComponentAboveUpperBoundException
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
