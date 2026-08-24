# src/assurance/validator/model/path/validator.py

"""
Module: assurance.validator.model.path.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from err import PathValidatorException
from domain.model import Path
from assurance import PathIntegrityChecker
from artifcat import ValidationResult
from util import LoggingLevelRouter
from assurance.validator import ModelValidator


class PathValidator(ModelValidator[Path]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Path instance is certified safe, reliable and consistent before use.

    Attributes:
        integrity_checker: PathIntegrityChecker

    Provides:
        -   execute(candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            integrity_checker: PathIntegrityChecker | None = PathIntegrityChecker(),
    ):
        super().__init__(integrity_checker=integrity_checker)
        
    @property
    def integrity_checker(self) -> PathIntegrityChecker:
        return cast(PathIntegrityChecker, self.integrity_checker)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify the object is a Path that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                integrity_checker test..
            2.  Otherwise, cast the payload into a Path and send in the success result.
                success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Path]
        Raises:
             PathValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the candidate is not safe.
        certification = self.integrity_checker.execute(candidate)
        if certification.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidatorException.MSG,
                    err_code=PathValidatorException.ERR_CODE,
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