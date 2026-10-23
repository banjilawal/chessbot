# src/authorization/reviewer/role/reviewer.py

"""
Module: authorization.reviewer.role.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import Decision
from authorization import Reviewer, RoleChecker
from exchange import AuthorizationRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="AuthorizationRequest")

class RoleReviewer(Reviewer[T], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if an Actor satisfies the requirements to perform an
            activity.

    Attributes:
        checker: RoleChecker[T]

    Provides:
        -   def execute(request: T) -> Decision[T]

    Super Class:
        Reviewer
    """
    _checker: RoleChecker[T]
    
    def __init__(self, checker: RoleChecker[T]):
        """
        Args:
            checker: RoleChecker[T]
        """
        super().__init__()
        self._checker = checker
        
    @property
    def checker(self) -> RoleChecker:
        return self._checker
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        pass
        