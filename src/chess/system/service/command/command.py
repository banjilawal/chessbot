# src/chess/system/service/command/command.py

"""
Module: chess.system.service.command.command
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, TypeVar

T = TypeVar('T')

class Command(ABC, Generic[T]):
    """
    A class representing a service command.
    """
    _name: str
    _parameters: Dict[str: Any]
    
    def __init__(self, name: str, parameters: Dict[str, Any]):
        self._name = name
        self._parameters = parameters
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def parameters(self) -> Dict[str, Any]:
        return self._parameters
    
    @classmethod
    @abstractmethod
    def key(cls,) -> T:
        pass