# src/span/area/span.py

"""
Module: span.area.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from result import ComputationResult
from span import SpanBounds, VectorSet
from toolkit import MathToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bounds="Rank")

class Span(ABC, Generic[T]):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Define points in a bounded span.
        2.  Provide a function that steps through every point in the plane,

    Attributes:
        area: Span.AreaArea
        stepper: Stepper
        math_toolkit: Optional[MathToolkit]

    Provides:

    Super Class:
    """
    _bounds: SpanBounds[T]
    _math_toolkit: Optional[MathToolkit]
    
    def __init__(
            self,
            bounds: SpanBounds[T],
            math_toolkit: Optional[MathToolkit] | None = MathToolkit()
    ):
        """
        Args:
            bounds: SpanBounds[T]
            math_toolkit: Optional[MathToolkit]
        """
        self._bounds = bounds
        self._math_toolkit = math_toolkit
    
    @property
    def bounds(self) -> SpanBounds[T]:
        return self._bounds
    
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit
    
    @property
    def is_empty(self) -> bool:
        return self._bounds.is_empty
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def destination_vectors(self) -> ComputationResult[VectorSet]:
        pass