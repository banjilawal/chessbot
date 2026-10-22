# src/authorization/checker/applicant/checker.py

"""
Module: authorization.checker.applicant.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import Decision
from authorization import Checker
from config.logging_setup import LOGGING_CONFIG
from domain import Actor
from exchange import AuthorizationRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="Actor")

class ApplicantChecker(Checker[T], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks that an Applicant satisfies an authorization requirement.

    Attributes:
        
    Provides:
        -   def execute(request: T) -> Decision[T]
        
    Super Class:
        Checker
    """
    pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AuthorizationRequest) -> Decision:
        pass