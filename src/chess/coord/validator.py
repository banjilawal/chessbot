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
    Coord, NullCoordException, NullRowException, RowBelowBoundsException, RowAboveBoundsException,
    NullColumnException, ColumnBelowBoundsException, ColumnAboveBoundsException, InvalidCoordException,
    InvalidCoordColumnException, InvalidCoordRowException
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
            * InvalidCoordException
        """
        method = "CoordValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullCoordException(f"{method}: "
                                       f"{NullCoordException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Coord):
                return ValidationResult.failure(
                    TypeError(f"{method}: "
                              f"Expected Coord, got {type(candidate).__name__} instead.")
                )
            
            coord = cast(Coord, candidate)
            
            row_validation = cls.validate_row(candidate=coord.row)
            if row_validation.is_failure():
                return ValidationResult.failure(row_validation.exception)
            
            column_validation = cls.validate_column(candidate=coord.column)
            if column_validation.is_failure():
                return ValidationResult.failure(column_validation.exception)
            
            return ValidationResult.success(payload=coord)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCoordException(
                    ex=ex,
                    message=f"{method}: "
                            f"{InvalidCoordException.DEFAULT_MESSAGE}",
                )
            )
        
        
    @classmethod
    def validate_row(cls, candidate: Any) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Check candidate is not null.
        2.  Check if candidate is an INT
        3.  Check if candidate is between 0 and ROW_SIZE - 1 inclusive.
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
            * NullRowException
            * RowBelowBoundsException
            * RowAboveBoundsException
            * InvalidCoordRowException
        """
        method = "CoordValidator.validate_row"
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullRowException(f"{method}: "
                                     f"{NullRowException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, int):
                return ValidationResult.failure(
                    TypeError(f"{method}: "
                              f"Expected int, got {type(candidate).__name__} instead.")
                )
            
            number = cast(int, candidate)
            
            if number < 0:
                return ValidationResult.failure(
                    RowBelowBoundsException(
                        f"{method}: {RowBelowBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if number >= ROW_SIZE:
                return ValidationResult.failure(
                    RowAboveBoundsException(
                        f"{method}: "
                        f"{RowAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(payload=number)
            
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCoordRowException(
                    ex=ex,
                    message=f"{method}: "
                            f"{InvalidCoordRowException.DEFAULT_MESSAGE}",
                )
            )
    
    @classmethod
    def validate_column(cls, candidate: Any) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Check candidate is not null.
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
            * InvalidCoordColumnException
        """
        method = "CoordValidator.validate_column"
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullColumnException(f"{method}: "
                                        f"{NullColumnException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, int):
                return ValidationResult.failure(
                    TypeError(f"{method}: "
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
                InvalidCoordColumnException(
                    ex=ex,
                    message=f"{method}: "
                            f"{InvalidCoordColumnException.DEFAULT_MESSAGE}",
                )
            )
