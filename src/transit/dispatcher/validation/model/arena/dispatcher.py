# src/transit/dispatcher/validator/model/arena/dispatcher.py

"""
Module: transit.dispatcher.validator.model.arena.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast


from assurance import ArenaValidator
from artifcat import ValidationResult
from domain import Arena
from err import ArenaValidationDispatcherException
from transit import ValidationDispatcher, ArenaCarrier
from util import LoggingLevelRouter


class ArenaValidationDispatcher(ValidationDispatcher[Arena]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute Arena validation jobs among workers, then forward their results.

    Attributes:
        validator: ArenaValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """

    def __init__(
            self,
            validator: Optional[ArenaValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[ArenaValidator]
        """
        super().__init__(validator=validator or ArenaValidator())
        
    @property
    def validator(self) -> ArenaValidator:
        return cast(ArenaValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[ArenaCarrier]:
        """
        Send jobs to a ArenaValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
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
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
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