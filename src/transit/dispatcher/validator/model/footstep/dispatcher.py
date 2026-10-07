# src/transit/dispatcher/validator/model/footstep/validator.py

"""
Module: transit.dispatcher.validator.model.footstep.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from assurance import FootstepValidator
from artifcat import ValidationResult
from domain import Footstep
from err import FootstepValidationDispatcherException
from transit import ModelValidationDispatcher, FootstepCarrier
from util import LoggingLevelRouter


class FootstepValidationDispatcher(ModelValidationDispatcher[Footstep]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a Footstep instance is certified safe, reliable, and consistent before use.

    Attributes:
        validator: FootstepValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult{Footstep]

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            validator: FootstepValidator | None = FootstepValidator(),
    ):
        super().__init__(validator=validator or FootstepValidator())
        
    @property
    def validator(self) -> FootstepValidator:
        return cast(FootstepValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[FootstepCarrier]:
        """
        Verify the object is a Footstep that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                validator test..
            2.  Otherwise, cast the payload into a Footstep and send in the success result.
                success result.
        Args:
            job: Any
        Returns:
            ValidationResult[Footstep]
        Raises:
             FootstepValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepValidationDispatcherException.MSG,
                    err_code=FootstepValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            cast(FootstepCarrier, validation.payload)
        )