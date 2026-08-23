# src/operation/crud/operator.py

"""
Module: operation.crud.operator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import CrudAuthorizer
from domain import CrudRequest
from operation import Operator
from artifcat.result import CrudResult
from util import LoggingLevelRouter


T = TypeVar("T", bound="CrudResult")


class CrudOperator(Operator[T], ABC, Generic[T]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Process a CrudRequest.

    Attributes:
        authorizer: CrudAuthorizer[T]
        
    Provides:
        -   def execute(request: CrudRequest[T]) -> T

    Super Class:
        Operation
    """
    
    def __init__(self, authorizer: CrudAuthorizer[T]):
        """
        Args:
            authorizer: CrudAuthorizer[T]
        """
        super().__init__(authorizer=authorizer)
    
    @property
    def authorizer(self) -> CrudAuthorizer[T]:
        return cast(CrudAuthorizer[T], super().authorizer)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: CrudRequest[T]) -> T:
        """
        Args:
            request: CrudRequest[T]
        Result:
            T
        Raises:
            CrudOperationException
        """
        pass