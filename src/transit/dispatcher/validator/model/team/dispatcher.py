# src/transit/dispatcher/validator/model/team/validator.py

"""
Module: transit.dispatcher.validator.model.team.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import TeamValidator
from artifcat import ValidationResult
from domain import Team
from err import TeamValidationDispatcherException
from transit import ModelValidationDispatcher, TeamCarrier
from util import LoggingLevelRouter


class TeamValidationDispatcher(ModelValidationDispatcher[Team]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the TeamValidation workflow.

    Attributes:
        validator: TeamValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[validatorCarrier]

    Super Class:
        ModelValidationDispatcher
    """

    def __init__(
            self,
            validator: TeamValidator | None = None,
    ):
        super().__init__(validator=validator or TeamValidator())
        
    @property
    def validator(self) -> TeamValidator:
        return cast(TeamValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[TeamCarrier]:
        """
        Forward a job to a TeamValidator then deliver the result.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator cannot
                certify the job's content.
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
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
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