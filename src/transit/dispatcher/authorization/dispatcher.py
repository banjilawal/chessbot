# src/transit/dispatcher/authorization/dispatcher.py

"""
Module: transit.dispatcher.authorization.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import Decision
from authorization import Permitter
from exchange import PermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="PermissionRequest")

class PermissionDispatcher(ABC, Generic[T]):
    """
    Role
        -   Authorization Process Flow

    Responsibilities:
        1.  Direct jobs towards a Permitter then send the results back to clients.

    Attributes:
        permitter: Permitter[T]

    Provides:
        -   def  execute(candidate: Any) -> Decision

    Super Class:
        Dispatcher
    """
    
    _permitter: Permitter[T]
    
    def __init__(self, permitter: Permitter[T]):
        """
        Args:
            permitter: Permitter[T]
        """
        self._permitter = permitter
        
    @property
    def permitter(self) -> Permitter[T]:
        return self._permitter
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> Decision:
        """
        Make a decision about a TransactionRequest
        Args:
            candidate: Any
        Returns:
            Decision
        Raises:
            PermissionDispatcherException
        """
        pass