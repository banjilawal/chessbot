# src/sensor/collision/detector.py

"""
Module: sensor.collision.detector
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
from sensor import Sensor
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")


class CollisionSensor(Sensor, ABC, Generic[T]):
    """
    Role:
        -   Sensor

    Responsibilities:
        1.  Detect if an item violates a Stack uniqueness constraint.

    Attributes:

    Provides:
        -   def execute(attractor: T, collection: Stack[T]) -> AttributeCollisionReport

    Super Class:
        Sensor
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, attractor: T, collection: Stack[T]) -> CollisionReport:
        """
        Check the attractor satisfies stack uniqueness constraint.
        Args:
            attractor: T
            collection: Stack[T]
        Result:
            AttributeCollisionReport
        Raises:
            CollisionSensorException
        """
        pass
