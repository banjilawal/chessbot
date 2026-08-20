# src/dispatcher/authorization/dispatcher.py

"""
Module: dispatcher.authorization.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from authorization import RequestAuthorizer
from report import AuthorizationDecision
from request import Request
from result import Result
from util import LoggingLevelRouter

T = TypeVar("T", bound="Result")

class AuthorizationDispatcher(ABC, Generic[T]):
    
    _authorizer: RequestAuthorizer[T]
    
    def __init__(self, authorizer: RequestAuthorizer[T]):
        """
        Args:
            authorizer: RequestAuthorizer[T]
        """
        self._authorizer = authorizer
        
    @property
    def authorizer(self) -> RequestAuthorizer[T]:
        return self._authorizer
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Request[T]) -> AuthorizationDecision:
        pass