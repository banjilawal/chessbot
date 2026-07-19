# src/validator/model/register/operand/validator.py

"""
Module: validator.model.register.operand.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from selector import VectorSelector
from util import LoggingLevelRouter
from validator import ModelValidator


class VectorSelectorValidator(ModelValidator[VectorSelector]):
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
            root_certifier: CartesianRegisterRootCertifier | None = CartesianRegisterRootCertifier(),
    ):
        super().__init__(root_certifier=root_certifier)
        
    @property
    def root_certifier(self) -> CartesianRegisterRootCertifier:
        return cast(CartesianRegisterRootCertifier, self.root_certifier)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
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
        validator_priming_result = self.root_certifier.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=self.root_certifier.toolkit.model,
            context_null_exception=self.root_certifier.toolkit.null_exception,
        )
        if validator_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorOperandValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorOperandValidatorException.MSG,
                    err_code=VectorOperandValidatorException.ERR_CODE,
                    ex=validator_priming_result.exception
                )
            )
        # --- Cast candidate to a VectorOperand for additional tests. ---#
        register = cast(VectorOperandEntityRegister, candidate)
        
        root_certification = self.root_certifier.execute(register)
        if root_certification.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorOperandValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorOperandValidatorException.MSG,
                    err_code=VectorOperandValidatorException.ERR_CODE,
                    ex=root_certification.exception
                )
            )
        
        return root_certification

            