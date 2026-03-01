# src/chess/system/command/command.py

"""
Module: chess.system.command.command
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Dict


class Command:
    """
    A class representing a service command.
    """
    _id: int
    _name: str
    _parameters: Dict[str: Any]
    
    def __init__(self, id: int, name: str, parameters: Dict[str, Any]):
        self._id = id
        self._name = name
        self._parameters = parameters
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def parameters(self) -> Dict[str, Any]:
        return self._parameters
    
    def __eq__(self, other: Any) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Command):
            return other.id == self._id
        return False
    
    def __hash__(self) -> int:
        return hash(self._id)
    @classmethod
    @abstractmethod
    def cipher(cls, ) -> T:
        pass