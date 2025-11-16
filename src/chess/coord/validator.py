# src/chess/coord/validator.py

"""
Module: chess.coord.validator
Author: Banji Lawal
Created: 2025-08-12
version: 1.0.0
"""

from typing import cast, Any

from chess.system import Validator, ValidationResult, LoggingLevelRouter, ROW_SIZE, COLUMN_SIZE
from chess.coord import (
    Coord, NullCoordException, NullRowException, RowBelowBoundsException, RowAboveBoundsException, NullColumnException,
    ColumnBelowBoundsException, ColumnAboveBoundsException, InvalidCoordException
)


class CoordValidator(Validator[Coord]):
    """
    # ROLE: Validation, Verify Data Integrity
  
    # RESPONSIBILITIES:
    Verifies a candidate is an instance of Coord, that meets integrity requirements, before
    the candidate is used.
  
    # PROVIDES:
    ValidationResult[Coord] containing either:
        - On success: Coord in the payload.
        - On failure: Exception.
  
    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[Coord]:
        """
        # ACTION:
        1.  Check candidate is not null.
        2.  Check if candidate is a Coord.
        3.  Check candidate.row is:
                *   an INT
                *   between 0 and ROW_SIZE - 1 inclusive.
        4.  Check candidate.column is:
                *   an INT
                *   between 0 and ROW_SIZE - 1 inclusive.
        4.  If any check fails, return the exception inside a ValidationResult.
        3.  When all checks pass cast candidate to a Coord instance then return inside a ValidationResult.
    
        # PARAMETERS:
            *   candidate (Any): Object to validate.
    
        # Returns:
        ValidationResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.
    
        # RAISES:
            * TypeError
            * NullCoordException
            * NullRowException
            * RowBelowBoundsException
            * RowAboveBoundsException
            * NullColumnException
            * ColumnBelowBoundsException
            * ColumnAboveBoundsException
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
                    TypeError(f"{method}: Expected Coord, got {type(candidate).__name__} instead.")
                )
            
            coord = cast(Coord, candidate)
            
            if coord.row is None:
                return ValidationResult.failure(
                    NullRowException(f"{method}: {NullRowException.DEFAULT_MESSAGE}")
                )
            
            if coord.row < 0:
                return ValidationResult.failure(
                    RowBelowBoundsException(
                        f"{method}: {RowBelowBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if coord.row >= ROW_SIZE:
                return ValidationResult.failure(
                    RowAboveBoundsException(
                        f"{method}: {RowAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if coord.column is None:
                return ValidationResult.failure(
                    NullColumnException(
                        f"{method}: {NullColumnException.DEFAULT_MESSAGE}"
                    )
                )
            
            if coord.column < 0:
                return ValidationResult.failure(
                    ColumnBelowBoundsException(
                        f"{method}: {ColumnBelowBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if coord.column >= COLUMN_SIZE:
                return ValidationResult.failure(
                    ColumnAboveBoundsException(
                        f"{method}: {ColumnAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(payload=coord)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCoordException(
                    f"{method}: {InvalidCoordException.DEFAULT_MESSAGE}",
                    ex
                )
            )
