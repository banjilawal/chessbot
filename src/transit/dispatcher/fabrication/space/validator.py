# src/transit/dispatcher/fabrication/space/validator.py

"""
Module: transit.dispatcher.fabrication.space.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import BuildResult
from util import LoggingLevelRouter
from transit import BuildDispatcher

T = TypeVar("T", bound="Space")

class SpaceBuildDispatcher(BuildDispatcher, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[T]:
        pass
    
    