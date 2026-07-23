# src/validator/model/register/operand/validator.py

"""
Module: validator.model.register.operand.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from selector import OrientationToggle
from util import LoggingLevelRouter
from validator import ModelValidator


class OrientationSelectorValidator(ModelValidator[OrientationToggle]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a OrientationOperand instance is certified safe, reliable and consistent
            before use.

    Attributes:
        carrier_validator: VectorToggleRegisterRootCertifier

    Properties:
        -   def validate(
                    candidate: Any,
                    toolkit : OrientationOperandToolkit,
            ) -> ValidationResult[OrientationOperand]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            root_certifier: VectorToggleRegisterRootCertifier | None = VectorToggleRegisterRootCertifier(),
    ):
        super().__init__(root_certifier=root_certifier)
        
    @property
    def root_certifier(self) -> VectorToggleRegisterRootCertifier:
        return cast(VectorToggleRegisterRootCertifier, self.root_certifier)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify the candidate is a safe OrientationOperand.
        
        Action:
            1.  Send an exception in the ValidationResult any of these
                conditions occur.
                    -   candidate is null.
                    -   It's not a OrientationOperand.
                    -   The orientationOperand's payload is flagged unsafe.
            3.  Otherwise, Send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult
        Raises:
            OrientationOperandValidatorException
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
                OrientationOperandValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=OrientationOperandValidatorException.MSG,
                    err_code=OrientationOperandValidatorException.ERR_CODE,
                    ex=validator_priming_result.exception
                )
            )
        # --- Cast candidate to a OrientationOperand for additional tests. ---#
        register = cast(OrientationOperandEntityRegister, candidate)
        
        root_certification = self.root_certifier.execute(register)
        if root_certification.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                OrientationOperandValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=OrientationOperandValidatorException.MSG,
                    err_code=OrientationOperandValidatorException.ERR_CODE,
                    ex=root_certification.exception
                )
            )
        
        return root_certification

            