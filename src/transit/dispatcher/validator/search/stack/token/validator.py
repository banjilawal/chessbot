# src/transit/dispatcher/validator/search/stack/token/validator.py

"""
Module: transit.dispatcher.validator.search.stack.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from artifcat import ValidationResult
from assurance import StackContextValidator, TokenContextValidator
from domain import TokenSearchContext
from err import TokenContextValidatorException
from util import LoggingLevelRouter


class TokenContextValidator(StackContextValidator[TokenSearchContext]):
    """
    Role
        -  Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TokenContext instance is safe before use.

    Attributes:
        integrity_checker: TokenContextChecker

    Provides:
        -  execute(self, candidate: Any) -> ValidationResult[TokenContext]

    Super Class:
        ContextValidator
    """
    
    def __init__(self, integrity_checker: TokenContextValidator):
        """
        Args:
            integrity_checker: TokenContextChecker
        """
        super().__init__(integrity_checker=integrity_checker)
    
    
    @property
    def integrity_checker(self) -> TokenContextValidator:
        return cast(TokenContextValidator, super().integrity_checker)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[TokenSearchContext]:
        """
        Certify a candidate is a TokenContext that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if integrity_checker
                returns a failure.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[TokenContext]
        Raises:
            TokenContextValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that integrity_checker flags the candidate.
        validation = self.integrity_checker.execute(candidate=candidate)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenContextValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenContextValidatorException.MSG,
                    err_code=TokenContextValidatorException.ERR_CODE,
                    ex=validation.exception
                )
            )
        # --- Otherwise, cast and forward the work product to the caller. ---#
        context = cast(TokenSearchContext, validation.payload)
        return ValidationResult.success(context)

        
    
