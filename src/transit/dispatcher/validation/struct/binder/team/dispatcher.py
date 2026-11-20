# src/transit/dispatcher/validator/struct/binder/team/dispatcher.py

"""
Module: transit.dispatcher.validator.binder.team.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from assurance import TeamBinderValidator
from artifcat import ValidationResult
from domain import TeamBinder
from err import TeamBinderValidationDispatcherException
from transit import TeamBinderCarrier, ValidationDispatcher
from util import LoggingLevelRouter


class TeamBinderValidationDispatcher(ValidationDispatcher[TeamBinder]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute TeamBinder validation jobs among workers, then forward their results.

    Attributes:
        validator: TeamBinderValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """
    
    def __init__(
            self,
            validator: Optional[TeamBinderValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[TeamBinderValidator]
        """
        super().__init__(validator=validator or TeamBinderValidator())
    
    @property
    def validator(self) -> TeamBinderValidator:
        return cast(TeamBinderValidator, super().validator)
    
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[TeamBinderCarrier]:
        """
        Send jobs to a TeamBinderValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
            2.  Otherwise, cast the job payload into a TeamBinderCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[TeamBinderCarrier]
        Raises:
             TeamBinderValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderValidationDispatcherException.MSG,
                    err_code=TeamBinderValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(TeamBinderCarrier, validation.payload)
        return ValidationResult.success(carrier)