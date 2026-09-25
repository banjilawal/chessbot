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
        - Transaction Worker
        - Integrity Maintenance
        - Consistency Assurance
        - Validation Process Owner

    Responsibilities:
        1.  Ensure a OrientationOperand instance is certified safe, reliable, and consistent
            before use.

    Attributes:
        carrier_validator: CartesianToggleRegisterValidator

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
            validator: CartesianToggleRegisterValidator | None = CartesianToggleRegisterValidator(),
    ):
        super().__init__(validator=validator)
        
    @property
    def validator(self) -> CartesianToggleRegisterValidator:
        return cast(CartesianToggleRegisterValidator, super().validator)
    
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult:
        """
        Verify the candidate is a safe OrientationOperand.
        
        Action:
            1.  Send an exception in the ValidationResult any of these
                conditions occur.
                    - candidate is null.
                    - It's not a OrientationOperand.
                    - The orientationOperand's payload is flagged unsafe.
            3.  Otherwise, Send the success result.
        Args:
            job: Any
        Returns:
            ValidationResult
        Raises:
            OrientationOperandValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        
        # Handle the case that the validator is not primed.
        validator_priming_result = self.validator.bundle.priming_validator.execute(
            job=job,
            target_model=self.validator.bundle.model,
            context_null_exception=self.validator.bundle.request_null_exception,
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
        register = cast(OrientationOperandEntityRegister, job)
        
        root_validation = self.validator.execute(register)
        if root_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                OrientationOperandValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=OrientationOperandValidatorException.MSG,
                    err_code=OrientationOperandValidatorException.ERR_CODE,
                    ex=root_validation.exception
                )
            )
        
        return root_validation

            