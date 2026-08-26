# src/authorization/authorization.py

"""
Module: authorization.authorization
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import AuthorizationDecision
from authorization import PermissionUtility
from domain import Request
from util import LoggingLevelRouter

T = TypeVar("T", bound="Request")


class RequestAuthorizer(ABC, Generic[T]):
    """
    Role
        -  Authorization

    Responsibilities:
        1.  Check if a Request satisfies integrity and consistency requirements.

    Attributes:
        utility: PermissionUtility[T]

    Provides:
        -  execute(self, request: T) -> AuthorizationDecision

    Super Class:
    """
    _utility: PermissionUtility[T]
    
    def __init__(self, utility: PermissionUtility[T]):
        """
        Args:
            utility: PermissionUtility[T]
        """
        self._utility = utility
        
    @property
    def utility(self) -> PermissionUtility[T]:
        return self._utility
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> AuthorizationDecision:
        """
        Decide if Request satisfies permission requirements.
        Args:
            request: T
        Returns:
            AuthorizationDecision
        Raises:
            RequestAuthorizerException
        """
        pass