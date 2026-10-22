# src/authorization/chain/model/checker.py

"""
Module: authorization.chain.model.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import Decision
from authorization import ActorChainable
from exchange import AuthorizationRequest, ValidationService
from util import LoggingLevelRouter

T = TypeVar("T")

class ModelChecker(ActorChainable, ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks that an Applicant satisfies an authorization requirement.

    Attributes:
        validation_service: ValidationService[T]
        
    Provides:
        -   def execute(request: T) -> Decision[T]
        
    Super Class:
    """
    
    _validation_service: ValidationService[T]
    
    def __init__(self, validation_service: ValidationService[T]):
        """
        Args:
            validation_service: ValidationService[T]
        """
        self._validation_service = validation_service
        
    @property
    def validation_service(self) -> ValidationService[T]:
        return self._validation_service
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AuthorizationRequest) -> Decision:
        pass