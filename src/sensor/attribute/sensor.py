# src/sensor/attribute/sensor.py

"""
Module: sensor.attribute.sensor
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


class AttributeSensor(Sensor, ABC, Generic[P, T]):
    """
    Role:
        -   Sensor

    Responsibilities:
        1.  Detect if an attribute-value exists in a Stack.

    Attributes:

    Provides:
        -   def execute(attractor: T, collection: Stack[P]) -> CollisionReport

    Super Class:
        Sensor
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, target: T, stream: Stack[P]) -> CollisionReport:
        """
        Detect if the attribute of an item in the stream matches the target.
        
        Args:
            target: T
            stream: Stack[P]
        Result:
            CollisionReport
        Raises:
            AttributeSensorException
        """
        pass
