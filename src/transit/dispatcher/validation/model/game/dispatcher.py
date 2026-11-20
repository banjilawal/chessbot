# src/transit/dispatcher/validator/model/game/dispatcher.py

"""
Module: transit.dispatcher.validator.model.game.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast


from assurance import GameValidator
from artifcat import ValidationResult
from domain import Game
from err import GameValidationDispatcherException
from transit import ValidationDispatcher, GameCarrier
from util import LoggingLevelRouter


class GameValidationDispatcher(ValidationDispatcher[Game]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute Game validation jobs among workers, then forward their results.

    Attributes:
        validator: GameValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """

    def __init__(
            self,
            validator: Optional[GameValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[GameValidator]
        """
        super().__init__(validator=validator or GameValidator())
        
    @property
    def validator(self) -> GameValidator:
        return cast(GameValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[GameCarrier]:
        """
        Send jobs to a GameValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
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
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
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