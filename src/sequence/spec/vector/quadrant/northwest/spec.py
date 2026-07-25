# src/spec/sequencevector/quadrant/northwest/spec.py

"""
Module: spec.sequence.vector.quadrant.northwest.spec
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from mapping import NorthwestMapFunction
from space import NorthwestQuadrant
from specification import QuadrantVectorSpec


class NorthwestQuadrantVectorSpec(QuadrantVectorSpec[NorthwestQuadrant]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next NorthwestQuadrant vector.

    Attributes:
        space: NorthwestQuadrant
        mapping_function: Optional[NorthwestMapFunction]

    Provides:

    Super Class:
        QuadrantVectorSequenceSpec
    """
    
    def __init__(
            self,
            space: NorthwestQuadrant,
            mapping_function: Optional[NorthwestMapFunction] | None = NorthwestMapFunction()
    ):
        """
        Args:
            space: NorthwestQuadrant
            mapping_function: Optional[NorthwestMapFunction]
        """
        super().__init__(space=space, mapping_function=mapping_function)
        
    @property
    def space(self) -> NorthwestQuadrant:
        return cast(NorthwestQuadrant, super().space)
    
    @property
    def mapping_function(self) -> NorthwestMapFunction:
        return cast(NorthwestMapFunction, super().mapping_function)

