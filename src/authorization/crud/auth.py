# src/authorization/crud/authorization.py

"""
Module: authorization.crud.authorization
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import RequestAuthorizer
from domain import CrudRequest
from artifcat.report import AuthorizationDecision
from operation.toolkit import PermissionRuleset
from util import LoggingLevelRouter


T = TypeVar("T", bound="CrudRequest")


class CrudAuthorizer(RequestAuthorizer[T], ABC, Generic[T]):
    """
    Role
        -   Authorization

    Responsibilities:
        1.  Check if a CrudRequest satisfies integrity and consistency requirements.

    Attributes:
        toolkit: CrudRequestToolkit[T]

    Provides:
        -   execute(self, request: T) -> AuthorizationDecision

    Super Class:
    """
    
    def __init__(self, ruleset: PermissionRuleset[T]):
        """
        Args:
            ruleset: CrudRequestToolkit[T]
        """
        super().__init__(ruleset=ruleset)
        
    @property
    def ruleset(self) -> PermissionRuleset[T]:
        return cast(PermissionRuleset[T], super().ruleset)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> AuthorizationDecision:
        """
        Decide if CrudRequest satisfies permission requirements.
        Args:
            request: T
        Returns:
            AuthorizationDecision
        Raises:
            CrudAuthorizerException
        """
        pass