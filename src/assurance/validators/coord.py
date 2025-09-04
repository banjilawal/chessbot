from typing import cast, Generic

from assurance.exception.validation.coord import CoordValidationException
from assurance.result.base import Result
from assurance.validators.base import Validator, T
from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.exception.coord import (
    RowBelowBoundsException, RowAboveBoundsException,
    ColumnBelowBoundsException, ColumnAboveBoundsException
)

from chess.exception.null.coord import NullCoordException
from chess.exception.null.column import NullColumnException
from chess.exception.null.row import NullRowException
from chess.geometry.coord import Coord


class CoordValidator(Validator):
    """
    Validates a Coord used in a domain module meets requirements:
        - Is not null.
        - Its fields meet the specifications for the domain.
    Unmet requirements will raise a CoordValidationException

    For performance and single source of truth CoordValidator has:
        - No fields
        - only static method validate
    subclasses must implement validate.
    """

    @staticmethod
    def validate(t: Generic[T]) -> Result[Coord]:
        entity = "Coord"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates a coord meets domain requirements:
            - Not null
            - row is not null
            - column is not null
            - row is within the bounds of the chess chessboard
            - column is within the bounds of the chess chessboard
        Any failed requirement raise an exception wrapped in a CoordValidationException
            
        Args
            t (Coord): coord to validate
            
         Returns:
             Result[T]: A Result object containing the validated payload if all domain requirements 
             are satisfied. CoordValidationException otherwise.
        
        Raises:
            TypeError: if t is not Coord
            NullCoordException: if t is null   

            RowBelowBoundsException: If coord.row < 0
            RowAboveBoundsException: If coord.row >= ROW_SIZE
                
            ColumnBelowBoundsException: If coord.column < 0
            ColumnAboveBoundsException: If coord.column>= ROW_SIZE
                
            CoordValidationException: Wraps any preceding exception     
        """

        try:
            """
            Tests are chained in this specific order for a reason.
            """

            # If t is null no point continuing
            if t is None:
                raise NullCoordException(
                    f"{method} NullCoordException.DEFAULT_MESSAGE"
                )

            # If cannot cast from t to Coord need to break
            if not isinstance(t, Coord):
                raise TypeError(f"{method} Expected a Coord, got {type(t).__name__}")

            # cast and run checks for the fields
            coordinate = cast(Coord, t)

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
                NullCoordException,

                NullRowException,
                RowBelowBoundsException,
                RowAboveBoundsException,

                NullColumnException,
                ColumnBelowBoundsException,
                ColumnAboveBoundsException
        ) as e:
            raise CoordValidationException(
                f"{method}: {CoordValidationException.DEFAULT_MESSAGE}"
            ) from e