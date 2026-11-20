# src/transit/dispatcher/validator/model/player/dispatcher.py

"""
Module: transit.dispatcher.validator.model.player.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast


from assurance import PlayerValidator
from artifcat import ValidationResult
from domain import Player
from err import PlayerValidationDispatcherException
from transit import ValidationDispatcher, PlayerCarrier
from util import LoggingLevelRouter


class PlayerValidationDispatcher(ValidationDispatcher[Player]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute Player validation jobs among workers, then forward their results.

    Attributes:
        validator: PlayerValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """

    def __init__(
            self,
            validator: Optional[PlayerValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[PlayerValidator]
        """
        super().__init__(validator=validator or PlayerValidator())
        
    @property
    def validator(self) -> PlayerValidator:
        return cast(PlayerValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[PlayerCarrier]:
        """
        Send jobs to a PlayerValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
            2.  Otherwise, cast the job payload into a PlayerCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[PlayerCarrier]
        Raises:
             PlayerValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidationDispatcherException.MSG,
                    err_code=PlayerValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(PlayerCarrier, validation.payload)
        return ValidationResult.success(carrier)