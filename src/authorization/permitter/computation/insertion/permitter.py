# src/authorization/permitter/computation/insertion/permitter.py

"""
Module: authorization.permitter.computation.insertion.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import InsertionDecision
from authorization import ComputationPermitter
from bootstrap import InsertionAuthorizationLoader
from exchange import InsertionPermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="InsertionPermissionRequest")

class InsertionPermitter(ComputationPermitter[T], ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about an InsertionPermissionRequest.

    Attributes:
        loader: InsertionAuthorizationLoader[T]

    Provides:
        -   def execute(candidate: Any) -> InsertionDecision

    Super Class:
        ComputationPermitter
    """
    
    def __init__(self, loader: InsertionAuthorizationLoader[T]):
        """
        Args:
            loader: InsertionAuthorizationLoader[T]
        """
        super().__init__(loader=loader)
    
    @property
    def loader(self) -> InsertionAuthorizationLoader[T]:
        return cast(InsertionAuthorizationLoader[T], super().loader)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> InsertionDecision:
        """
        Grant permission for an activity.
        
        Args:
            candidate: Any
        Returns:
           InsertionDecision
        Raises:
            InsertionPermitterException
        """
        