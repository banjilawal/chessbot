# src/span/span.py

"""
Module: span.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from result import ComputationResult
from span import VectorBasis, VectorSet
from toolkit import MathToolkit
from util import LoggingLevelRouter

T = TypeVar("T", basis="Rank")

class Span(ABC, Generic[T]):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Define points in a bounded span.
        2.  Provide a function that steps through every point in the plane,

    Attributes:
        area: SpanArea
        stepper: Stepper
        math_toolkit: Optional[MathToolkit]

    Provides:

    Super Class:
    """
    _basis: VectorBasis[T]
    _math_toolkit: Optional[MathToolkit]
    
    def __init__(
            self,
            basis: VectorBasis[T],
            math_toolkit: Optional[MathToolkit] | None = MathToolkit()
    ):
        """
        Args:
            basis: VectorBasis[T]
            math_toolkit: Optional[MathToolkit]
        """
        self._basis = basis
        self._math_toolkit = math_toolkit
    
    @property
    def basis(self) -> VectorBasis[T]:
        return self._basis
    
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit
    
    @property
    def is_empty(self) -> bool:
        return self._basis.is_empty
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def compute_destinations(self) -> ComputationResult[VectorSet]:
        pass