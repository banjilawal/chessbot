# src/command/interpreter/interpreter.py

"""
Module: command.interpreter.interpreter
Author: Banji Lawal
Created: 2026-03-01
version: 1.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from request import Request
from util import LoggingLevelRouter

T = TypeVar("T", bound="Request")


class CommandInterpreter(ABC, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, command) -> T:
        pass
    