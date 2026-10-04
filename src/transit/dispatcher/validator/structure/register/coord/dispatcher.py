# src/transit/dispatcher/validator/structure/register/coord/validator.py

"""
Module: transit.dispatcher.validator.register.coord.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from assurance import CoordRegisterValidator
from err import CoordRegisterValidationDispatcherException
from domain.structure.register import CoordRegister
from artifcat import ValidationResult
from transit import CoordRegisterCarrier
from util import LoggingLevelRouter
from transit.dispatcher.validator import RegisterValidationDispatcher


class CoordRegisterValidationDispatcher(RegisterValidationDispatcher[CoordRegister]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a CoordRegister instance is certified safe, reliable, and consistent before use.

    Attributes:
        validator: CoordRegisterValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult{CoordRegister]

    Super Class:
        RegisterValidator
    """
    
    def __init__(
            self,
            validator: CoordRegisterValidator | None = CoordRegisterValidator(),
    ):
        super().__init__(validator=validator or CoordRegisterValidator())
        
    @property
    def validator(self) -> CoordRegisterValidator:
        return cast(CoordRegisterValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[CoordRegisterCarrier]:
        """
        Verify the object is a CoordRegister that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                validator test..
            2.  Otherwise, cast the payload into a CoordRegister and send in the success result.
                success result.
        Args:
            job: Any
        Returns:
            ValidationResult[CoordRegister]
        Raises:
             CoordRegisterValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
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
        return ValidationResult.success(
            cast(CoordRegisterCarrier, validation.payload)
        )