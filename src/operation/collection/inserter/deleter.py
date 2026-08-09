# src/deleter/deleter.py

"""
Module: deleter.deleter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar


from util import LoggingLevelRouter

T = TypeVar("T", bound="Collection")

class Inserter(ABC, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: InsertionRequest) -> InsertionResult:
        pass