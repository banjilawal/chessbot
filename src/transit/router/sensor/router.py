# src/transit/route/sensor/router.py

"""
Module: transit.route.sensor.router
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import CollisionReport
from domain import Context, Model
from sensor import IdSensor
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")

class SensorRouter(ABC, Generic[T]):
    
    _id_sensor: IdSensor
    
    def __init__(self, id_sensor: IdSensor):
        """
        Args:
            id_sensor: IdSensor
        """
        self._id_sensor = id_sensor
        
    @property
    def id_sensor(self) -> IdSensor:
        return self._id_sensor
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, context: Context[T]) -> CollisionReport:
        pass
        
        