# src/validation/number/operation.py

"""
Module: validation.number.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from result import ValidationResult
from system import BOARD_DIMENSION, LoggingLevelRouter
from operation import ValidationPrimer, Validator
from err import (
    NegativeNumberException, NumberAboveBoundsException, NumberBelowBoundsException, NumberNullException,
    NumberValidationException
)


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
                    validation_primer: ValidationPrimer,
            ) -> ValidationResult[int]:
    
    Super Class:
        Validator
    """
    OPERATION_NAME = "number_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            floor: int = 0,
            ceiling: int = BOARD_DIMENSION-1,
            validation_primer: ValidationPrimer | None = None,
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
            validation_primer: ValidationPrimer
        Returns:
            ValidationResult[int]
        Raises:
            NegativeNumberException
            NumberAboveBoundsException
            NumberBelowBoundsException
            NumberValidationException
        """
        method = f"{cls.__name__}.validate"
        
        if validation_primer is None:
            validation_primer = ValidationPrimer()
        
        # Handle the case that, the candidate does not exist.
        validation_bootstrap_result = validation_primer.validate(
            candidate=candidate,
            target_model=int,
            null_exception=NumberNullException(),
        )
        if validation_bootstrap_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
               NumberValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NumberValidationException.MSG,
                    err_code=NumberValidationException.ERR_CODE,
                    ex=validation_bootstrap_result.exception,
                )
            )
        # --- Cast the candidate into a Token for additional tests ---#
        number = cast(int, candidate)
        
        # Handle the case that, the number
        if floor < 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NumberValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NumberValidationException.MSG,
                    err_code=NumberValidationException.ERR_CODE,
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
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NumberValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NumberValidationException.MSG,
                    err_code=NumberValidationException.ERR_CODE,
                    ex=NumberBelowBoundsException(
                        msg=NumberBelowBoundsException.MSG,
                        err_code=NumberBelowBoundsException.ERR_CODE,
                    )
                )
            )
        # Handle case that the number is above the floor
        if number > ceiling:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NumberValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NumberValidationException.MSG,
                    err_code=NumberValidationException.ERR_CODE,
                    ex=NumberAboveBoundsException(
                        msg=NumberAboveBoundsException.MSG,
                        err_code=NumberAboveBoundsException.ERR_CODE,
                    )
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(number)