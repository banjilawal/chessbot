from typing import Generic, cast

from assurance.exception.validation.coord import CoordinateValidationException
from assurance.exception.validation.euclid import EuclideanDistanceValidationException
from assurance.result.base import Result
from assurance.validators.coord import CoordinateValidator
from assurance.validators.base import Validator, T
from chess.exception.null.euclid import NullDistanceException
from chess.geometry.coordinate.euclid import Distance


class DistanceValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[Distance]:
        entity = "Distance"
        class_name = f"{entity}Specification"
        method = f"{class_name}.is_satisfied_by"

        """
        Validates Distance between coordinates p and q:
            - Not null
            - Coordinate p meets CoordinateSpecification
            - Coordinate q meets CoordinateSpecification
        If any validators fails their exception will be encapsulated in 
            DistanceValidationException
            
        Args
            t (Distance): Distance to validate
            
         Returns:
             Result[T]: A Result object containing the validated payload if the specification 
                is satisfied, CoordinateValidationException otherwise.
        
        Raises:
            NullDistanceException: if t is null  
            TypeError: if t is not Coordinate
.
            DistanceValidationException: Wraps any
                (NullCoordinate, TypeError, RowOutOfBounds or ColumnOutOfBoundsException)
                
        """
        try:
            if t is None:
                raise NullDistanceException(
                    f"{method} NullDistanceException.DEFAULT_MESSAGE"
)

            if not isinstance(t, Distance):
                raise TypeError(f"{method} Expected a Distance, got {type(t).__name__}")

            cartesian_distance = cast(Distance, t)

            p_coord_spec_result = CoordinateValidator.validate(cartesian_distance.p)
            if not p_coord_spec_result.is_success():
                raise p_coord_spec_result.exception

            q_coord_spec_result = CoordinateValidator.validate(cartesian_distance.q)
            if not q_coord_spec_result.is_success():
                raise q_coord_spec_result.exception
            
            return Result(payload=cartesian_distance)
    


        except (
            NullDistanceException, TypeError, CoordinateValidationException) as e:
            raise EuclideanDistanceValidationException(
                f"{method}: {EuclideanDistanceValidationException.DEFAULT_MESSAGE}"
            ) from e