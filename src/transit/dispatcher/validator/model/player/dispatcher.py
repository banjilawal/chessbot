# src/transit/dispatcher/validator/model/player/validator.py

"""
Module: transit.dispatcher.validator.model.player.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import PlayerValidator
from artifcat import ValidationResult
from domain import Player
from err import PlayerValidationDispatcherException
from transit import ModelValidationDispatcher, PlayerCarrier
from util import LoggingLevelRouter


class PlayerValidationDispatcher(ModelValidationDispatcher[Player]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the PlayerValidation workflow.

    Attributes:
        validator: PlayerValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[validatorCarrier]

    Super Class:
        ModelValidationDispatcher
    """

    def __init__(
            self,
            validator: PlayerValidator | None = None,
    ):
        super().__init__(validator=validator or PlayerValidator())
        
    @property
    def validator(self) -> PlayerValidator:
        return cast(PlayerValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[PlayerCarrier]:
        """
        Forward a job to a PlayerValidator then deliver the result.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator cannot
                certify the job's content.
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
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
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