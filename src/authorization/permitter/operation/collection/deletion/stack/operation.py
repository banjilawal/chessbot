# src/operation/collection/deletion/stack/operation.py

"""
Module: operation.collection.deletion.stack.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import StackPopRequest

f
from collection import StackService
from operation import CollectionDeletion
from artifcat import DeletionResult
from util import LoggingLevelRouter


T = TypeVar("T", bound="StateModel")


class StackPop(CollectionDeletion[StackService], ABC, Generic[T]):
    """
    Role
        -  Worker

    Responsibilities:
        1.  Remove a T instance out of the StackService[T].

    Attributes:
        permitter: PopStackPermitter[T]
        
    Provides:
        -  def execute(request: PopStackRequest[T]) -> DeletionResult[T]

    Super Class:
        CollectionDeletion
    """
    
    def __init__(self, permitter: PopStackPermitter[T]):
        """
        Args:
            permitter: PopStackPermitter[T]
        """
        super().__init__(permitter=permitter)
    
    @property
    def permitter(self) -> PopStackPermitter[T]:
        return cast(PopStackPermitter[T], super().permitter)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: StackPopRequest[T]) -> DeletionResult[T]:
        pass