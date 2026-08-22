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
from report import AuthorizationDecision
from toolkit import RequestToolkit
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
    
    def __init__(self, toolkit: RequestToolkit[T]):
        """
        Args:
            toolkit: CrudRequestToolkit[T]
        """
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> RequestToolkit[T]:
        return cast(RequestToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> AuthorizationDecision:
        """
        Args:
            request: T
        Returns:
            AuthorizationDecision
        Raises:
            CrudAuthorizerException
        """
        pass