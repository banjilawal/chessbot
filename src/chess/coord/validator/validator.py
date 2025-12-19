# src/chess/coord/validator.py

"""
Module: chess.coord.validator
Author: Banji Lawal
Created: 2025-08-12
version: 1.0.0
"""

from typing import cast, Any

from chess.system import (
    NotNegativeNumberValidator, Validator, ValidationResult, LoggingLevelRouter, ROW_SIZE, COLUMN_SIZE
)
from chess.coord import (
    Coord, NullCoordException, RowAboveBoundsException, ColumnAboveBoundsException, InvalidCoordException,
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
            number_validator: NotNegativeNumberValidator = NotNegativeNumberValidator()
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
            *   number_validator (NotNegativeNumberValidator)
    
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
            # Test the candidate exists.
            if candidate is None:
                return ValidationResult.failure(
                    NullCoordException(f"{method}: {NullCoordException.DEFAULT_MESSAGE}")
                )
            # Test the candidate is an int before proceeding.
            if not isinstance(candidate, Coord):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected a Coord, got {type(candidate).__name__} instead.")
                )
            
            # Cast candidate to an int after the existence and type checks pass.
            coord = cast(Coord, candidate)
            
            # Run row integrity checks.
            row_validation = cls.validate_row(candidate=coord.row, number_validator=number_validator)
            if row_validation.is_failure:
                return ValidationResult.failure(row_validation.exception)
            
            # Run column integrity checks.
            column_validation = cls.validate_column(candidate=coord.column)
            if column_validation.is_failure:
                return ValidationResult.failure(column_validation.exception)
            
            # Return the number if integrity checks are passed.
            return ValidationResult.success(payload=coord)
        # Finally, if there is an unhandled exception Wrap an InvalidCoordEException around it then return the
        # exception-chain inside the ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCoordException(ex=ex, message=f"{method}: {InvalidCoordException.DEFAULT_MESSAGE}")
            )
        
        
    @classmethod
    def validate_row(
            cls,
            candidate: Any,
            number_validator: NotNegativeNumberValidator = NotNegativeNumberValidator()
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
            * RowAboveBoundsException
            * InvalidCoordException
        """
        method = "CoordValidator.validate_row"
        try:
            # Verify candidate is an at-least-zero number.
            number_validation =number_validator.validate(candidate=candidate)
            if number_validation.is_failure:
                return ValidationResult.failure(number_validation.exception)
            # Cast to doubly make sure the payload is an int if not-negative number verification succeeds.
            number = cast(int, number_validation.payload)
            
            # Handle the case that the number is exceeds the row array's upper bound.
            if number > ROW_SIZE - 1:
                return ValidationResult.failure(
                    RowAboveBoundsException(f"{method}: {RowAboveBoundsException.DEFAULT_MESSAGE}")
                )
            # Return the number if integrity checks are passed.
            return ValidationResult.success(payload=number)
        # Finally, if there is an unhandled exception Wrap an InvalidCoordEException around it then return the
        # exception-chain inside the ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCoordException(ex=ex, message=f"{method}: {InvalidCoordException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    def validate_column(
            cls,
            candidate: Any,
            number_validator: NotNegativeNumberValidator = NotNegativeNumberValidator()
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
            *   number_validator (NotNegativeNumberValidator)

        # Returns:
        ValidationResult[int] containing either:
            - On success: int in the payload.
            - On failure: Exception.

        # RAISES:
            * ColumnAboveBoundsException
            * InvalidCoordException
        """
        method = "CoordValidator.validate_column"
        try:
            # Verify candidate is an at-least-zero number.
            number_validation = number_validator.validate(candidate=candidate)
            if number_validation.is_failure:
                return ValidationResult.failure(number_validation.exception)
            # Cast to doubly make sure the payload is an int if not-negative number verification succeeds.
            number = cast(int, number_validation.payload)
            
            # Handle the case that the number is exceeds the column array's upper bound.
            if number > COLUMN_SIZE - 1:
                return ValidationResult.failure(
                    ColumnAboveBoundsException(f"{method}: {ColumnAboveBoundsException.DEFAULT_MESSAGE}")
                )
            # Return the number if integrity checks are passed.
            return ValidationResult.success(payload=number)
        # Finally, if there is an unhandled exception Wrap an InvalidCoordEException around it then return the
        # exception-chain inside the ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCoordException(ex=ex, message=f"{method}: {InvalidCoordException.DEFAULT_MESSAGE}")
            )
