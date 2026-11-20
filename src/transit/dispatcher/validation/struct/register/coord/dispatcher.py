# src/transit/dispatcher/validator/struct/register/coordRegister/dispatcher.py

"""
Module: transit.dispatcher.validator.register.coordRegister.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import CoordRegisterValidator
from domain import CoordRegister
from err import CoordRegisterValidationDispatcherException
from transit import ValidationDispatcher, CoordRegisterCarrier
from util import LoggingLevelRouter


class CoordRegisterValidationDispatcher(ValidationDispatcher[CoordRegister]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute CoordRegister validation jobs among workers, then forward
            their results.

    Attributes:
        validator: CoordRegisterValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """
    
    def __init__(
            self,
            validator: Optional[CoordRegisterValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[CoordRegisterValidator]
        """
        super().__init__(validator=validator or CoordRegisterValidator())
    
    @property
    def validator(self) -> CoordRegisterValidator:
        return cast(CoordRegisterValidator, super().validator)
    
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[CoordRegisterCarrier]:
        """
        Send jobs to a CoordRegisterValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
            2.  Otherwise, cast the job payload into a CoordRegisterCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[CoordRegisterCarrier]
        Raises:
             CoordRegisterValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordRegisterValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterValidationDispatcherException.MSG,
                    err_code=CoordRegisterValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(CoordRegisterCarrier, validation.payload)
        return ValidationResult.success(carrier)