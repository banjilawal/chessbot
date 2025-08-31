from typing import cast, Generic

from assurance.exception.validation.coord import CoordinateValidationException
from assurance.result.base import Result
from assurance.validators.base import Validator, T
from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.exception.coord import ColumnOutOfBoundsException
from chess.exception.coord import RowOutOfBoundsException
from chess.exception.null.coord import NullCoordinateException
from chess.exception.null.column import NullColumnException
from chess.exception.null.row import NullRowException
from chess.geometry.coordinate.coord import Coordinate


class CoordinateValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[Coordinate]:
        entity = "Coordinate"
        class_name = f"{entity}Specification"
        method = f"{class_name}.is_satisfied_by"


        """
        Validates a coordinate with chained exceptions for coordinate meeting specifications:
            - Not null
            - row is not null
            - row is within the bounds of the chess chessboard
            - column is not null
            - column is within the bounds of the chess chessboard
        If either validators fails their exception will be encapsulated in a CoordinateValidationException
            
        Args
            t (Coordinate): coordinate to validate
            
         Returns:
             Result[T]: A Result object containing the validated payload if the specification is satisfied,
                        CoordinateValidationException otherwise.
        
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
                    f"{method} NullCoordinateException.DEFAULT_MESSAGE"
                )

            if not isinstance(t, Coordinate):
                raise TypeError(f"{method} Expected a Coordinate, got {type(t).__name__}")

            coordinate = cast(Coordinate, t)

            if coordinate.row is None:
                raise NullRowException(f"{method} {NullRowException.DEFAULT_MESSAGE}")

            if coordinate.row < 0 or coordinate.row >= ROW_SIZE:
                raise RowOutOfBoundsException(f"{method} {RowOutOfBoundsException.DEFAULT_MESSAGE}")

            if coordinate.column is None:
                raise NullCoordinateException(f"{method} {NullCoordinateException.DEFAULT_MESSAGE}")

            if coordinate.column < 0 or coordinate.column >= COLUMN_SIZE:
                raise ColumnOutOfBoundsException(f"{method} {ColumnOutOfBoundsException.DEFAULT_MESSAGE}")

            return Result(payload=coordinate)

        except (
            NullCoordinateException, TypeError,
            NullRowException, RowOutOfBoundsException,
            NullColumnException, ColumnOutOfBoundsException) as e:
            raise CoordinateValidationException(
                f"{method}: {CoordinateValidationException.DEFAULT_MESSAGE}"
            ) from e