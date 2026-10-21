# src/authorization/checker/validation/checker.py

"""
Module: authorization.checker.validation.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypeVar

from artifcat import Decision
from authorization import Checker
from exchange import AuthorizationRequest, ValidationService
from util import LoggingLevelRouter

T = TypeVar("T")

class ValidationChecker(Checker[T], ABC):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if a Token satisfies the requirements for an activity.

    Attributes:
        validation_service: ValidationService[T]
        
    Provides:
        -   def execute(request: T) -> Decision[T]


    Super Class:
        ApplicantApprover
    """
    _validation_service: ValidationService[T]

    
    def __init__(self, validation_service: ValidationService[T]):
        """
        Args:
            validation_service: ValidationService[T]
        """
        
    @property
    def validation_service(self) -> ValidationService[T]:
        return self._validation_service
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AuthorizationRequest) -> Decision:
        pass