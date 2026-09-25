# src/transit/dispatcher/validator/model/state/arena/validator.py

"""
Module: transit.dispatcher.validator.model.state.arena.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from err import ArenaValidatorException
from domain.model import Arena
from assurance import ArenaValidator
from artifcat import ValidationResult
from util import LoggingLevelRouter
from transit.dispatcher.validator import ModelValidationDispatcher


class ArenaValidationDispatcher(ModelValidationDispatcher[Arena]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a Arena instance is certified safe, reliable, and consistent before use.

    Attributes:
        validator: ArenaValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            validator: ArenaValidator | None = ArenaValidator(),
    ):
        super().__init__(validator=validator)
        
    @property
    def validator(self) -> ArenaValidator:
        return cast(ArenaValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify the object is a Arena that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                validator test..
            2.  Otherwise, cast the payload into a Arena and send in the success result.
                success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Arena]
        Raises:
             ArenaValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(candidate)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaValidatorException.MSG,
                    err_code=ArenaValidatorException.ERR_CODE,
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