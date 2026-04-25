# src/operation/validation/number/operation.py

"""
Module: operation.validation.number.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from err import (
    NegativeNumberException, NumberAboveBoundsException, NumberBelowBoundsException, NumberNullException,
    NumberValidationException
)
from integrity import Validator
from result import ValidationResult
from system import BOARD_DIMENSION, LoggingLevelRouter


class NumberValidator(Validator[int]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a number instance iss within bounds before use.

    Attributes:

    Provides:
        -   def validate(
                    candidate: Any,
                    floor: int = 0,
                    ceiling: int = BOARD_DIMENSION,
            ) -> ValidationResult[int]:
    
    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            floor: int = 0,
            ceiling: int = BOARD_DIMENSION-1,
    ) -> ValidationResult[int]:
        """
        Make sure an object is a number within bounds before use.
        
        Action:
            1.  Send an exception in the Validation result if any of these conditions occur
                    -   Not null
                    -   int between floor and ceiling
        Args:
            candidate: Any
            floor: int
            ceiling: int
        Returns:
            ValidationResult[int]
        Raises:
            TypeError
            NumberException
        # ACTION:
            1.  If rank fails not-negative validation return the validation result containing the exception.
                Else get the number from the validation payload.
            2.  If number > BOARD.DIMENSION -1 return the ValidationResult containing the exception.
            3.  The tests have been passed. Return the ValidationResult with the number in the payload.
        # PARAMETERS:
            *   rank (Any)
            *   not_negative_validator (NotNegativeNumberValidator)
        # RETURNS:
            *   ValidationResult[int] containing either:
                    - On failure: Exception.
                    - On success: int in the payload.
        Raises:
              *     NumberValidationException
              *     NumberBelowFloorException
              *     NumberAboveCeilingException
        """
        method = f"{cls.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NumberValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NumberValidationException.MSG,
                    err_code=NumberValidationException.ERR_NONE,
                    ex=NumberNullException(
                        msg=NumberNullException.MSG,
                        err_code=NumberNullException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, int):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NumberValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NumberValidationException.MSG,
                    err_code=NumberValidationException.ERR_NONE,
                    ex=TypeError(f"Expected an integer, got {type(candidate).__name__} instead.")
                )
            )
        number = cast(int, candidate)
        # Handle the case that, the number
        if floor < 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NumberValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NumberValidationException.MSG,
                    err_code=NumberValidationException.ERR_NONE,
                    ex=NegativeNumberException(
                        var="floor",
                        val=number,
                        msg=f"Floor cannot be negative",
                        err_code=NegativeNumberException.ERR_CODE,
                    )
                )
            )
        # Handle case that the number is below the floor
        if number < floor:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NumberValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NumberValidationException.MSG,
                    err_code=NumberValidationException.ERR_NONE,
                    ex=NumberBelowBoundsException(
                        msg=NumberBelowBoundsException.MSG,
                        err_code=NumberBelowBoundsException.ERR_CODE,
                    )
                )
            )
        # Handle case that the number is above the floor
        if number > ceiling:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NumberValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NumberValidationException.MSG,
                    err_code=NumberValidationException.ERR_NONE,
                    ex=NumberAboveBoundsException(
                        msg=NumberAboveBoundsException.MSG,
                        err_code=NumberAboveBoundsException.ERR_CODE,
                    )
                )
            )
        # On certification success return the number in the ValidationResult
        return ValidationResult.success(number)