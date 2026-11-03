# src/authorization/permitter/crud/insertion/push/permitter.py

"""
Module: authorization.permitter.crud.insertion.push.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import PushDecision
from authorization import InsertionPermitter
from bootstrap import PushAuthorizationLoader
from exchange import PushPermissionRequest
from sensor import CollisionSensor
from util import LoggingLevelRouter

T = TypeVar("T", bound="PushPermissionRequest")

class PushPermitter(InsertionPermitter[T], ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about a PushPermissionRequest.


    Attributes:
        collision_sensor: CollisionSensor
        loader: PushAuthorizationLoader[T]

    Provides:
        -   def execute(candidate: Any) -> PushDecision

    Super Class:
        InsertionPermitter
    """
    
    _collision_sensor: CollisionSensor
    
    def __init__(
            self,
            loader: PushAuthorizationLoader[T],
            collision_sensor: CollisionSensor,
    ):
        """
        Args:
            collision_sensor: CollisionSensor
            loader: PushAuthorizationLoader[T]
        """
        super().__init__(loader=loader)
        self._collision_sensor = collision_sensor
    
    @property
    def collision_sensor(self) -> CollisionSensor:
        return self._collision_sensor
    
    @property
    def loader(self) -> PushAuthorizationLoader[T]:
        return cast(PushAuthorizationLoader[T], super().loader)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> PushDecision:
        """
        Grant permission for a stack push.
        
        Args:
            candidate: Any
        Returns:
           PushDecision
        Raises:
            PushPermitterException
        """
        