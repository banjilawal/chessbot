# src/transit/dispatcher/validator/struct/binder/player/dispatcher.py

"""
Module: transit.dispatcher.validator.binder.player.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from assurance import PlayerBinderValidator
from artifcat import ValidationResult
from domain import PlayerBinder
from err import PlayerBinderValidationDispatcherException
from transit import PlayerBinderCarrier, ValidationDispatcher
from util import LoggingLevelRouter


class PlayerBinderValidationDispatcher(ValidationDispatcher[PlayerBinder]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute PlayerBinder validation jobs among workers, then forward their results.

    Attributes:
        validator: PlayerBinderValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """
    
    def __init__(
            self,
            validator: Optional[PlayerBinderValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[PlayerBinderValidator]
        """
        super().__init__(validator=validator or PlayerBinderValidator())
    
    @property
    def validator(self) -> PlayerBinderValidator:
        return cast(PlayerBinderValidator, super().validator)
    
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[PlayerBinderCarrier]:
        """
        Send jobs to a PlayerBinderValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
            2.  Otherwise, cast the job payload into a PlayerBinderCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[PlayerBinderCarrier]
        Raises:
             PlayerBinderValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerBinderValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderValidationDispatcherException.MSG,
                    err_code=PlayerBinderValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(PlayerBinderCarrier, validation.payload)
        return ValidationResult.success(carrier)