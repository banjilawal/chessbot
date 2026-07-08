# src/popper/popper.py

"""
Module: popper.popper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from request import PopRequest
from result import DeletionResult
from util import LoggingLevelRouter

T = TypeVar("T")

class Popper(ABC, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: PopRequest) -> DeletionResult[T]:
        pass