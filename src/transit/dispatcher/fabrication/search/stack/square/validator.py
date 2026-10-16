# src/transit/dispatcher/fabrication/search/stack/square/validator.py

"""
Module: transit.dispatcher.fabrication.search.stack.square.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from artifcat import BuildResult
from assurance import StackContextValidator, SquareContextValidator
from domain import SquareSearchContext
from err import SquareContextValidatorException
from util import LoggingLevelRouter


class SquareContextValidator(StackContextValidator[SquareSearchContext]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a SquareContext instance is safe before use.

    Attributes:
        validator: SquareContextChecker

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[SquareContext]

    Super Class:
        ContextValidator
    """
    
    def __init__(self, validator: SquareContextValidator):
        """
        Args:
            validator: SquareContextChecker
        """
        super().__init__(validator=validator)
    
    
    @property
    def validator(self) -> SquareContextValidator:
        return cast(SquareContextValidator, super().validator)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> BuildResult[SquareSearchContext]:
        """
        Certify a candidate is a SquareContext that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResult if validator
                returns a failure.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            BuildResult[SquareContext]
        Raises:
            SquareContextValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that validator flags the candidate.
        build = self.validator.execute(candidate=candidate)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                SquareContextValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareContextValidatorException.MSG,
                    err_code=SquareContextValidatorException.ERR_CODE,
                    ex=build.exception
                )
            )
        # --- Otherwise, cast and forward the work product to the caller. ---#
        context = cast(SquareSearchContext, build.payload)
        return BuildResult.success(context)

        
    
