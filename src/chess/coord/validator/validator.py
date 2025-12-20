# src/chess/coord/validator.py

"""
Module: chess.coord.validator
Author: Banji Lawal
Created: 2025-08-12
version: 1.0.0
"""

from typing import cast, Any

from chess.coord import Coord, NullCoordException, InvalidCoordException
from chess.system import Validator, ValidationResult, LoggingLevelRouter, NumberInBoundsValidator

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
            number_bounds_validator: NumberInBoundsValidator = NumberInBoundsValidator(),
    ) -> ValidationResult[Coord]:
        """
        # ACTION:
        1.  Confirm the candidate exists and is a Coord object. On meeting both conditions cast the candidate to a coord.
        2.  Confirm Coord.row and Coord.column are within the bounds or the 2D Board array.
        4.  Send an exception in the VAlidationResult if any check fails otherwise, send the certified Coord.
    
        # PARAMETERS:
            *   candidate (Any)
            *   number_bounds_validator (NNumberInBoundsValidato)
    
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
            row_validation = number_bounds_validator.validate(candidate=coord.row)
            if row_validation.is_failure:
                return ValidationResult.failure(row_validation.exception)
            
            # Run column integrity checks.
            column_validation = number_bounds_validator.validate(candidate=coord.column)
            if column_validation.is_failure:
                return ValidationResult.failure(column_validation.exception)
            
            # Return the Coord if integrity checks are passed.
            return ValidationResult.success(payload=coord)
        
        # Finally, if there is an unhandled exception Wrap an InvalidCoordEException around it then return the
        # exception-chain inside the ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCoordException(ex=ex, message=f"{method}: {InvalidCoordException.DEFAULT_MESSAGE}")
            )