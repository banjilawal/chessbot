# src/transit/dispatcher/validator/struct/register/vector/validator.py

"""
Module: transit.dispatcher.validator.register.vector.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from err import VectorRegisterValidationDispatcherException
from domain.struct.register import VectorRegister
from artifcat import ValidationResult
from transit import VectorRegisterCarrier
from util import LoggingLevelRouter
from transit.dispatcher.validator import RegisterValidationDispatcher


class VectorRegisterValidationDispatcher(RegisterValidationDispatcher[VectorRegister]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a VectorRegister instance is certified safe, reliable, and consistent before use.

    Attributes:
        validator: VectorRegisterValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult{VectorRegister]

    Super Class:
        RegisterValidator
    """
    
    def __init__(
            self,
            validator: VectorRegisterValidator | None = VectorRegisterValidator(),
    ):
        super().__init__(validator=validator or VectorRegisterValidator())
        
    @property
    def validator(self) -> VectorRegisterValidator:
        return cast(VectorRegisterValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[VectorRegisterCarrier]:
        """
        Verify the object is a VectorRegister that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                validator test..
            2.  Otherwise, cast the payload into a VectorRegister and send in the success result.
                success result.
        Args:
            job: Any
        Returns:
            ValidationResult[VectorRegister]
        Raises:
             VectorRegisterValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterValidationDispatcherException.MSG,
                    err_code=VectorRegisterValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            cast(VectorRegisterCarrier, validation.payload)
        )