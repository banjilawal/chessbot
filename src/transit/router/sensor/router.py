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
from assurance import ContextValidator
from collection import Stack
from domain import Context, Model
from sensor import IdSensor
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")

class SensorRouter(ABC, Generic[T]):
    """
    Role
        -   Task Routing

    Responsibilities:
        1.  Route jobs to an AttributeSensor by Context.

    Attributes:
        id_sensor: IdSensor

    Provides:
        -   def execute(context: Context[T]) -> CollisionReport

    Super Class:
    """
    
    _id_sensor: IdSensor
    _context_validator: ContextValidator
    
    def __init__(
            self,
            id_sensor: IdSensor,
            context_validator: ContextValidator,
    ):
        """
        Args:
            id_sensor: IdSensor
            context_validator: ContextValidator
        """
        self._id_sensor = id_sensor
        self._context_validator = context_validator
        
    @property
    def id_sensor(self) -> IdSensor:
        return self._id_sensor
    
    @property
    def context_validator(self) -> ContextValidator:
        return self._context_validator
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, context: Context[T], stream: Stack[T]) -> CollisionReport:
        pass
        
        