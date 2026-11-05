# src/sensor/attribute/account/sensor.py

"""
Module: sensor.attribute.account.sensor
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import CollisionReport
from collection import Stack
from domain import Account
from sensor import AttributeSensor
from util import LoggingLevelRouter

P = TypeVar("P", bound="Account")
T = TypeVar("T")


class AccountSensor(AttributeSensor[P, T], ABC, Generic[P, T]):
    """
    Role:
        -   Sensor

    Responsibilities:
        1.  Detect if an attribute-value exists in the AccountStack.

    Attributes:

    Provides:
        -   def execute(attractor: T, collection: Stack[P]) -> CollisionReport

    Super Class:
        AttributeSensor
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, target: T, stream: Stack[P]) -> CollisionReport:
        """
        Detect if the attribute of an account in the stream matches the target.
        
        Args:
            target: T
            stream: Stack[P]
        Result:
            CollisionReport
        Raises:
            AccountSensorException
        """
        pass
