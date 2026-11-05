# src/production/manager/sensor/manager.py

"""
Module: production.manager.sensor.manager
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import CollisionReport
from domain import Context, Model
from transit import SensorRouter
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")


class CollisionDetector(ABC, Generic[T]):
    _router: SensorRouter
    
    def __init__(self, router: SensorRouter[T]):
        self._router = router
        
    @property
    def router(self) -> SensorRouter[T]:
        return self._router
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, context: Context[T]) -> CollisionReport:
        pass