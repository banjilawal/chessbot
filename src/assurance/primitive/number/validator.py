# src/assurance/primitive/number/validator.py

"""
Module: assurance.primitive.number.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from assurance import PlayerValidator, PrimingValidator
from config import NumericSetting
from err import (
    NumberAboveBoundsException, NumberBelowBoundsException, NumberNullException,
    NumberValidatorException
)
from artifcat import ValidationResult
from microservice import IdentityService
from util import LoggingLevelRouter


class NumberValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a number instance iss within bounds before use.

    Attributes:

    Provides:
        - def validate(
                    candidate: Any,
                    floor: Optional[int],
                    ceiling: Optional[int],
            ) -> ValidationResult[int]:
    
    Super Class:
    """
    
    def __init__(
            self,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            priming_validator: Optional[PrimingValidator]
        """
        self._priming_validator = priming_validator or PrimingValidator()
        
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
            floor: Optional[int] | None = None,
            ceiling: Optional[int] | None = None,
    ) -> ValidationResult[int]:
        """
        Make sure an object is a number within bounds before use.
        
        Action:
            1.  Send an exception in the Validation result if any of these conditions occur
                    - Not null
                    - int between floor and ceiling
        Args:
            candidate: Any
            floor: Optional[int] = 0
            ceiling: Optional[int] = NumericSetting.ceiling
        Returns:
            ValidationResult[int]
        Raises:
            NegativeNumberException
            NumberAboveBoundsException
            NumberBelowBoundsException
            NumberValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        if floor is None:
            floor = 0
        if ceiling is None:
            ceiling = NumericSetting.ceiling
         
        # Handle the case that the validator is not primed.
        validator_priming_result = self._priming_validator.execute(
            candidate=candidate,
            target_model=int,
            null_exception=NumberNullException(),
        )
        if validator_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
               NumberValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NumberValidatorException.MSG,
                    err_code=NumberValidatorException.ERR_CODE,
                    ex=validator_priming_result.exception,
                )
            )
        # --- Cast the candidate into a Token for additional tests ---#
        number = cast(int, candidate)
        
        # Handle case that the number is below the floor
        if number < floor:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NumberValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NumberValidatorException.MSG,
                    err_code=NumberValidatorException.ERR_CODE,
                    ex=NumberBelowBoundsException(
                        msg=NumberBelowBoundsException.MSG,
                        err_code=NumberBelowBoundsException.ERR_CODE,
                    )
                )
            )
        # Handle case that the number is above the ceiling.
        if number > ceiling:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NumberValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NumberValidatorException.MSG,
                    err_code=NumberValidatorException.ERR_CODE,
                    ex=NumberAboveBoundsException(
                        msg=NumberAboveBoundsException.MSG,
                        err_code=NumberAboveBoundsException.ERR_CODE,
                    )
                )
            )
        return ValidationResult.success(number)