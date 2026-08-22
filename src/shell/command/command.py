# src/shell/command/command.py

"""
Module: shell.command.command
Author: Banji Lawal
Created: 2026-03-01
version: 1.0.0
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Generic, TypeVar

from result import Result

T = TypeVar("T", bound="Result")

class Command(ABC, Generic[T]):
    _name: str
    _parameters: dict[str, Any]
    
    def __init__(self, name: str, parameters: dict[str, Any]):
        self._name = name
        self._parameters = parameters
        
    @property
    def name(self) -> str:
        return self._name
    
    def parameters(self) -> dict[str, Any]:
        return self._parameters
