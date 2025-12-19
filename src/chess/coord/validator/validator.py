# src/chess/coord/validator.py

"""
Module: chess.coord.validator
Author: Banji Lawal
Created: 2025-08-12
version: 1.0.0
"""

from typing import cast, Any


from chess.system import NumberValidator, Validator, ValidationResult, LoggingLevelRouter, ROW_SIZE, COLUMN_SIZE
from chess.coord import (
    Coord, NegativeRowException, NullCoordException, NullRowException, RowBelowBoundsException, RowAboveBoundsException,
    NullColumnException, ColumnBelowBoundsException, ColumnAboveBoundsException, InvalidCoordException,
)


class CoordValidator(Validator[Coord]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a Coord instance is certified safe, reliable and consistent before use.
    2.  Return useful debugging information if a candidate does not satisfy Coord integrity constraints.

    # PARENT:
        *   Validator

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            number_validator: NumberValidator = NumberValidator()
    ) -> ValidationResult[Coord]:
        """
        # ACTION:
        1.  Confirm the candidate exists and is a Coord object. On meeting both conditions cast the candidate to a coord.
        2.  Check coord.row is an int between (0, ROW_SIZE - 1) inclusive.
        3.  Check coord.column is an int between (0, COLUMN_SIZE - 1) inclusive.
        4.  If any check fails, return the exception inside a ValidationResult. Otherwise, pass the candidate in the
            ValidationResult.
    
        # PARAMETERS:
            *   candidate (Any)
    
        # Returns:
        ValidationResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.
    
        # RAISES:
            * TypeError
            * NullCoordException
            * InvalidCoordException
        """
        method = "CoordValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullCoordException(f"{method}: {NullCoordException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Coord):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected a Coord, got {type(candidate).__name__} instead.")
                )
            
            coord = cast(Coord, candidate)
            
            row_validation = cls.validate_row(candidate=coord.row, number_validator=number_validator)
            if row_validation.is_failure:
                return ValidationResult.failure(row_validation.exception)
            
            column_validation = cls.validate_column(candidate=coord.column)
            if column_validation.is_failure:
                return ValidationResult.failure(column_validation.exception)
            
            return ValidationResult.success(payload=coord)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCoordException(ex=ex, message=f"{method}: {InvalidCoordException.DEFAULT_MESSAGE}")
            )
        
        
    @classmethod
    def validate(
            cls,
            candidate: Any,
            number_validator: NumberValidator = NumberValidator()
    ) -> ValidationResult[int]:
        """
        # ACTION:
        1.  If number_validator confirms candidate is an int, cast the candidate to row.
        2.  Test the number is not negative.
        3.  Test the number is less than ROW_SIZE.
        4.  If any check fails, return the exception inside a ValidationResult. Otherwise, send the number back in the
            ValidationResult.

        # PARAMETERS:
            *   candidate (Any)
            *   number_validator (NumberValidator)

        # Returns:
        ValidationResult[int] containing either:
            - On success: int in the payload.
            - On failure: Exception.

        # RAISES:
            * NegativeRowException
            * RowAboveBoundsException
            * InvalidCoordException
        """
        method = "CoordValidator.validate_row"
        try:
            # Run tests to an int.
            number_validation = number_validator.validate(candidate=candidate)
            if number_validation.is_failure:
                return ValidationResult.failure(number_validation.exception)
            # Cast to doubly make sure the payload is an int if number validation i successful.
            number = cast(int, number_validation.payload)
            
            # Return an exception if the number is negative.
            if number < 0:
                return ValidationResult.failure(
                    NegativeRowException(f"{method}: {NegativeRowException.DEFAULT_MESSAGE}")
                )
            
            if number > ROW_SIZE - 1:
                return ValidationResult.failure(
                    RowAboveBoundsException(f"{method}: {RowAboveBoundsException.DEFAULT_MESSAGE}")
                )

            return ValidationResult.success(payload=number)
            
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCoordException(ex=ex, message=f"{method}: {InvalidCoordException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    def validate_column(
            cls,
            candidate: Any,
            number_validator: NumberValidator = NumberValidator()
    ) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Check candidate is not validation.
        2.  Check if candidate is an INT
        3.  Check if candidate is between 0 and COLUMN_SIZE - 1 inclusive.
        4.  If any check fails, return the exception inside a ValidationResult.
        3.  When all checks pass cast candidate to a int then return inside a ValidationResult.

        # PARAMETERS:
            *   candidate (Any): Object to validate is a legitimate row

        # Returns:
        ValidationResult[int] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        # RAISES:
            * TypeError
            * NullColumnException
            * ColumnBelowBoundsException
            * ColumnAboveBoundsException
            * InvalidCoordException
        """
        method = "CoordValidator.validate_column"
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullColumnException(
                        f"{method}: "
                        f"{NullColumnException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, int):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: "
                        f"Expected int, got {type(candidate).__name__} instead.")
                )
            
            number = cast(int, candidate)
            
            if number < 0:
                return ValidationResult.failure(
                    ColumnBelowBoundsException(
                        f"{method}: "
                        f"{ColumnBelowBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if number >= COLUMN_SIZE:
                return ValidationResult.failure(
                    ColumnAboveBoundsException(
                        f"{method}: "
                        f"{ColumnAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(payload=number)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCoordException(
                    ex=ex,
                    message=f"{method}: "
                            f"{InvalidCoordException.DEFAULT_MESSAGE}",
                )
            )
