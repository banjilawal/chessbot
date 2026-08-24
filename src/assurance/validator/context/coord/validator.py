# src/assurance/validator/context/coord/validator.py

"""
Module: assurance.validator.context.coord.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations
from typing import Any, cast

from artifcat import ValidationResult
from assurance import ContextValidator, CoordContextChecker
from domain import CoordSearchContext
from err import CoordContextValidatorException
from util import LoggingLevelRouter


class CoordContextValidator(ContextValidator[CoordSearchContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a CoordSearchContext instance is certified safe, reliable, and consistent before use.

    Attributes:
        integrity_checker: CoordContextChecker

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult[CoordSearchContext]

    Super Class:
        ContextValidator
    """
    
    def __init__(self, integrity_checker: CoordContextChecker):
        """
        Args:
            integrity_checker: CoordContextChecker
        """
        super().__init__(integrity_checker=integrity_checker)
    
    
    @property
    def integrity_checker(self) -> CoordContextChecker:
        return cast(CoordContextChecker, super().integrity_checker)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[CoordSearchContext]:
        """
        Certify a candidate is a CoordSearchContext that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if integrity_checker
                returns a failure.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[CoordSearchContext]
        Raises:
            CoordContextValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that integrity_checker flags the candidate.
        validation = self.integrity_checker.execute(candidate=candidate)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordContextValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordContextValidatorException.MSG,
                    err_code=CoordContextValidatorException.ERR_CODE,
                    ex=validation.exception
                )
            )
        # --- Otherwise, cast and forward the work product to the caller. ---#
        context = cast(CoordSearchContext, validation.payload)
        return ValidationResult.success(context)

        



