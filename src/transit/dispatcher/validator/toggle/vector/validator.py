# src/transit/dispatcher/validator/model/structure/register/operand/validator.py

"""
Module: transit.dispatcher.validator.model.register.operand.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from artifcat import ValidationResult
from assurance import ToggleValidator
from domain import CartesianToggle
from err import CartesianToggleValidatorException
from util import LoggingLevelRouter


class CartesianToggleValidator(ToggleValidator[CartesianToggle]):
    """
    Role
        -  Transaction Worker
        -  Integrity Maintenance
        -  Consistency Assurance
        -  Validation Process Owner

    Responsibilities:
        1.  Ensure a CartesianToggle instance is certified safe, reliable and consistent
            before use.

    Attributes:
        carrier_validator: CartesianToggleRegisterIntegrityChecker

    Properties:
        - def validate(
                    candidate: Any,
                    toolkit : CartesianToggleToolkit,
            ) -> ValidationResult[CartesianToggle]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            integrity_checker: CartesianToggleIntegrityChecker | None = None,
    ):
        super().__init__(integrity_checker=integrity_checker)
        
    @property
    def integrity_checker(self) -> CartesianToggleIntegrityChecker:
        return cast(CartesianToggleIntegrityChecker, super().integrity_checker)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[CartesianToggle]:
        """
        Verify the candidate is a safe CartesianToggle.
        
        Action:
            1.  Send an exception in the ValidationResult any of these
                conditions occur.
                    -  candidate is null.
                    -  It's not a CartesianToggle.
                    -  The cartesianToggle's payload is flagged unsafe.
            3.  Otherwise, Send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult
        Raises:
            CartesianToggleValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        
        # Handle the case that, the validator is not primed.
        certification = self.integrity_checker.execute(
            candidate=candidate,
            target_model=self.integrity_checker.ruleset.model,
            context_null_exception=self.integrity_checker.ruleset.domain_null_exception,
        )
        if certification.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CartesianToggleValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianToggleValidatorException.MSG,
                    err_code=CartesianToggleValidatorException.ERR_CODE,
                    ex=certification.exception
                )
            )
        # --- Cast candidate to a CartesianToggle for additional tests. ---#
        return ValidationResult.success(cast(CartesianToggle, certification.payload))

            