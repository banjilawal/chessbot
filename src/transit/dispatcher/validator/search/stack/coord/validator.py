# src/transit/dispatcher/validator/search/stack/coord/validator.py

"""
Module: transit.dispatcher.validator.search.stack.coord.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations
from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import StackSearchContextValidator, CoordContextValidator
from domain import CoordSearchContext
from err import CoordContextValidatorException
from util import LoggingLevelRouter


class CoordContextValidator(StackSearchContextValidator[CoordSearchContext]):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a CoordSearchContext instance is safe before use.

    Attributes:
        integrity_checker: CoordContextChecker

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult[CoordSearchContext]

    Super Class:
        ContextValidator
    """
    
    def __init__(self, integrity_checker: Optional[CoordContextValidator] | None = None):
        """
        Args:
            integrity_checker: Optional[CoordContextChecker]
        """
        super().__init__(integrity_checker=integrity_checker or CoordContextValidator)
    
    
    @property
    def integrity_checker(self) -> CoordContextValidator:
        return cast(CoordContextValidator, super().integrity_checker)
    
    
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

        



