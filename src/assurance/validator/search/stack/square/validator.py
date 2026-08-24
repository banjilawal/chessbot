# src/assurance/validator/search/stack/square/validator.py

"""
Module: assurance.validator.search.stack.square.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from artifcat import ValidationResult
from assurance import StackSearchContextValidator, SquareContextChecker
from domain import SquareSearchContext
from err import SquareContextValidatorException
from util import LoggingLevelRouter


class SquareContextValidator(StackSearchContextValidator[SquareSearchContext]):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a SquareSearchContext instance is safe before use.

    Attributes:
        integrity_checker: SquareContextChecker

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult[SquareSearchContext]

    Super Class:
        ContextValidator
    """
    
    def __init__(self, integrity_checker: SquareContextChecker):
        """
        Args:
            integrity_checker: SquareContextChecker
        """
        super().__init__(integrity_checker=integrity_checker)
    
    
    @property
    def integrity_checker(self) -> SquareContextChecker:
        return cast(SquareContextChecker, super().integrity_checker)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[SquareSearchContext]:
        """
        Certify a candidate is a SquareContext that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if integrity_checker
                returns a failure.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[SquareSearchContext]
        Raises:
            SquareContextValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that integrity_checker flags the candidate.
        validation = self.integrity_checker.execute(candidate=candidate)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareContextValidatorException.MSG,
                    err_code=SquareContextValidatorException.ERR_CODE,
                    ex=validation.exception
                )
            )
        # --- Otherwise, cast and forward the work product to the caller. ---#
        context = cast(SquareSearchContext, validation.payload)
        return ValidationResult.success(context)

        
    
