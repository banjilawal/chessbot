# src/assurance/validator/model/scalar/validator.py

"""
Module: assurance.validator.model.scalar.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from err import ScalarValidatorException
from model import Scalar
from assurance.checker import ScalarRootCertifier
from result import ValidationResult
from util import LoggingLevelRouter
from assurance.validator import ModelValidator


class ScalarValidator(ModelValidator[Scalar]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Scalar instance is certified safe, reliable and consistent before use.

    Attributes:
        root_certifier: ScalarRootCertifier

    Provides:
        -   execute(candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            root_certifier: ScalarRootCertifier | None = ScalarRootCertifier(),
    ):
        super().__init__(root_certifier=root_certifier)
        
    @property
    def integrity_checker(self) -> ScalarRootCertifier:
        return cast(ScalarRootCertifier, self.integrity_checker)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify the object is a Scalar that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                root_certifier test..
            2.  Otherwise, cast the payload into a Scalar and send in the success result.
                success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Scalar]
        Raises:
             ScalarValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the candidate is not safe.
        certification = self.integrity_checker.execute(candidate)
        if certification.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidatorException.MSG,
                    err_code=ScalarValidatorException.ERR_CODE,
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