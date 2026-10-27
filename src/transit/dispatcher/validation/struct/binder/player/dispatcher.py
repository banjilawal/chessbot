# src/transit/dispatcher/validator/struct/binder/player/dispatcher.py

"""
Module: transit.dispatcher.validator.binder.player.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from err import PlayerBinderValidationDispatcherException
from domain.struct.binder import PlayerBinder
from artifcat import ValidationResult
from transit import PlayerBinderCarrier
from util import LoggingLevelRouter
from transit.dispatcher.validator import BinderValidationDispatcher


class PlayerBinderValidationDispatcher(BinderValidationDispatcher[PlayerBinder]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a PlayerBinder instance is certified safe, reliable, and consistent before use.

    Attributes:
        validator: PlayerBinderValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult{PlayerBinder]

    Super Class:
        BinderValidator
    """
    
    def __init__(
            self,
            validator: PlayerBinderValidator | None = PlayerBinderValidator(),
    ):
        super().__init__(validator=validator or PlayerBinderValidator())
        
    @property
    def validator(self) -> PlayerBinderValidator:
        return cast(PlayerBinderValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[PlayerBinderCarrier]:
        """
        Verify the object is a PlayerBinder that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                validator test..
            2.  Otherwise, cast the payload into a PlayerBinder and send in the success result.
                success result.
        Args:
            job: Any
        Returns:
            ValidationResult[PlayerBinder]
        Raises:
             PlayerBinderValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
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
        return ValidationResult.success(
            cast(PlayerBinderCarrier, validation.payload)
        )