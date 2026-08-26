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
from assurance import PlayerIntegrityChecker
from artifcat import ValidationResult
from util import LoggingLevelRouter
from transit.dispatcher.validator import ModelValidationDispatcher


class PlayerValidationDispatcher(ModelValidationDispatcher[Player]):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a Player instance is certified safe, reliable and consistent before use.

    Attributes:
        integrity_checker: PlayerIntegrityChecker

    Provides:
        -   execute(candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            integrity_checker: PlayerIntegrityChecker | None = PlayerIntegrityChecker(),
    ):
        super().__init__(integrity_checker=integrity_checker)
        
    @property
    def integrity_checker(self) -> PlayerIntegrityChecker:
        return cast(PlayerIntegrityChecker, super().integrity_checker)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify the object is a Player that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                integrity_checker test..
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
        
        # Handle the case that, the candidate is not safe.
        certification = self.integrity_checker.execute(candidate)
        if certification.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidatorException.MSG,
                    err_code=PlayerValidatorException.ERR_CODE,
                    ex=certification.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            cast(
                self.integrity_checker.bundle.model,
                certification.payload
            )
        )