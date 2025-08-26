from typing import Generic, cast

from assurance.exception.validation.coord import CoordinateValidationException
from assurance.exception.validation.distance_magnitude_validation import DistanceMagnitudeValidationException
from assurance.result.base import Result
from assurance.validation.coord import CoordinateSpecification
from assurance.validation.specification import Specification, T
from chess.exception.null.distance_magnitude_null import NullDistanceMagnitudeException
from chess.geometry.coordinate.distance import ScalarDistance


class DistanceMagnitudeSpecification(Specification):

    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> Result[ScalarDistance]:
        method = "DistanceMagnitudeSpecification.is_satisfied_by"

        """
        Validates DistanceMagnitude between coordinates p and q:
            - Not null
            - Coordinate p meets CoordinateSpecification
            - Coordinate q meets CoordinateSpecification
        If any validation fails their exception will be encapsulated in DistanceMagnitudeValidationException
            
        Args
            t (DistanceMagnitude): DistanceMagnitude to validate
            
         Returns:
             Result[T]: A Result object containing the validated payload if the specification is satisfied,
                        CoordinateValidationException otherwise.
        
        Raises:
            NullDistanceMagnitudeException: if t is null  
            TypeError: if t is not Coordinate
.
            DistanceMagnitudeValidationException: Wraps any
                (NullCoordinate, TypeError, RowOutOfBounds or ColumnOutOfBoundsException)
                
        """
        try:
            if t is None:
                raise NullDistanceMagnitudeException(
                    f"{method} NullDistanceMagnitudeException.DEFAULT_MESSAGE"
)

            if not isinstance(t, ScalarDistance):
                raise TypeError(f"{method} Expected a DistanceMagnitude, got {type(t).__name__}")

            cartesian_distance = cast(ScalarDistance, t)

            p_coord_spec_result = CoordinateSpecification.is_satisfied_by(cartesian_distance.p)
            if not p_coord_spec_result.is_success():
                raise p_coord_spec_result.exception

            q_coord_spec_result = CoordinateSpecification.is_satisfied_by(cartesian_distance.q)
            if not q_coord_spec_result.is_success():
                raise q_coord_spec_result.exception
            
            return Result(payload=cartesian_distance)
    


        except (
            NullDistanceMagnitudeException, TypeError, CoordinateValidationException) as e:
            raise DistanceMagnitudeValidationException(
                f"{method} DistanceMagnitudeSpecification : validation failed"
            ) from e