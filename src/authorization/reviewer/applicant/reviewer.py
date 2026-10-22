# src/authorization/reviewer/applicant/reviewer.py

"""
Module: authorization.reviewer.applicant.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

from artifcat import Decision
from authorization import ActorChainable, Reviewer
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

    Provides:
        -   def execute(request: T) -> Decision[T]

    Super Class:
        Reviewer
    """
    
    def __init__(self,):
        """"""
        super().__init__()
    
    @property
    @abstractmethod
    def checkers(self) -> List[ActorChainable]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        pass
        