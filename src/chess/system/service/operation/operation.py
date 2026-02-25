# src/chess/system/service/menu/operation/operation.py

"""
Module: chess.system.service.menu.operation.operation
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, TypeVar

T = TypeVar("T")

class ServiceOperation(ABC, Generic[T]):
    """
    A class representing a service operation.
    """
    _name: str
    _params: Dict[str: Any]
    
    def __init__(self, name: str, params: Dict[str, Any]):
        self._name = name
        self._params = params
    
    @property
    def name(self):
        return self._name
    
    @property
    def params(self):
        return self._params
    
    @classmethod
    @abstractmethod
    def key(cls) -> T:
        pass