# src/transit/dispatcher/validator/struct/register/square/validator.py

"""
Module: transit.dispatcher.validator.register.square.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from assurance import SquareRegisterValidator
from err import SquareRegisterValidationDispatcherException
from domain.struct.register import SquareRegister
from artifcat import ValidationResult
from transit import SquareRegisterCarrier
from util import LoggingLevelRouter
from transit.dispatcher.validator import RegisterValidationDispatcher


class SquareRegisterValidationDispatcher(RegisterValidationDispatcher[SquareRegister]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a SquareRegister instance is certified safe, reliable, and consistent before use.

    Attributes:
        validator: SquareRegisterValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult{SquareRegister]

    Super Class:
        RegisterValidator
    """
    
    def __init__(
            self,
            validator: SquareRegisterValidator | None = SquareRegisterValidator(),
    ):
        super().__init__(validator=validator or SquareRegisterValidator())
        
    @property
    def validator(self) -> SquareRegisterValidator:
        return cast(SquareRegisterValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[SquareRegisterCarrier]:
        """
        Verify the object is a SquareRegister that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                validator test..
            2.  Otherwise, cast the payload into a SquareRegister and send in the success result.
                success result.
        Args:
            job: Any
        Returns:
            ValidationResult[SquareRegister]
        Raises:
             SquareRegisterValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidationDispatcherException.MSG,
                    err_code=SquareRegisterValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            cast(SquareRegisterCarrier, validation.payload)
        )