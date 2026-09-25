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
from assurance import StackContextValidator, CoordContextValidator
from domain import CoordSearchContext
from err import CoordContextValidatorException
from util import LoggingLevelRouter


class CoordContextValidator(StackContextValidator[CoordSearchContext]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a CoordContext instance is safe before use.

    Attributes:
        validator: CoordContextChecker

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[CoordContext]

    Super Class:
        ContextValidator
    """
    
    def __init__(self, validator: Optional[CoordContextValidator] | None = None):
        """
        Args:
            validator: Optional[CoordContextChecker]
        """
        super().__init__(validator=validator or CoordContextValidator)
    
    
    @property
    def validator(self) -> CoordContextValidator:
        return cast(CoordContextValidator, super().validator)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[CoordSearchContext]:
        """
        Certify a candidate is a CoordContext that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if validator
                returns a failure.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[CoordContext]
        Raises:
            CoordContextValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that validator flags the candidate.
        validation = self.validator.execute(candidate=candidate)
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

        



