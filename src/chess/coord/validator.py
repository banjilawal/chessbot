from typing import cast, Generic

from chess.geometry.exception.coord import CoordValidationException
from chess.result import Result
from chess.common.validator import Validator, T
from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.exception.coord_exception import (
    RowBelowBoundsException, RowAboveBoundsException,
    ColumnBelowBoundsException, ColumnAboveBoundsException
)

from chess.coord.coord_exception.null.coord_null import NullCoordException
from chess.coord.coord_exception.null.col_null import NullColumnException
from chess.coord.coord_exception.null.row_null import NullRowException
from chess.coord import Coord


class CoordValidator(Validator):
    """
    Validates existing `Coord` instances that are passed around the system. While `CoordBuilder` ensures 
    valid Coords are created, `CoordValidator` checks `Coord` instances that already exist - whether they
    came from deserialization, external sources, or need re-validation after modifications. For performance and 
    single source of truth CoordValidator has:
        - No fields
        - only static method validate  
          
    Usage:
        ```python
        from typing import cast
        from chess.Coord import Coord, CoordValidator
        
        # Validate an existing Coord
        Coord_validation = CoordValidator.validate(candidate)    
        if not Coord_validation.is_success():
            raise Coord_validation.exception
            
        # Cast the payload to a Coord instance to make sure it will work correctly and to avoid type or 
        # null errors that might be difficult to detect.
        Coord = cast(Coord, Coord_validation.payload)
        ```
    
    Use `CoordBuilder` for construction, `CoordValidator` for verification.
    """

    @staticmethod
    def validate(t: Generic[T]) -> Result[Coord]:
        """
        Validates that an existing `Coord` instance meets all specifications. Performs comprehensive validation
        on a `Coord` instance that already exists, checking type safety, null values, and component bounds. 
        Unlike CoordBuilder which creates new valid Coords, `CoordValidator` verifies existing `Coord` 
        instances from external sources, deserialization, or after modifications.

        Args:
        t (Generic[T]): The object to validate, expected to be a Coord instance.

        Returns:
        Result[Coord]: A Result containing either:
            - On success: The validated Coord instance in the payload
            - On failure: Error information and exception details

        Raises:
        CoordValidationException: Wraps any specification violations including:
            - NullCoordException: if input is None
            - TypeError: if input is not a Coord instance
            - NullXComponentException: if Coord.x is None
            - RowBelowBoundsException: If coord.row < 0
            - RowAboveBoundsException: If coord.row >= ROW_SIZE    
            - ColumnBelowBoundsException: If coord.column < 0
            - ColumnAboveBoundsException: If coord.column>= ROW_SIZE
              
        Note:
        *   Use CoordBuilder for creating new Coords with validation,
        *   use CoordValidator for verifying existing Coord instances.
        
        Example:
        ```python
        from typing import cast
        from chess.Coord import Coord, CoordValidator

        validation = CoordValidator.validate(candidate)
        if validation.is_success():
            raise validation.exception
        Coord = cast(Coord, validation.payload)
        ```
        """
        
        method = "CoordValidator.validate"
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