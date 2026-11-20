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
from exchange import ModelPushRequest
from operation import Inserter
from transit import PushPermissionDispatcher
from util import LoggingLevelRouter

Q = TypeVar("Q", bound="ModelPushRequest")
R = TypeVar("R", bound="InsertionResult")


class ModelPusher(Inserter[Q, R], ABC, Generic[Q, R]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes a PushRequest

    Attributes:
        permitter: PushPermissionDispatcher

    Provides:
        -   def execute(request: Q) ->R

    Super Class:
        Inserter
    """
    
    def __init__(self, permitter: PushPermissionDispatcher):
        """
        Args:
            permitter: PushPermissionDispatcher
        """
        super().__init__(permitter=permitter)
    
    
    @property
    def permitter(self) -> PushPermissionDispatcher:
        return cast(PushPermissionDispatcher, super().permitter)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> R:
        """
        Args:
            request: Q
        Result:
            R
        Raises:
            ModelPusherException
        """
        pass