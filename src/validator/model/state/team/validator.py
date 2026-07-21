# src/validator/model/state/team/validator.py

"""
Module: validator.model.state.team.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from err import TeamValidatorException
from model import Team
from err.root import TeamRootCertifier
from result import ValidationResult
from util import LoggingLevelRouter
from validator import ModelValidator


class TeamValidator(ModelValidator[Team]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Team instance is certified safe, reliable and consistent before use.

    Attributes:
        root_certifier: TeamRootCertifier

    Provides:
        -   execute(candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            root_certifier: TeamRootCertifier | None = TeamRootCertifier(),
    ):
        super().__init__(root_certifier=root_certifier)
        
    @property
    def root_certifier(self) -> TeamRootCertifier:
        return cast(TeamRootCertifier, self.root_certifier)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify the object is a Team that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                root_certifier test..
            2.  Otherwise, cast the payload into a Team and send in the success result.
                success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Team]
        Raises:
             TeamValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the candidate is not safe.
        certification = self.root_certifier.execute(candidate)
        if certification.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidatorException.MSG,
                    err_code=TeamValidatorException.ERR_CODE,
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