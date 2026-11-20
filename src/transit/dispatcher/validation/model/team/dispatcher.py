# src/transit/dispatcher/validator/model/team/dispatcher.py

"""
Module: transit.dispatcher.validator.model.team.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast


from assurance import TeamValidator
from artifcat import ValidationResult
from domain import Team
from err import TeamValidationDispatcherException
from transit import ValidationDispatcher, TeamCarrier
from util import LoggingLevelRouter


class TeamValidationDispatcher(ValidationDispatcher[Team]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute Team validation jobs among workers, then forward their results.

    Attributes:
        validator: TeamValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """

    def __init__(
            self,
            validator: Optional[TeamValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[TeamValidator]
        """
        super().__init__(validator=validator or TeamValidator())
        
    @property
    def validator(self) -> TeamValidator:
        return cast(TeamValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[TeamCarrier]:
        """
        Send jobs to a TeamValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
            2.  Otherwise, cast the job payload into a TeamCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[TeamCarrier]
        Raises:
             TeamValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidationDispatcherException.MSG,
                    err_code=TeamValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(TeamCarrier, validation.payload)
        return ValidationResult.success(carrier)