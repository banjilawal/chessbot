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
from artifcat.report import AuthorizationDecision
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
    
    def __init__(self, ruleset: DeleteRequestToolkit[T]):
        """
        Args:
             ruleset: DeleteRequestToolkit[T]
        """
        super().__init__(ruleset=ruleset)
        
    @property
    def ruleset(self) -> DeleteRequestToolkit[T]:
        return cast(DeleteRequestToolkit[T], super().ruleset)
    
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