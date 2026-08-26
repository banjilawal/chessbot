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
from assurance import StackSearchContextValidator, TeamContextValidator
from domain import TeamSearchSearchContext
from err import TeamContextValidatorException
from util import LoggingLevelRouter


class TeamContextValidator(StackSearchContextValidator[TeamSearchSearchContext]):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TeamSearchContext instance is safe before use.

    Attributes:
        integrity_checker: TeamContextChecker

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult[TeamSearchContext]

    Super Class:
        ContextValidator
    """
    
    def __init__(self, integrity_checker: TeamContextValidator):
        """
        Args:
            integrity_checker: TeamContextChecker
        """
        super().__init__(integrity_checker=integrity_checker)
    
    @property
    def integrity_checker(self) -> TeamContextValidator:
        return cast(TeamContextValidator, super().integrity_checker)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[TeamSearchSearchContext]:
        """
        Certify a candidate is a TeamSearchContext that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if integrity_checker
                returns a failure.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[TeamSearchContext]
        Raises:
            TeamContextValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that integrity_checker flags the candidate.
        validation = self.integrity_checker.execute(candidate=candidate)
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
        context = cast(TeamSearchSearchContext, validation.payload)
        return ValidationResult.success(context)

