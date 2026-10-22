# src/authorization/reviewer/applicant/reviewer.py

"""
Module: authorization.reviewer.applicant.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, List, Type, TypeVar, cast

from artifcat import Decision
from authorization import ApplicantChecker, Attributable, Checkable, Checker, Reviewer, ValidApplicantChecker
from exchange import AuthorizationRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="AuthorizationRequest")

class ApplicantReviewer(Reviewer[T], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if an Actor satisfies the requirements to perform an
            activity.

    Attributes:
        valid_applicant_checker: ValidApplicantChecker[T]

    Provides:
        -   def execute(request: T) -> Decision[T]

    Super Class:
    """
    _valid_applicant_checker: ValidApplicantChecker[T]
    
    def __init__(self, valid_applicant_checker: ValidApplicantChecker[T]):
        """
        Args:
            valid_applicant_checker: ValidApplicantChecker[T]
        """
        super().__init__()
        self._valid_applicant_checker =valid_applicant_checker
        
    @property
    def valid_applicant_checker(self) -> ValidApplicantChecker[T]:
        return self._.valid_applicant_checker
    
    @property
    @abstractmethod
    def checkers(self) -> List[ApplicantChecker]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        pass
        