# src/authorization/reviewer/reviewer.py

"""
Module: authorization.reviewer.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

from artifcat import Decision
from authorization import ActorChainable, ReadyChecker
from exchange import PermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="PermissionRequest")

class ApplicantReviewer(ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Run the series of ApplicantCheckers.

    Attributes:
        model_checker: ModelChecker
        checkers: List[ActorChainable]
    
    Provides:
        -   def execute(request: T) -> Decision[T]

    Super Class:
    """
    
    _ready_checker: ReadyChecker
    
    def __init__(self, ready_checker: ReadyChecker):
        self._ready_checker = ready_checker
        
    @property
    def ready_checker(self) -> ReadyChecker:
        return self._ready_checker
    
    @property
    @abstractmethod
    def checkers(self) -> List[ActorChainable]:
        pass
        
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        """
        Decide if authorization should be granted.
        Args:
            request: T
        Returns:
           Decision[T]
        Raises:
          ApplicantReviewerException
        """
        pass