from typing import Generic, cast

from assurance.exception.validation.coordinate_validation import CoordinateValidationException
from assurance.exception.validation.distance_magnitude_validation import DistanceMagnitudeValidationException
from assurance.result.base_result import Result
from assurance.validation.coordinate_specification import CoordinateSpecification
from assurance.validation.specification import Specification, T
from chess.exception.null.distance_magnitude_null import NullDistanceMagnitudeException
from chess.geometry.coordinate.distance_magnitude import DistanceMagnitude


class DistanceMagnitudeSpecification(Specification):

    DEFAULT_MESSAGE = "DistanceMagnitudeSpecification: DistanceMagnitude validation failed"

    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> Result[DistanceMagnitude]:
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
            bool: True if coordinate passes validation. In testing only ever returns
                true. It throws an exception if any validation condition is not met.
        
        Raises:
            NullDistanceMagnitudeException: if t is null
            
            TypeError: if t is not Coordinate
.
            CoordinateValidationException: Wraps any
                (NullCoordinate, TypeError, RowOutOfBounds or ColumnOutOfBoundsException)
                
        """
        try:
            if t is None:
                raise NullDistanceMagnitudeException(
                    f"{method} NullDistanceMagnitudeException.DEFAULT_MESSAGE"
)

            if not isinstance(t, DistanceMagnitude):
                raise TypeError(f"{method} Expected a DistanceMagnitude, got {type(t).__name__}")

            cartesian_distance = cast(DistanceMagnitude, t)

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