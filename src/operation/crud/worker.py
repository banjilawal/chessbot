# src/operation/crud/worker.py

"""
Module: operation.crud.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from operation import Worker

T = TypeVar("T", bound="CrudResult")


class CrudWorker(Worker[T], ABC, Generic[T]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes a CrudRequest

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