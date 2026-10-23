# src/authorization/chain/role/checker.py

"""
Module: authorization.chain.role.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import Decision
from authorization import Checker, RoleChainable
from exchange import AuthorizationRequest, ValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="AuthorizationRequest")

class RoleChecker(Checker[T], RoleChainable, ABC, Generic[T]):
    """
    Role:
        -   Authorization
        -   Interface

    Responsibilities:
        1.  Decides if an Actionable satisfies a Request's conditions.

    Attributes:
        
    Provides:
        -   def execute(request: T) -> Decision[T]

    Super Class:
        Checker
    """
    
    _validation_service: ValidationService
    
    def __init__(self, validation_service: ValidationService):
        """
        Args:
            validation_service: Optional[ValidationService]
        """
        super().__init__()
        self._validation_service = validation_service
    
    @property
    def validation_service(self) -> ValidationService:
        return self._validation_service
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        """
        Decide if a Request can be fulfilled with an Actionable.
        Args:
            request: T
        Returns:
           Decision[T]
        Raises:
          RoleCheckerException
        """
        pass