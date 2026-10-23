# src/authorization/reviewer/reviewer.py

"""
Module: authorization.reviewer.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import Decision
from exchange import AuthorizationRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="AuthorizationRequest")

class ApplicantReviewer(ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Run the series of ApplicantCheckers.

    Attributes:
    
    Provides:
        -   def execute(request: T) -> Decision[T]

    Super Class:
    """
    
    def __init__(self):
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