# src/authorization/reviewer/activity/reviewer.py

"""
Module: authorization.reviewer.activity.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import Decision
from authorization import  Reviewer, ValidRoleChecker
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
        valid_item_checker: ValidRoleChecker[T]

    Provides:
        -   def execute(request: T) -> Decision[T]

    Super Class:
        Reviewer
    """
    
    def __init__(self, valid_item_checker: ValidRoleChecker[T]):
        """
        Args:
            valid_item_checker: ValidRoleChecker[T]
        """
        super().__init__(valid_item_checker=valid_item_checker)
        
    @property
    def valid_item_checker(self) -> ValidRoleChecker[T]:
        return cast(type[ValidRoleChecker[T]], super().valid_item_checker)

    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        pass
        