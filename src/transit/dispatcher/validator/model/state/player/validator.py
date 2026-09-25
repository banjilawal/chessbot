# src/transit/dispatcher/validator/model/state/player/validator.py

"""
Module: transit.dispatcher.validator.model.state.player.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from err import PlayerValidatorException
from domain.model import Player
from assurance import PlayerValidator
from artifcat import ValidationResult
from util import LoggingLevelRouter
from transit.dispatcher.validator import ModelValidationDispatcher


class PlayerValidationDispatcher(ModelValidationDispatcher[Player]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a Player instance is certified safe, reliable, and consistent before use.

    Attributes:
        validator: PlayerValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            validator: PlayerValidator | None = PlayerValidator(),
    ):
        super().__init__(validator=validator)
        
    @property
    def validator(self) -> PlayerValidator:
        return cast(PlayerValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify the object is a Player that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                validator test..
            2.  Otherwise, cast the payload into a Player and send in the success result.
                success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Player]
        Raises:
             PlayerValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(candidate)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidatorException.MSG,
                    err_code=PlayerValidatorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            cast(
                self.validator.bundle.model,
                validation.payload
            )
        )