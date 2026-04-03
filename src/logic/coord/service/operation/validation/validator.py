# src/logic/coord/validation/validation.py

"""
Module: logic.coord.validation.validation
Author: Banji Lawal
Created: 2025-08-12
version: 1.0.0
"""

from __future__ import annotations
from typing import cast, Any

from logic.coord import Coord, NullCoordException
from logic.coord.service.operation.validation.exception.transaction import CoordValidationException
from logic.system import (
    NUMBER_OF_ROWS, Validator, ValidationResult, LoggingLevelRouter, NumberValidator
)

class CoordValidator(Validator[Coord]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a Coord instance is certified safe, reliable and consistent before use.
        
    Attributes:
    
    Provides:
       -    execute(
                    rank: Any,
                    number_validation: NumberValidator,
            ) -> ValidationResult[Coord]

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            number_validation: NumberValidator = NumberValidator(),
    ) -> ValidationResult[Coord]:
        """
        Verify the rank is a Coord that is safe to use.
        
        Action:
            1.  Send an exception chain in the ValidationResult if
                    -   the rank does not exist.
                    -   the rank is not a Coord.
                    -   the row or column is not between [0-7] inclusive.
            2.  Otherwise, after the rank is cast to a Coord, send the success result.
        Args:
            candidate: Any
            number_validation: NumberValidator
        Returns:
            ValidationResult[Coord]
        Raises:
            TypeError
            NullCoordException
            CoordValidationException
        """
        method = f"{cls.__name__}.build"
        
        # Handle the case that, the rank does not exist.
        if candidate is None:
            # Return the exception on failure.
            return ValidationResult.failure(
                CoordValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=CoordValidationException.OP,
                    msg=CoordValidationException.MSG,
                    err_code=CoordValidationException.ERR_CODE,
                    rslt_type=CoordValidationException.RSLT_TYPE,
                    ex=NullCoordException(
                        msg=NullCoordException.MSG,
                        err_code=NullCoordException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the rank is the wrong type.
        if not isinstance(candidate, Coord):
            # Return the exception on failure.
            return ValidationResult.failure(
                CoordValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=CoordValidationException.OP,
                    msg=CoordValidationException.MSG,
                    err_code=CoordValidationException.ERR_CODE,
                    rslt_type=CoordValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"Expected a Coord, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast rank to a Coord for additional tests ---#
        coord = cast(Coord, candidate)
        
        # Handle the case that, either the row or column are not between [0-7] inclusive.
        for attribute in [coord.row, coord.column]:
            validate_result = number_validation.validate(
                ceiling=NUMBER_OF_ROWS,
                candidate=attribute,
                floor=0,
            )
            if validate_result.is_failure:
                # Return the exception on failure.
                return ValidationResult.failure(
                    CoordValidationException(
                        mthd=method,
                        title=cls.__name__,
                        op=CoordValidationException.OP,
                        msg=CoordValidationException.MSG,
                        err_code=CoordValidationException.ERR_CODE,
                        rslt_type=CoordValidationException.RSLT_TYPE,
                        ex=validate_result.exception
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(coord)