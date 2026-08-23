# src/operation/collection/operation.py

"""
Module: operation.collection.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import CollectionRequest, OperationPermitter
from operation import Operator
from util import LoggingLevelRouter


T = TypeVar("T", bound="Result")


class CollectionOperation(Operator, ABC, Generic[T]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Execute a task on a Collection that produces either an Insertion, Deletion, Update
            or Search Result.

    Attributes:
        permitter: CollectionOperationPermitter[T]
        
    Provides:
        -   def execute(request: CollectionRequest[T]) -> T

    Super Class:
        Operation
    """
    
    def __init__(self, id: int, permitter: CollectionOperationPermitter[T]):
        """
        Args:
            permitter: CollectionOperationPermitter[T]
        """
        super().__init__(id=id, permitter=permitter)
        
    @property
    def permitter(self) -> OperationPermitter[T]:
        return cast(CollectionOperationPermitter, super().permitter)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: CollectionRequest[T]) -> T:
        pass