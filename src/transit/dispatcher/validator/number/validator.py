# src/transit/dispatcher/validator/number/validator.py

"""
Module: transit.dispatcher.validator.number.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from assurance import PrimingValidator
from err import (
    NegativeNumberException, NumberAboveBoundsException, NumberBelowBoundsException, NumberNullException,
    NumberValidatorException
)
from artifcat import ValidationResult
from util import LoggingLevelRouter


class NumberValidator:
    """
    Role
        -  Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a number instance iss within bounds before use.

    Attributes:

    Provides:
        - def validate(
                    candidate: Any,
                    floor: int = 0,
                    ceiling: int = BOARD_DIMENSION,
            ) -> ValidationResult[int]:
    
    Super Class:
        Validator
    """
    _priming_validator: Optional[PrimingValidator]
    
    def __init__(self, priming_validator: Optional[PrimingValidator] | None = None):
        """
        Args:
            priming_validator: Optional[PrimingValidator]
        """
        self._priming_validator = priming_validator or PrimingValidator()
        
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
            floor: int | None = 0,
            ceiling: int | None = config.setting.board.dimension.config.board_size - 1,
    ) -> ValidationResult[int]:
        """
        Make sure an object is a number within bounds before use.
        
        Action:
            1.  Send an exception in the Validation result if any of these conditions occur
                    -  Not null
                    -  int between floor and ceiling
        Args:
            candidate: Any
            floor: int
            ceiling: int
        Returns:
            ValidationResult[int]
        Raises:
            NegativeNumberException
            NumberAboveBoundsException
            NumberBelowBoundsException
            NumberValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        
        # Handle the case that, the validator is not primed.
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
        
        # Handle the case that, the number
        if floor < 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NumberValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NumberValidatorException.MSG,
                    err_code=NumberValidatorException.ERR_CODE,
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
        # Handle case that the number is above the floor
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