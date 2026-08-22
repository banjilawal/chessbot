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

from domain import Request
from report import AuthorizationDecision
from toolkit import RequestToolkit
from util import LoggingLevelRouter


T = TypeVar("T", bound="Request")


class RequestAuthorizer(ABC, Generic[T]):
    """
    Role
        -   Authorization

    Responsibilities:
        1.  Check if a Request satisfies integrity and consistency requirements.

    Attributes:
        toolkit: RequestToolkit[T]

    Provides:
        -   execute(self, request: T) -> AuthorizationDecision

    Super Class:
    """
    _toolkit: RequestToolkit[T]
    
    def __init__(self, toolkit: RequestToolkit[T]):
        """
        Args:
            toolkit: RequestToolkit[T]
        """
        self._toolkit = toolkit
        
    @property
    def toolkit(self) -> RequestToolkit[T]:
        return self._toolkit
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> AuthorizationDecision:
        """
        Args:
            request: T
        Returns:
            AuthorizationDecision
        Raises:
            RequestAuthorizerException
        """
        pass