# src/validator/model/register/operand/validator.py

"""
Module: validator.model.register.operand.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from err import VectorToggleValidatorException
from primary import VectorToggleRootCertifier
from result import ValidationResult
from toggle import VectorToggle
from util import LoggingLevelRouter
from validator import Validator


class VectorToggleValidator(Validator[VectorToggle]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a VectorOperand instance is certified safe, reliable and consistent
            before use.

    Attributes:
        bootstrapper: CartesianRegisterRootCertifier

    Properties:
        -   def validate(
                    candidate: Any,
                    toolkit : VectorOperandToolkit,
            ) -> ValidationResult[VectorOperand]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            root_certifier: VectorToggleRootCertifier | None = VectorToggleRootCertifier(),
    ):
        super().__init__(root_certifier=root_certifier)
        
    @property
    def root_certifier(self) -> VectorToggleRootCertifier:
        return cast(VectorToggleRootCertifier, self.root_certifier)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[VectorToggle]:
        """
        Verify the candidate is a safe VectorOperand.
        
        Action:
            1.  Send an exception in the ValidationResult any of these
                conditions occur.
                    -   candidate is null.
                    -   It's not a VectorOperand.
                    -   The vectorOperand's payload is flagged unsafe.
            3.  Otherwise, Send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult
        Raises:
            VectorOperandValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        
        # Handle the case that, the validator is not primed.
        certification = self.root_certifier.execute(
            candidate=candidate,
            target_model=self.root_certifier.toolkit.model,
            context_null_exception=self.root_certifier.toolkit.null_exception,
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
        # --- Cast candidate to a VectorOperand for additional tests. ---#
        return ValidationResult.success(cast(VectorToggle, certification.payload))

            