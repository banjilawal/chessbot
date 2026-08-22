# src/authorization/crud/delete/authorization.py

"""
Module: authorization.crud.delete.authorization
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import CrudAuthorizer
from domain import DeleteRequest
from report import AuthorizationDecision
from util import LoggingLevelRouter


T = TypeVar("T", bound="DeleteRequest")


class DeleteAuthorizer(CrudAuthorizer[T], ABC, Generic[T]):
    """
    Role
        -   Authorization

    Responsibilities:
        1.  Check if a DeleteRequest satisfies integrity and consistency requirements.

    Attributes:
         toolkit: DeleteRequestToolkit[T]

    Provides:
        -   execute(self, request: T) -> AuthorizationDecision

    Super Class:
        CrudAuthorizer
    """
    
    def __init__(self, toolkit: DeleteRequestToolkit[T]):
        """
        Args:
             toolkit: DeleteRequestToolkit[T]
        """
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> DeleteRequestToolkit[T]:
        return cast(DeleteRequestToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> AuthorizationDecision:
        """
        Args:
            request: T
        Returns:
            AuthorizationDecision
        Raises:
            DeleteAuthorizerException
        """
        pass