# src/authorization/checker/applicant/checker.py

"""
Module: authorization.checker.applicant.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypeVar

from artifcat import Decision
from authorization import PropertyChecker
from exchange import AuthorizationRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="AuthorizationRequest")

class ApplicantChecker(PropertyChecker[T], ABC):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks that an Applicant satisfies an authorization requirement.

    Attributes:
        
    Provides:
        -   def execute(request: T) -> Decision[T]
        
    Super Class:
        PropertyChecker
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        pass