# src/space/stepper/space.py

"""
Module: space.stepper.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from result import ComputationResult
from toolkit import MathToolkit
from util import LoggingLevelRouter


T = TypeVar("T", bound="Space")


class Stepper(ABC, Generic[T]):
    
    _math_toolkit: MathToolkit
    
    def __init__(self, math_toolkit: MathToolkit | None = MathToolkit ):
        self._math_toolkit = math_toolkit
        
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def next(self) -> ComputationResult:
        pass