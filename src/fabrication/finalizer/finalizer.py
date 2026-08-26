# src/fabrication/finalizer/finalizer.py

"""
Module: fabrication.finalizer.finalizer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import BuildResult
from util import LoggingLevelRouter


T = TypeVar("T")


class BuildFinalizer(ABC, Generic[T]):
    

    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, item: T) -> BuildResult[T]:
        pass