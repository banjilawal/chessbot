# src/authorization/permitter/crud/insertion/permitter.py

"""
Module: authorization.permitter.crud.insertion.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import Decision
from authorization import CrudPermitter
from bootstrap import InsertionAuthorizationLoader
from exchange import InsertionPermissionRequest, ValidationService
from sensor import CollisionSensor
from util import LoggingLevelRouter

T = TypeVar("T", bound="InsertionPermissionRequest")

class InsertionPermitter(CrudPermitter[T], ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about an InsertionPermissionRequest then forward
            that decision an Inserter.

    Attributes:
        loader: CrudAuthorizationLoader[T]

    Provides:
        -   def execute(candidate: Any) -> Decision

    Super Class:
        CrudPermitter
    """
    
    def __init__(
            self,
            collision_sensor: CollisionSensor,
            loader: InsertionAuthorizationLoader[T],
    ):
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
    def execute(self, candidate: Any) -> Decision:
        """
        Grant permission for an activity.
        
        Args:
            candidate: Any
        Returns:
           Decision
        Raises:
            InsertionPermitterException
        """
        