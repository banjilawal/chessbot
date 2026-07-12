# src/validator/token/validator.py

"""
Module: validator.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from err import TokenValidatorException
from model import Token
from primary import TokenRootCertifier
from result import ValidationResult
from util import LoggingLevelRouter
from validator import ModelValidator


class TokenValidator(ModelValidator[Token]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Token instance is certified safe, reliable and consistent before use.

    Attributes:
        root_certifier: TokenRootCertifier

    Provides:
        -   execute(candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            root_certifier: TokenRootCertifier | None = TokenRootCertifier(),
    ):
        super().__init__(root_certifier=root_certifier)
        
    @property
    def root_certifier(self) -> TokenRootCertifier:
        return cast(TokenRootCertifier, self.root_certifier)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify the object is a Token that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                root_certifier test..
            2.  Otherwise, cast the payload into a Token and send in the success result.
                success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Token]
        Raises:
             TokenValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the candidate is not safe.
        certification = self.root_certifier.execute(candidate)
        if certification.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=certification.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            cast(
                self.root_certifier.toolkit.model,
                certification.payload
            )
        )