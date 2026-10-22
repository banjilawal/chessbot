# src/authorization/checker/valid/activity.checker.py

"""
Module: authorization.checker.valid.activity.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypeVar, cast

from artifcat import Decision
from authorization import ValidItemChecker
from domain import Actionable
from exchange import AuthorizationRequest, ValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="Actionable")

class ValidRoleChecker(ValidItemChecker[T], ABC):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Verifies an Actionable meets minimum safety requirements.

    Attributes:
        validation_service: ValidationService[T]
        
    Provides:
        -   def execute(request: AuthorizationRequest) -> Decision


    Super Class:
        ValidItemChecker
    """
    
    def __init__(self, validation_service: ValidationService[T]):
        """
        Args:
            validation_service: ValidationService[T]
        """
        super().__init__(validation_service=validation_service)
        
    @property
    def validation_service(self) -> ValidationService[T]:
        return cast(ValidationService[T], super().validation_service)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AuthorizationRequest) -> Decision:
        pass