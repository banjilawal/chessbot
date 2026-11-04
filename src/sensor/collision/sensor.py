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

P = TypeVar("P", bound="Model")
T = TypeVar("T")


class CollisionSensor(Sensor, ABC, Generic[P, T]):
    """
    Role:
        -   Sensor

    Responsibilities:
        1.  Detect if an item violates a Stack uniqueness constraint.

    Attributes:

    Provides:
        -   def execute(attractor: T, collection: Stack[T]) -> CollisionReport

    Super Class:
        Sensor
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, target: T, stream: Stack[P]) -> CollisionReport:
        """
        Check the attractor satisfies stack uniqueness constraint.
        Args:
            target: T
            stream: Stack[T]
        Result:
            CollisionReport
        Raises:
            CollisionSensorException
        """
        pass
