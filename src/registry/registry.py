# src/registry/registry.py

"""
Module: registry.registry
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar


from domain.model import Model
from suite import OperationSuite, SensorSuite

T = TypeVar("T", bound="Model")

class Registry(ABC, Generic[T]):
    _operations: OperationSuite
    _sensors: SensorSuite
    
    def __init__(self, operations: OperationSuite, sensors: SensorSuite):
        self._operations = operations
        self._sensors = sensors
        
    @property
    def operations(self) -> OperationSuite:
        return self._operations
    
    @property
    def sensors(self) -> SensorSuite:
        return self._sensors
    