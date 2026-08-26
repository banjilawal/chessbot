# src/transit/dispatcher/validator/model/vector/validator.py

"""
Module: transit.dispatcher.validator.model.vector.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from assurance import ModelValidator
from err import VectorValidatorException
from assurance import VectorIntegrityValidator
from domain.model import Vector
from artifcat import ValidationResult
from util import LoggingLevelRouter



class VectorValidator(ModelValidator):
    """
    Role
        -  Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a Vector instance is certified safe, reliable and consistent before use.

    Attributes:
        integrity_checker: VectorIntegrityChecker

    Provides:
        -  execute(candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            integrity_checker: VectorIntegrityValidator | None = None,
    ):
        super().__init__(integrity_checker=integrity_checker or VectorIntegrityValidator())
        
    @property
    def integrity_checker(self) -> VectorIntegrityValidator:
        return cast(VectorIntegrityValidator, super().integrity_checker)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify the object is a Vector that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                integrity_checker test.
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
        certification = self.integrity_checker.execute(candidate)
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
        return ValidationResult.success(cast(Vector, certification.payload))