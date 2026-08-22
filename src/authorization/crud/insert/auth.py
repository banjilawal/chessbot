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

from authorization import CrudAuthorizer
from domain import InsertRequest
from report import AuthorizationDecision
from toolkit import InsertRequestToolkit
from util import LoggingLevelRouter


T = TypeVar("T", bound="InsertRequest")


class InsertAuthorizer(CrudAuthorizer[T], ABC, Generic[T]):
    """
    Role
        -   Authorization

    Responsibilities:
        1.  Check if an InsertRequest satisfies integrity and consistency requirements.

    Attributes:
         toolkit: InsertRequestToolkit[T]

    Provides:
        -   execute(self, request: T) -> AuthorizationDecision

    Super Class:
        CrudAuthorizer
    """
    
    def __init__(self, toolkit: InsertRequestToolkit[T]):
        """
        Args:
             toolkit: InsertRequestToolkit[T]
        """
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> InsertRequestToolkit[T]:
        return cast(InsertRequestToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> AuthorizationDecision:
        """
        Args:
            request: T
        Returns:
            AuthorizationDecision
        Raises:
            InsertAuthorizerException
        """
        pass