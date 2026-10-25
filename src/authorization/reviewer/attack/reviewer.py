# src/authorization/reviewer/attack/reviewer.py

"""
Module: authorization.reviewer.attack.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar, cast

from artifcat import AttackDecision
from authorization import ActorChainable, ApplicantReviewer, ReadyChecker
from domain import Actor
from exchange import AttackPermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="Actor")

class AttackApplicantReviewer(ApplicantReviewer[AttackPermissionRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Interface for implementing a Attack applicant permission check chain.

    Attributes:
        ready_checker: ReadyChecker[T]
        checkers: List[ActorChainable]

    Provides:
        -   def execute(request: AttackPermissionRequest) -> AttackDecision

    Super Class:
        ApplicantReviewer
    """
    
    def __init__(self, ready_checker: ReadyChecker):
        """
        Args:
            ready_checker: ReadyChecker
        """
        super().__init__(ready_checker=ready_checker)
        
    @property
    def ready_checker(self) -> ReadyChecker[T]:
        return cast(ReadyChecker[T], super().ready_checker)
    
    @property
    @abstractmethod
    def checkers(self) -> List[ActorChainable]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AttackPermissionRequest) -> AttackDecision:
        """
        Decide if an applicant can be promoted.
        Args:
            request: AttackPermissionRequest
        Returns:
            AttackDecision
        Raises:
            AttackApplicantReviewerException
        """
        pass

        