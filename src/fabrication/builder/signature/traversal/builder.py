# src/fabrication/builder/pattern/traversal/fabrication/builder.py

"""
Module: fabrication.builder.pattern.traversal.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from fabrication.builder import SignatureBuilder
from util import LoggingLevelRouter

T = TypeVar("T", bound="TraversalSignature")

class TraversalBuilder(SignatureBuilder, ABC, Generic[T]):
    """
    Role:
        -   Iteration


    Responsibilities:
        1.  Stepping function which gives the next vector in a series.

    Attributes:
        stepper: Stepper
        math_toolkit: Optional[MathToolkit]

    Provides:

    Super Class:
    """
    
    def __init__(self, builder_toolkit: TraversalBuilderToolkit[T]):
        super().__init__(builder_toolkit=builder_toolkit)
        
    @property
    def builder_toolkit(self) -> TraversalBuilderToolkit[T]:
        return cast(TraversalBuilderToolkit[T], super().builder_toolkit)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, builder: TraversalBuilder[T]) -> BuildResult[T]:
        pass