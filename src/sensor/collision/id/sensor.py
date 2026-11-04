# src/sensor/collision/id/sensor.py

"""
Module: sensor.collision.id.sensor
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, List, TypeVar

from artifcat import CollisionReport
from collection import Stack
from domain import Model
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")

class IdCollisionSensor(ABC, Generic[T]):
    """
    Role:
        -   Sensor

    Responsibilities:
        1.  Detect if an id has already been used in a DataStruct.

    Attributes:

    Provides:
        -   def execute(attractor: id, collection: Stack[M]) -> AttributeCollisionReport

    Super Class:
    """

    @LoggingLevelRouter.monitor
    def execute(self, attractor: int, collection: Stack[T]) -> CollisionReport:
        """
        Check that the attractor will be unique in the collection.

        Action:
            1.  Send an exception chain in the collision report if either duplicate;
                ids, emails, or machine_names are detected.
            2.  Otherwise, report the attractor is unique.
        Args:
            attractor: Id
            collection: IdStack
        Result:
            AttributeCollisionReport
        Raises:
            IdCollisionSensorException
        """
        pass
    
    
