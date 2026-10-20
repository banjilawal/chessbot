# src/authorization/applicant/approver.py

"""
Module: authorization.applicant.approver
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from artifcat import Decision
from assurance import PrimingValidator
from exchange import AuthorizationRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="AuthorizationRequest")

class ApplicantApprover(ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if an Applicant satisfies the condition for a Permit.

    Attributes:
        priming_validator: PrimingValidator

    Provides:
        -   def execute(request: T) -> Decision[T]

    Super Class:
    """
    _priming_validator: PrimingValidator

    
    def __init__(self, priming_validator: Optional[PrimingValidator] | None = None,):
        self._priming_validator = priming_validator or PrimingValidator()
        
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        pass
        