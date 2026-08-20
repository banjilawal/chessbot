# src/assurance/validator/model/rank/validator.py

"""
Module: assurance.validator.model.rank.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from err import RankValidatorException
from model import Rank
from assurance.checker import RankRootCertifier
from result import ValidationResult
from util import LoggingLevelRouter
from assurance.validator import ModelValidator


class RankValidator(ModelValidator[Rank]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Rank instance is certified safe, reliable and consistent before use.

    Attributes:
        root_certifier: RankRootCertifier

    Provides:
        -   execute(candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            root_certifier: RankRootCertifier | None = RankRootCertifier(),
    ):
        super().__init__(root_certifier=root_certifier)
        
    @property
    def certifier(self) -> RankRootCertifier:
        return cast(RankRootCertifier, self.certifier)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify the object is a Rank that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                root_certifier test..
            2.  Otherwise, cast the payload into a Rank and send in the success result.
                success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Rank]
        Raises:
             RankValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the candidate is not safe.
        certification = self.certifier.execute(candidate)
        if certification.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidatorException.MSG,
                    err_code=RankValidatorException.ERR_CODE,
                    ex=certification.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            cast(
                self.certifier.toolkit.model,
                certification.payload
            )
        )