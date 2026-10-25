# src/operation/crud/insertion/push/worker.py

"""
Module: operation.crud.insertion.push.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import InsertionResult
from operation import Inserter
from transit import PushPermissionPermitter
from util import LoggingLevelRouter

T = TypeVar("T", bound="PushRequest")


class Pusher(Inserter[T], ABC, Generic[T]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes a PushRequest

    Attributes:
        permitter: PushPermissionPermitter[T]

    Provides:
        -   def execute(self, request: T) -> InsertionResult

    Super Class:
        Inserter
    """
    
    def __init__(self, permitter: PushPermissionPermitter[T]):
        """
        Args:
            permitter: InsertionPermissionPermitter[T]
        """
        super().__init__(permitter=permitter[T])
    
    
    @property
    def permitter(self) -> PushPermissionPermitter[T]:
        return cast(PushPermissionPermitter[T], super().permitter)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> InsertionResult:
        """
        Args:
            request: T
        Result:
            InsertionResult
        Raises:
            PusherException
        """
        pass