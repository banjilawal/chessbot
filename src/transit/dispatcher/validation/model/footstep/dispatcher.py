# src/transit/dispatcher/validator/model/footstep/dispatcher.py

"""
Module: transit.dispatcher.validator.model.footstep.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast


from assurance import FootstepValidator
from artifcat import ValidationResult
from domain import Footstep
from err import FootstepValidationDispatcherException
from transit import ValidationDispatcher, FootstepCarrier
from util import LoggingLevelRouter


class FootstepValidationDispatcher(ValidationDispatcher[Footstep]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute Footstep validation jobs among workers, then forward their results.

    Attributes:
        validator: FootstepValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """

    def __init__(
            self,
            validator: Optional[FootstepValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[FootstepValidator]
        """
        super().__init__(validator=validator or FootstepValidator())
        
    @property
    def validator(self) -> FootstepValidator:
        return cast(FootstepValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[FootstepCarrier]:
        """
        Send jobs to a FootstepValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
            2.  Otherwise, cast the job payload into a FootstepCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[FootstepCarrier]
        Raises:
             FootstepValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
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
        carrier = cast(FootstepCarrier, validation.payload)
        return ValidationResult.success(carrier)