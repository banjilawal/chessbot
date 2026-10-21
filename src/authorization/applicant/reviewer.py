# src/authorization/applicant/approver.py

"""
Module: authorization.applicant.approver
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from artifcat import ValidationResult
from assurance import PrimingValidator
from domain import Actor
from exchange import ValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="Actor")

class ApplicantApprover(ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if an Actor satisfies the requirements to perform an
            activity.

    Attributes:
        priming_validator: PrimingValidator
        validation_service: ValidationService[T]

    Provides:
        -   def execute(request: T) -> Decision[T]

    Super Class:
    """
    _priming_validator: PrimingValidator
    _validation_service: ValidationService[T]
    
    def __init__(
            self,
            validation_service: ValidationService[T],
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            validation_service: ValidationService[T]
            priming_validator: Optional[PrimingValidator]
        """
        self._validation_service = validation_service
        self._priming_validator = priming_validator or PrimingValidator()
        
    @property
    def validation_service(self) -> ValidationService[T]:
        return self._validation_service
        
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def run_validation_check(self, applicant: Any) -> ValidationResult[T]:
        """
        Checks if an applicant meets basic safety requirements.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate gets
                flagged.
            2.  Otherwise, send the success result.
        Args:
            applicant: Any
        Returns:
           ValidationResult[T]
        Raises:
            ApplicantApproverException
        """
        pass
        