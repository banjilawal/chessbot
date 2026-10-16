# src/transit/dispatcher/fabrication/space/span/validator.py

"""
Module: transit.dispatcher.fabrication.space.span.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import BuildResult
from transit.dispatcher.fabrication import SpaceBuildDispatcher

T = TypeVar("T", bound="Span")

class SpanValidator(SpaceBuildDispatcher, Generic[T]):
    
       @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> BuildResult[T]:
        pass
    
    