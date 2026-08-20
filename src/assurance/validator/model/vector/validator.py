# src/assurance/validator/model/vector/validator.py

"""
Module: assurance.validator.model.vector.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from assurance import ModelValidator
from err import VectorValidatorException
from model import Vector
from assurance.checker import VectorIntegrityChecker
from result import ValidationResult
from util import LoggingLevelRouter



class VectorValidator(ModelValidator[Vector]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Vector instance is certified safe, reliable and consistent before use.

    Attributes:
        root_certifier: VectorRootCertifier

    Provides:
        -   execute(candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            root_certifier: VectorIntegrityChecker | None = None,
    ):
        super().__init__(root_certifier=root_certifier or VectorIntegrityChecker())
        
    @property
    def certifier(self) -> VectorIntegrityChecker:
        return cast(VectorIntegrityChecker, super().certifier)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify the object is a Vector that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                root_certifier test..
            2.  Otherwise, cast the payload into a Vector and send in the success result.
                success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Vector]
        Raises:
             VectorValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the candidate is not safe.
        certification = self.certifier.execute(candidate)
        if certification.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidatorException.MSG,
                    err_code=VectorValidatorException.ERR_CODE,
                    ex=certification.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            cast(
                self.certifier.toolkit.model,
                certification.payload
            )
        )