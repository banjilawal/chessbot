# src/assurance/validator/model/register/operand/validator.py

"""
Module: assurance.validator.model.register.operand.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations
from typing import Any, cast

from assurance import ToggleValidator
from err import VectorToggleValidatorException
from assurance import VectorToggleIntegrityChecker
from artifcat import ValidationResult
from domain.structure.toggle import CartesianToggle
from util import LoggingLevelRouter



class VectorToggleValidator(ToggleValidator[CartesianToggle]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a VectorToggle instance is certified safe, reliable and consistent
            before use.

    Attributes:
        carrier_validator: VectorToggleRegisterIntegrityChecker

    Properties:
        -   def validate(
                    candidate: Any,
                    toolkit : VectorToggleToolkit,
            ) -> ValidationResult[VectorToggle]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            integrity_checker: VectorToggleIntegrityChecker | None = VectorToggleIntegrityChecker(),
    ):
        super().__init__(integrity_checker=integrity_checker)
        
    @property
    def integrity_checker(self) -> VectorToggleIntegrityChecker:
        return cast(VectorToggleIntegrityChecker, self.integrity_checker)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[CartesianToggle]:
        """
        Verify the candidate is a safe VectorToggle.
        
        Action:
            1.  Send an exception in the ValidationResult any of these
                conditions occur.
                    -   candidate is null.
                    -   It's not a VectorToggle.
                    -   The vectorToggle's payload is flagged unsafe.
            3.  Otherwise, Send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult
        Raises:
            VectorToggleValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        
        # Handle the case that, the validator is not primed.
        certification = self.integrity_checker.execute(
            candidate=candidate,
            target_model=self.integrity_checker.ruleset.model,
            context_null_exception=self.integrity_checker.ruleset.null_exception,
        )
        if certification.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorToggleValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorToggleValidatorException.MSG,
                    err_code=VectorToggleValidatorException.ERR_CODE,
                    ex=certification.exception
                )
            )
        # --- Cast candidate to a VectorToggle for additional tests. ---#
        return ValidationResult.success(cast(CartesianToggle, certification.payload))

            