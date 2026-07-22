# src/validator/register/vector/validator.py

"""
Module: validator.register.vector.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from register import VectorRegister
from validator import RegisterValidator


class VectorRegisterValidator(RegisterValidator[VectorRegister]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a VectorRegister instance is certified safe, reliable and consistent before use.

    Attributes:
        root_certifier: VectorRegisterRootCertifier

    Provides:
        -   execute(candidate: Any) -> ValidationResult{VectorRegister]

    Super Class:
        RegisterValidator
    """
    
    def __init__(
            self,
            root_certifier: VectorRegisterRootCertifier | None = VectorRegisterRootCertifier(),
    ):
        super().__init__(root_certifier=root_certifier)
        
    @property
    def root_certifier(self) -> VectorRegisterRootCertifier:
        return cast(VectorRegisterRootCertifier, self.root_certifier)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify the object is a VectorRegister that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                root_certifier test..
            2.  Otherwise, cast the payload into a VectorRegister and send in the success result.
                success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[VectorRegister]
        Raises:
             VectorRegisterValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the candidate is not safe.
        certification = self.root_certifier.execute(candidate)
        if certification.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterValidatorException.MSG,
                    err_code=VectorRegisterValidatorException.ERR_CODE,
                    ex=certification.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            cast(
                self.root_certifier.toolkit.register,
                certification.payload
            )
        )