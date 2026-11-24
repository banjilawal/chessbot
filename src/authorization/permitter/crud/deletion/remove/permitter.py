# src/authorization/permitter/crud/deletion/remove/permitter.py

"""
Module: authorization.permitter.crud.deletion.remove.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import RemoveDecision
from authorization import DeletionPermitter
from bootstrap import RemoveAuthorizationLoader
from exchange import RemovePermissionRequest
from production import CollisionManager
from util import LoggingLevelRouter

T = TypeVar("T", bound="RemovePermissionRequest")

class RemoveNodePermitter(DeletionPermitter[T], ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about a RemovePermissionRequest.


    Attributes:
        loader: RemoveAuthorizationLoader[T]
        collision_manager: CollisionManager[T]

    Provides:
        -   def execute(candidate: Any) -> RemoveDecision

    Super Class:
        DeletionPermitter
    """
    
    _collision_manager: CollisionManager[T]
    
    def __init__(
            self,
            loader: RemoveAuthorizationLoader[T],
            collision_manager: CollisionManager[T],
    ):
        """
        Args:
            loader: RemoveAuthorizationLoader[T]
            collision_manager: CollisionManager[T]
        """
        super().__init__(loader=loader)
        self._collision_manager = collision_manager
    
    @property
    def collision_manager(self) -> CollisionManager[T]:
        return self._collision_manager
    
    @property
    def loader(self) -> RemoveAuthorizationLoader[T]:
        return cast(RemoveAuthorizationLoader[T], super().loader)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> RemoveDecision:
        """
        Grant permission for a stack remove.
        
        Args:
            candidate: Any
        Returns:
           RemoveDecision
        Raises:
            RemovePermitterException
        """
        