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
from toolkit import PermissionRuleset
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
    _ruleset: PermissionRuleset[T]
    
    def __init__(self, ruleset: PermissionRuleset[T]):
        """
        Args:
            ruleset: RequestToolkit[T]
        """
        self._ruleset = ruleset
        
    @property
    def ruleset(self) -> PermissionRuleset[T]:
        return self._ruleset
    
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