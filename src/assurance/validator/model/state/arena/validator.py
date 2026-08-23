# src/assurance/validator/model/state/arena/validator.py

"""
Module: assurance.validator.model.state.arena.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from err import ArenaValidatorException
from domain.model import Arena
from assurance import ArenaIntegrityChecker
from artifcat.result import ValidationResult
from util import LoggingLevelRouter
from assurance.validator import ModelValidator


class ArenaValidator(ModelValidator[Arena]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Arena instance is certified safe, reliable and consistent before use.

    Attributes:
        integrity_checker: ArenaIntegrityChecker

    Provides:
        -   execute(candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            integrity_checker: ArenaIntegrityChecker | None = ArenaIntegrityChecker(),
    ):
        super().__init__(integrity_checker=integrity_checker)
        
    @property
    def integrity_checker(self) -> ArenaIntegrityChecker:
        return cast(ArenaIntegrityChecker, self.integrity_checker)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify the object is a Arena that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                integrity_checker test..
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
        
        # Handle the case that, the candidate is not safe.
        certification = self.integrity_checker.execute(candidate)
        if certification.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaValidatorException.MSG,
                    err_code=ArenaValidatorException.ERR_CODE,
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