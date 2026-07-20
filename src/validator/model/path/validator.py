# src/validator/model/path/validator.py

"""
Module: validator.model.path.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from err import PathValidatorException
from model import Path
from primary import PathRootCertifier
from result import ValidationResult
from util import LoggingLevelRouter
from validator import ModelValidator


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
        root_certifier: PathRootCertifier

    Provides:
        -   execute(candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            root_certifier: PathRootCertifier | None = PathRootCertifier(),
    ):
        super().__init__(root_certifier=root_certifier)
        
    @property
    def root_certifier(self) -> PathRootCertifier:
        return cast(PathRootCertifier, self.root_certifier)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify the object is a Path that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                root_certifier test..
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
        certification = self.root_certifier.execute(candidate)
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
                self.root_certifier.toolkit.model,
                certification.payload
            )
        )