# src/bootstrap/operation.py

"""
Module: operation.priming.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from abc import abstractmethod
from typing import TypeVar

from operation import Operation
from result import ValidationResult
from util import LoggingLevelRouter

T = TypeVar("T")

class Primer(Operation[T]):
    DOMAIN = "Priming"
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(cls, *args, **kwargs,) -> ValidationResult[T]:
        pass