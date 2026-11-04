# src/sensor/collision/id/sensor.py

"""
Module: sensor.collision.id.sensor
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
    """
    ID_IDENTIFIER = "id"
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, target: T, stream: Stack[T]) -> CollisionReport:
        """
        Check that the attractor will be unique in the collection.

        Action:
            1.  Send an exception chain in the collision report if either duplicate;
                ids, emails, or machine_names are detected.
            2.  Otherwise, report the attractor is unique.
        Args:
            target: T
            stream: collection: Stack[T]
        Result:
            CollisionReport
        Raises:
            IdSensorException
        """
        pass
    
    
