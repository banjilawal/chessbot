# src/transit/dispatcher/validator/model/arena/validator.py

"""
Module: transit.dispatcher.validator.model.arena.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import ArenaValidator
from artifcat import ValidationResult
from domain import Arena
from err import ArenaValidationDispatcherException
from transit import ModelValidationDispatcher, ArenaCarrier
from util import LoggingLevelRouter


class ArenaValidationDispatcher(ModelValidationDispatcher[Arena]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the ArenaValidation workflow.

    Attributes:
        validator: ArenaValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[validatorCarrier]

    Super Class:
        ModelValidationDispatcher
    """

    def __init__(
            self,
            validator: ArenaValidator | None = None,
    ):
        super().__init__(validator=validator or ArenaValidator())
        
    @property
    def validator(self) -> ArenaValidator:
        return cast(ArenaValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[ArenaCarrier]:
        """
        Forward a job to a ArenaValidator then deliver the result.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a ArenaCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[ArenaCarrier]
        Raises:
             ArenaValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaValidationDispatcherException.MSG,
                    err_code=ArenaValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(ArenaCarrier, validation.payload)
        return ValidationResult.success(carrier)