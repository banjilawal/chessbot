# src/transit/dispatcher/validator/struct/register/vectorRegister/dispatcher.py

"""
Module: transit.dispatcher.validator.register.vectorRegister.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import VectorRegisterValidator
from domain import VectorRegister
from err import VectorRegisterValidationDispatcherException
from transit import ValidationDispatcher, VectorRegisterCarrier
from util import LoggingLevelRouter


class VectorRegisterValidationDispatcher(ValidationDispatcher[VectorRegister]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute VectorRegister validation jobs among workers, then forward
            their results.

    Attributes:
        validator: VectorRegisterValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """
    
    def __init__(
            self,
            validator: Optional[VectorRegisterValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[VectorRegisterValidator]
        """
        super().__init__(validator=validator or VectorRegisterValidator())
    
    @property
    def validator(self) -> VectorRegisterValidator:
        return cast(VectorRegisterValidator, super().validator)
    
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[VectorRegisterCarrier]:
        """
        Send jobs to a VectorRegisterValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
            2.  Otherwise, cast the job payload into a VectorRegisterCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[VectorRegisterCarrier]
        Raises:
             VectorRegisterValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
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
        carrier = cast(VectorRegisterCarrier, validation.payload)
        return ValidationResult.success(carrier)