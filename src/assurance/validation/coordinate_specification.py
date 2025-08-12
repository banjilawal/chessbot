from typing import Generic, cast

from assurance.validation.specification import Specification, T
from assurance.validation.validation_exception import CoordinateValidationException
from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.exception.null.null import NullCoordinateException
from chess.geometry.coordinate.coordinate import Coordinate, RowOutOfBoundsException, ColumnOutOfBoundsException


class CoordinateSpecification(Specification):

    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> bool:
        method = "CoordinateSpecification.is_satisfied_by"

        """
        Validates a coordinate with chained exceptions for coordinate meeting specifications:
            - Not null
            - Within the bounds of the chess board
        If either validation fails their exception will be encapsulated in a CoordinateValidationException
            
        Args
            t (Coordinate): coordinate to validate
            
        Returns:
            bool: True if coordinate passes validation. In testing only ever returns
                true. It throws an exception if any validation condition is not met.
        
        Raises:

            NullCoordinateException: if t is null
            
            TypeError: if t is not Coordinate
            
            RowOutOfBoundsException: If coordinate.row is outside the range 
                (0, ROW_SIZE - 1) inclusive
                
            ColumnOutOfBoundsException: If coordinate.column is outside the range
                (0, COLUMN_SIZE - 1) inclusive
.
            CoordinateValidationException: Wraps any
                (NullCoordinate, TypeError, RowOutOfBounds or ColumnOutOfBoundsException)
                
        """
        try:
            if t is None:
                raise NullCoordinateException(
                    f"{method} NullCoordinateException.default_message"
                )

            if not isinstance(t, Coordinate):
                raise TypeError(f"{method} Expected a Coordinate, got {type(t).__name__}")

            coordinate = cast(Coordinate, t)

            if coordinate.row < 0 or coordinate.row >= ROW_SIZE:
                raise RowOutOfBoundsException(
                    f"{method} {RowOutOfBoundsException.default_message}"
                )

            if coordinate.column < 0 or coordinate.column >= COLUMN_SIZE:
                raise ColumnOutOfBoundsException(
                    f"{method} {ColumnOutOfBoundsException.default_message}"
                )

            return True

        except (
            NullCoordinateException, TypeError,
            RowOutOfBoundsException, ColumnOutOfBoundsException) as e:
            raise CoordinateValidationException(
                f"{method} CoordinateValidationException.default_message") from e