# src/bootstrap/loader.py

"""
Module: bootstrap.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import Result
from util import LoggingLevelRouter

T = TypeVar("T", bound="Result")

class Loader(ABC, Generic[T]):
    pass

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> Result[T]:
        pass