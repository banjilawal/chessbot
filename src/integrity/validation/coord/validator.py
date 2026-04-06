# src/integrity/validation/coord/validator.py

"""
Module: integrity.validation.coord.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any

from err import CoordNullException, CoordValidationException
from integrity import NumberValidator, Validator
from model import Coord
from result import ValidationResult
from system import LoggingLevelRouter, NUMBER_OF_ROWS


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
                    coord: Any,
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
        Verify the coord is a Coord that is safe to use.
        
        Action:
            1.  Send an exception chain in the ValidationResult if
                    -   the coord does not exist.
                    -   the coord is not a Coord.
                    -   the row or column is not between [0-7] inclusive.
            2.  Otherwise, after the coord is cast to a Coord, send the success result.
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
        
        # Handle the case that, the coord does not exist.
        if candidate is None:
            # Return the exception on failure.
            return ValidationResult.failure(
                CoordValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=CoordValidationException.MSG,
                    err_code=CoordValidationException.ERR_CODE,
                    ex=CoordNullException(
                        msg=CoordNullException.MSG,
                        err_code=CoordNullException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the coord is the wrong type.
        if not isinstance(candidate, Coord):
            # Return the exception on failure.
            return ValidationResult.failure(
                CoordValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=CoordValidationException.MSG,
                    err_code=CoordValidationException.ERR_CODE,
                    ex=TypeError(
                        f"Expected a Coord, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast coord to a Coord for additional tests ---#
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
                        cls_mthd=method,
                        cls_name=method.__name__,
                        msg=CoordValidationException.MSG,
                        err_code=CoordValidationException.ERR_CODE,
                        ex=validate_result.exception
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(coord)