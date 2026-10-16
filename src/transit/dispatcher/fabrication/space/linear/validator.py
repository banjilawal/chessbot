# src/transit/dispatcher/fabrication/space/linear/validator.py

"""
Module: transit.dispatcher.fabrication.space.linear.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import BuildResult
from util import LoggingLevelRouter
from transit.dispatcher.fabrication import SpaceBuildDispatcher

T = TypeVar("T", bound="LinearSpace")

class LinearSpaceValidator(SpaceBuildDispatcher, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[T]:
        pass
    
    