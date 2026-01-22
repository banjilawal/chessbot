# src/chess/coord/validator/validator.py

"""
Module: chess.coord.validator.validator
Author: Banji Lawal
Created: 2025-08-12
version: 1.0.0
"""

from typing import cast, Any

from chess.coord import Coord, CoordValidationFailedException, NullCoordException
from chess.system import NUMBER_OF_ROWS, Validator, ValidationResult, LoggingLevelRouter, NumberValidator

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
            number_validator: NumberValidator = NumberValidator(),
    ) -> ValidationResult[Coord]:
        """
        # ACTION:
            1.  If the candidate fails existence or type checks send an exception chain in the ValidationResult.
                Else, cast to Coord instance coord.
            2.  If either coord.row or coord.column are not ints bound in the range [0, BOARD_DIMENSION] send an
                exception chain in the ValidationResult. Else, send coord in the ValidationResult.
        # PARAMETERS:
            *   candidate (Any)
            *   validator (NNumberInBoundsValidator)
        # RETURNS:
            *   ValidationResult[Coord] containing either:
                    - On failure: Exception.
                    - On success: Coord in the payload.
        # RAISES:
            * TypeError
            * NullCoordException
            * CoordValidationFailedException
        """
        method = "CoordValidator.validate"
        
        # Handle the case that the candidate does not exist.
        if candidate is None:
            # Return the exception on failure.
            return ValidationResult.failure(
                CoordValidationFailedException(
                    message=f"{method}: {CoordValidationFailedException.DEFAULT_MESSAGE}",
                    ex=NullCoordException(f"{method}: {NullCoordException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the candidate is the wrong type.
        if not isinstance(candidate, Coord):
            # Return the exception on failure.
            return ValidationResult.failure(
                CoordValidationFailedException(
                    message=f"{method}: {CoordValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected a Coord, got {type(candidate).__name__} instead.")
                )
            )
        
        # --- Cast candidate to a Coord for additional tests ---#
        coord = cast(Coord, candidate)
        
        # Handle the case that coord.row is not an int between [0-7] inclusive.
        row_validation = number_validator.validate(floor=0, ceiling=NUMBER_OF_ROWS, candidate=coord.row)
        if row_validation.is_failure:
            # Return the exception on failure.
            return ValidationResult.failure(
                CoordValidationFailedException(
                    message=f"{method}: {CoordValidationFailedException.DEFAULT_MESSAGE}",
                    ex=row_validation.exception
                )
            )
        # Handle the case that coord.column is not an int between [0-7] inclusive.
        column_validation = number_validator.validate(floor=0, ceiling=NUMBER_OF_ROWS, candidate=coord.column)
        if row_validation.is_failure:
            # Return the exception on failure.
            return ValidationResult.failure(
                CoordValidationFailedException(
                    message=f"{method}: {CoordValidationFailedException.DEFAULT_MESSAGE}",
                    ex=column_validation.exception
                )
            )
        # Return the Coord if integrity checks are passed.
        return ValidationResult.success(payload=coord)