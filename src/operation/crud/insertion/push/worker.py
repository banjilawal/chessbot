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

R = TypeVar("R", bound="InsertionResult")
Q = TypeVar("Q", bound="ModelPushRequest")


class ModelPusher(Inserter[R, Q], ABC, Generic[R, Q]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes a PushRequest

    Attributes:
        dispatcher: PushPermissionDispatcher

    Provides:
        -   def execute(request: Q) ->R

    Super Class:
        Inserter
    """
    
    def __init__(self, dispatcher: PushPermissionDispatcher):
        """
        Args:
            dispatcher: PushPermissionDispatcher
        """
        super().__init__(dispatcher=dispatcher)
    
    
    @property
    def dispatcher(self) -> PushPermissionDispatcher:
        return cast(PushPermissionDispatcher, super().dispatcher)
    
    
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