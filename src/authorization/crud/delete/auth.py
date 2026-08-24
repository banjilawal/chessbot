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

from artifcat import AuthorizationDecision
from authorization import CrudAuthorizer, DeletePermissionUtility
from domain import DeleteRequest
from util import LoggingLevelRouter


T = TypeVar("T", bound="DeleteRequest")


class DeleteAuthorizer(CrudAuthorizer[T], ABC, Generic[T]):
    """
    Role
        -   Authorization

    Responsibilities:
        1.  Check if a DeleteRequest satisfies integrity and consistency requirements.

    Attributes:
         utility: DeletePermissionUtility[T]

    Provides:
        -   execute(self, request: T) -> AuthorizationDecision

    Super Class:
        CrudAuthorizer
    """
    
    def __init__(self, utility: DeletePermissionUtility[T]):
        """
        Args:
             utility: DeletePermissionUtility[T]
        """
        super().__init__(utility=utility)
        
        
    @property
    def utility(self) -> DeletePermissionUtility[T]:
        return cast(DeletePermissionUtility[T], super().utility)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> AuthorizationDecision:
        """
        Decide if a DeleteRequest satisfies permission requirements.
        Args:
            request: T
        Returns:
            AuthorizationDecision
        Raises:
            DeleteAuthorizerException
        """
        pass