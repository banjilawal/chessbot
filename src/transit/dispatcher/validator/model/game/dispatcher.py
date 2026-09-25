# src/transit/dispatcher/validator/model/game/validator.py

"""
Module: transit.dispatcher.validator.model.game.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import GameValidator
from artifcat import ValidationResult
from domain import Game
from err import GameValidationDispatcherException
from transit import ModelValidationDispatcher, GameCarrier
from util import LoggingLevelRouter


class GameValidationDispatcher(ModelValidationDispatcher[Game]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the GameValidation workflow.

    Attributes:
        validator: GameValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[validatorCarrier]

    Super Class:
        ModelValidationDispatcher
    """

    def __init__(
            self,
            validator: GameValidator | None = None,
    ):
        super().__init__(validator=validator or GameValidator())
        
    @property
    def validator(self) -> GameValidator:
        return cast(GameValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[GameCarrier]:
        """
        Forward a job to a GameValidator then deliver the result.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a GameCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[GameCarrier]
        Raises:
             GameValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidationDispatcherException.MSG,
                    err_code=GameValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(GameCarrier, validation.payload)
        return ValidationResult.success(carrier)