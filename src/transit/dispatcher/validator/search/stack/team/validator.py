# src/transit/dispatcher/validator/search/stack/team/validator.py

"""
Module: transit.dispatcher.validator.search.stack.team.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from artifcat import ValidationResult
from assurance import StackContextValidator, TeamContextValidator
from domain import TeamSearchContext
from err import TeamContextValidatorException
from util import LoggingLevelRouter


class TeamContextValidator(StackContextValidator[TeamSearchContext]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TeamContext instance is safe before use.

    Attributes:
        validator: TeamContextChecker

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[TeamContext]

    Super Class:
        ContextValidator
    """
    
    def __init__(self, validator: TeamContextValidator):
        """
        Args:
            validator: TeamContextChecker
        """
        super().__init__(validator=validator)
    
    @property
    def validator(self) -> TeamContextValidator:
        return cast(TeamContextValidator, super().validator)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[TeamSearchContext]:
        """
        Certify a candidate is a TeamContext that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if validator
                returns a failure.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[TeamContext]
        Raises:
            TeamContextValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that validator flags the candidate.
        validation = self.validator.execute(candidate=candidate)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamContextValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamContextValidatorException.MSG,
                    err_code=TeamContextValidatorException.ERR_CODE,
                    ex=validation.exception
                )
            )
        # --- Otherwise, cast and forward the work product to the caller. ---#
        context = cast(TeamSearchContext, validation.payload)
        return ValidationResult.success(context)

