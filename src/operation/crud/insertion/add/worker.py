# src/operation/crud/insertion/add/worker.py

"""
Module: operation.crud.insertion.add.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import InsertionResult
from operation import Inserter
from request import AddNodeRequest
from util import LoggingLevelRouter

Q = TypeVar("Q", bound="AddNodeRequest")
R = TypeVar("R")


class NodeAdder(Inserter, ABC, Generic[Q]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes a AddRequest

    Attributes:
        permitter: AddPermissionDispatcher

    Provides:
        -   def execute(request: Q) ->R

    Super Class:
        Inserter
    """
    
    def __init__(self, permitter: AddPermissionDispatcher):
        """
        Args:
            permitter: AddPermissionDispatcher
        """
        super().__init__(permitter=permitter)
    
    
    @property
    def permitter(self) -> AddPermissionDispatcher:
        return cast(AddPermissionDispatcher, super().permitter)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> InsertionResult:
        """
        Args:
            request: Q
        Result:
            InsertionResult
        Raises:
            ModelAdderException
        """
        pass