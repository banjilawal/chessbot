# src/transit/dispatcher/validator/model/structure/register/operand/validator.py

"""
Module: transit.dispatcher.validator.model.register.operand.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from selector import OrientationToggle
from util import LoggingLevelRouter
from transit.dispatcher.validator import ModelValidationDispatcher


class OrientationSelectorValidationDispatcher(ModelValidationDispatcher[OrientationToggle]):
    """
    Role
        -  Transaction Worker
        -  Integrity Maintenance
        -  Consistency Assurance
        -  Validation Process Owner

    Responsibilities:
        1.  Ensure a OrientationOperand instance is certified safe, reliable and consistent
            before use.

    Attributes:
        carrier_validator: CartesianToggleRegisterIntegrityChecker

    Properties:
        - def validate(
                    candidate: Any,
                    toolkit : OrientationOperandToolkit,
            ) -> ValidationResult[OrientationOperand]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            integrity_checker: CartesianToggleRegisterIntegrityChecker | None = CartesianToggleRegisterIntegrityChecker(),
    ):
        super().__init__(integrity_checker=integrity_checker)
        
    @property
    def integrity_checker(self) -> CartesianToggleRegisterIntegrityChecker:
        return cast(CartesianToggleRegisterIntegrityChecker, super().integrity_checker)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify the candidate is a safe OrientationOperand.
        
        Action:
            1.  Send an exception in the ValidationResult any of these
                conditions occur.
                    -  candidate is null.
                    -  It's not a OrientationOperand.
                    -  The orientationOperand's payload is flagged unsafe.
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
        validator_priming_result = self.integrity_checker.bundle.priming_validator.execute(
            candidate=candidate,
            target_model=self.integrity_checker.bundle.model,
            context_null_exception=self.integrity_checker.bundle.request_null_exception,
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
        
        root_certification = self.integrity_checker.execute(register)
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

            