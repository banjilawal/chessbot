# src/authorization/crud/insert/authorization.py

"""
Module: authorization.crud.insert.authorization
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import AuthorizationDecision
from authorization import CrudAuthorizer, InsertPermissionUtility
from domain import InsertRequest
from util import LoggingLevelRouter


T = TypeVar("T", bound="InsertRequest")


class InsertAuthorizer(CrudAuthorizer[T], ABC, Generic[T]):
    """
    Role
        -  Authorization

    Responsibilities:
        1.  Check if an InsertRequest satisfies integrity and consistency requirements.

    Attributes:
         utility: InsertPermissionUtility[T]

    Provides:
        -  execute(self, request: T) -> AuthorizationDecision

    Super Class:
        CrudAuthorizer
    """
    
    def __init__(self, utility: InsertPermissionUtility[T]):
        """
        Args:
             utility: InsertPermissionUtility[T]
        """
        super().__init__(utility=utility)
        
        
    @property
    def utility(self) -> InsertPermissionUtility[T]:
        return cast(InsertPermissionUtility[T], super().utility)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> AuthorizationDecision:
        """
        Decide if an InsertRequest satisfies permission requirements.
        Args:
            request: T
        Returns:
            AuthorizationDecision
        Raises:
            InsertAuthorizerException
        """
        pass