from typing import cast, Generic

from assurance.exception.validation.coord import CoordinateValidationException
from assurance.result.base import Result
from assurance.validators.base import Validator, T
from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.exception.coord import (
    RowBelowBoundsException, RowAboveBoundsException,
    ColumnBelowBoundsException, ColumnAboveBoundsException
)

from chess.exception.null.coord import NullCoordinateException
from chess.exception.null.column import NullColumnException
from chess.exception.null.row import NullRowException
from chess.geometry.coord import Coordinate


class CoordinateValidator(Validator):
    """
    Validates a Coordinate used in a domain module meets requirements:
        - Is not null.
        - Its fields meet the specifications for the domain.
    Unmet requirements will raise a CoordinateValidationException

    For performance and single source of truth CoordinateValidator has:
        - No fields
        - only static method validate
    subclasses must implement validate.
    """

    @staticmethod
    def validate(t: Generic[T]) -> Result[Coordinate]:
        entity = "Coordinate"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates a coordinate meets domain requirements:
            - Not null
            - row is not null
            - column is not null
            - row is within the bounds of the chess chessboard
            - column is within the bounds of the chess chessboard
        Any failed requirement raise an exception wrapped in a CoordinateValidationException
            
        Args
            t (Coordinate): coordinate to validate
            
         Returns:
             Result[T]: A Result object containing the validated payload if all domain requirements 
             are satisfied. CoordinateValidationException otherwise.
        
        Raises:
            TypeError: if t is not Coordinate
            NullCoordinateException: if t is null   

            RowBelowBoundsException: If coordinate.row < 0
            RowAboveBoundsException: If coordinate.row >= ROW_SIZE
                
            ColumnBelowBoundsException: If coordinate.column < 0
            ColumnAboveBoundsException: If coordinate.column>= ROW_SIZE
                
            CoordinateValidationException: Wraps any preceding exception     
        """

        try:
            """
            Tests are chained in this specific order for a reason.
            """

            # If t is null no point continuing
            if t is None:
                raise NullCoordinateException(
                    f"{method} NullCoordinateException.DEFAULT_MESSAGE"
                )

            # If cannot cast from t to Coordinate need to break
            if not isinstance(t, Coordinate):
                raise TypeError(f"{method} Expected a Coordinate, got {type(t).__name__}")

            # cast and run checks for the fields
            coordinate = cast(Coordinate, t)

            if coordinate.row is None:
                raise NullRowException(f"{method} {NullRowException.DEFAULT_MESSAGE}")

            if coordinate.row < 0:
                raise RowBelowBoundsException(f"{method} {RowBelowBoundsException.DEFAULT_MESSAGE}")

            if coordinate.row >= ROW_SIZE:
                raise RowAboveBoundsException(f"{method} {RowAboveBoundsException.DEFAULT_MESSAGE}")

            if coordinate.column is None:
                raise NullColumnException(f"{method} {NullColumnException.DEFAULT_MESSAGE}")

            if coordinate.column < 0:
                raise ColumnBelowBoundsException(f"{method} {ColumnBelowBoundsException.DEFAULT_MESSAGE}")

            if coordinate.column >= COLUMN_SIZE:
                raise ColumnAboveBoundsException(f"{method} {ColumnAboveBoundsException.DEFAULT_MESSAGE}")

            # Return the result if checks passed
            return Result(payload=coordinate)

        except (
            TypeError,
            NullCoordinateException,

            NullRowException,
            RowBelowBoundsException,
            RowAboveBoundsException,

            NullColumnException,
            ColumnBelowBoundsException,
            ColumnAboveBoundsException
        ) as e:
            raise CoordinateValidationException(
                f"{method}: {CoordinateValidationException.DEFAULT_MESSAGE}"
            ) from e