# src/transit/dispatcher/validator/struct/binder/team/dispatcher.py

"""
Module: transit.dispatcher.validator.binder.team.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from err import TeamBinderValidationDispatcherException
from domain.struct.binder import TeamBinder
from artifcat import ValidationResult
from transit import TeamBinderCarrier
from util import LoggingLevelRouter
from transit.dispatcher.validator import BinderValidationDispatcher


class TeamBinderValidationDispatcher(BinderValidationDispatcher[TeamBinder]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TeamBinder instance is certified safe, reliable, and consistent before use.

    Attributes:
        validator: TeamBinderValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult{TeamBinder]

    Super Class:
        BinderValidator
    """
    
    def __init__(
            self,
            validator: TeamBinderValidator | None = TeamBinderValidator(),
    ):
        super().__init__(validator=validator or TeamBinderValidator())
        
    @property
    def validator(self) -> TeamBinderValidator:
        return cast(TeamBinderValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[TeamBinderCarrier]:
        """
        Verify the object is a TeamBinder that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                validator test..
            2.  Otherwise, cast the payload into a TeamBinder and send in the success result.
                success result.
        Args:
            job: Any
        Returns:
            ValidationResult[TeamBinder]
        Raises:
             TeamBinderValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
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
        return ValidationResult.success(
            cast(TeamBinderCarrier, validation.payload)
        )