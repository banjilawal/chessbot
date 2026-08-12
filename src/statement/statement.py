# src/statement/statement.py

"""
Module: statement.statement
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Any


class UserStatement(ABC):
    _name: str
    _arguments: dict[str, Any]
    
    def __init__(self, name: str, arguments: dict[str, Any]):
        self._name = name
        self._arguments = arguments
        
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def arguments(self) -> dict[str, Any]:
        return self._arguments