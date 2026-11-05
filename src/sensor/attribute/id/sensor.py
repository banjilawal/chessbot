# src/sensor/attribute/id/sensor.py

"""
Module: sensor.attribute.id.sensor
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import CollisionReport
from collection import Stack
from domain import Model
from sensor import AttributeSensor
from util import LoggingLevelRouter

P = TypeVar("P", bound="Model")
T = TypeVar("T", bound="int")


class IdSensor(AttributeSensor[P, T], ABC, Generic[P, T]):
    """
    Role:
        -   Sensor

    Responsibilities:
        1.  Detect if an id has already been used in a DataStruct.

    Attributes:

    Provides:
        -   def execute(attractor: int, collection: Stack[M]) -> CollisionReport

    Super Class:
        AttributeSensor
    """
    
    ID_IDENTIFIER = "id"
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, target: T, stream: Stack[T]) -> CollisionReport:
        """
        Detect if the id of an item in the stream matches the target.

        Args:
            target: T
            stream: Stack[P]
        Result:
            CollisionReport
        Raises:
            IdSensorException
        """
        pass
    
    
