# src/sensor/detector/collision/detector.py

"""
Module: sensor.detector.collision.detector
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

from artifcat import CollisionReport
from domain import Model
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")


class Collider(ABC, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, attractor: T, items: List[T]) -> CollisionReport:
        pass
