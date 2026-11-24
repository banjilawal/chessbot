# src/authorization/permitter/crud/insertion/add/permitter.py

"""
Module: authorization.permitter.crud.insertion.add.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import AddDecision
from authorization import InsertionPermitter
from bootstrap import AddAuthorizationLoader
from exchange import AddPermissionRequest
from production import CollisionManager
from util import LoggingLevelRouter

T = TypeVar("T", bound="AddPermissionRequest")

class AddNodePermitter(InsertionPermitter[T], ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about a AddPermissionRequest.


    Attributes:
        loader: AddAuthorizationLoader[T]
        collision_manager: CollisionManager[T]

    Provides:
        -   def execute(candidate: Any) -> AddDecision

    Super Class:
        InsertionPermitter
    """
    
    _collision_manager: CollisionManager[T]
    
    def __init__(
            self,
            loader: AddAuthorizationLoader[T],
            collision_manager: CollisionManager[T],
    ):
        """
        Args:
            loader: AddAuthorizationLoader[T]
            collision_manager: CollisionManager[T]
        """
        super().__init__(loader=loader)
        self._collision_manager = collision_manager
    
    @property
    def collision_manager(self) -> CollisionManager[T]:
        return self._collision_manager
    
    @property
    def loader(self) -> AddAuthorizationLoader[T]:
        return cast(AddAuthorizationLoader[T], super().loader)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> AddDecision:
        """
        Grant permission for a stack add.
        
        Args:
            candidate: Any
        Returns:
           AddDecision
        Raises:
            AddPermitterException
        """
        