# src/transit/dispatcher/validator/struct/register/squareRegister/dispatcher.py

"""
Module: transit.dispatcher.validator.register.squareRegister.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import SquareRegisterValidator
from domain import SquareRegister
from err import SquareRegisterValidationDispatcherException
from transit import ValidationDispatcher, SquareRegisterCarrier
from util import LoggingLevelRouter


class SquareRegisterValidationDispatcher(ValidationDispatcher[SquareRegister]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute SquareRegister validation jobs among workers, then forward
            their results.

    Attributes:
        validator: SquareRegisterValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """
    
    def __init__(
            self,
            validator: Optional[SquareRegisterValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[SquareRegisterValidator]
        """
        super().__init__(validator=validator or SquareRegisterValidator())
    
    @property
    def validator(self) -> SquareRegisterValidator:
        return cast(SquareRegisterValidator, super().validator)
    
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[SquareRegisterCarrier]:
        """
        Send jobs to a SquareRegisterValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
            2.  Otherwise, cast the job payload into a SquareRegisterCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[SquareRegisterCarrier]
        Raises:
             SquareRegisterValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
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
        carrier = cast(SquareRegisterCarrier, validation.payload)
        return ValidationResult.success(carrier)