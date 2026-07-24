# src/builder/container/vector/builder.py

"""
Module: builder.container.vector.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar


from model import Vector

from result import BuildResult
from toolkit import MathToolkit
from util import LoggingLevelRouter


T = TypeVar("T", bound="Space")

class SpaceBuilder(ABC, Generic[T]):
    _math_toolkit: MathToolkit
    
    def __init__(self, math_toolkit: Optional[MathToolkit] | None = MathToolkit()):
        self._math_toolkit = math_toolkit
        
        
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, origin: Vector) -> BuildResult[T]:
        pass
