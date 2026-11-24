# src/authorization/permitter/crud/deletion/permitter.py

"""
Module: authorization.permitter.crud.deletion.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import DeletionDecision
from authorization import CrudPermitter
from bootstrap import DeletionAuthorizationLoader
from exchange import DeletionPermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="DeletionPermissionRequest")

class DeletionPermitter(CrudPermitter[T], ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about an DeletionPermissionRequest.

    Attributes:
        loader: DeletionAuthorizationLoader[T]

    Provides:
        -   def execute(candidate: Any) -> DeletionDecision

    Super Class:
        CrudPermitter
    """
    
    def __init__(self, loader: DeletionAuthorizationLoader[T]):
        """
        Args:
            loader: DeletionAuthorizationLoader[T]
        """
        super().__init__(loader=loader)
    
    @property
    def loader(self) -> DeletionAuthorizationLoader[T]:
        return cast(DeletionAuthorizationLoader[T], super().loader)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> DeletionDecision:
        """
        Grant permission for an activity.
        
        Args:
            candidate: Any
        Returns:
           DeletionDecision
        Raises:
            DeletionPermitterException
        """
        