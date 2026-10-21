# src/authorization/reviewer/reviewer.py

"""
Module: authorization.reviewer.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, List, TypeVar

from artifcat import Decision
from authorization import PropertyChecker, ValidItemChecker
from exchange import AuthorizationRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="AuthorizationRequest")

class Reviewer(ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if an Actor satisfies the requirements to perform an
            activity.

    Attributes:
        valid_item_checker: ValidItemChecker[T]

    Provides:
        -   def execute(request: T) -> Decision[T]

    Super Class:
    """
    _valid_item_checker: ValidItemChecker[T]
    
    def __init__(self, valid_item_checker: ValidItemChecker):
        """
        Args:
            valid_item_checker: ValidItemChecker
        """
        self._valid_item_checker = valid_item_checker
        
    @property
    def valid_item_checker(self) -> ValidItemChecker:
        return self._valid_item_checker
    
    @property
    @abstractmethod
    def checkers(self) -> List[PropertyChecker[T]]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        pass
        