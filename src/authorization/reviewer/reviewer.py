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
from authorization import Checker
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
    
    Provides:
        -   def execute(request: T) -> Decision[T]

    Super Class:
    """
    
    def __init__(self,):
        """"""
        
    @property
    @abstractmethod
    def checkers(self) -> List[Checker]:
        pass
        
        
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        pass
        