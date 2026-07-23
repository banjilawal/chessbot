# src/spec/sequencevector/quadrant/northeast/spec.py

"""
Module: spec.sequence.vector.quadrant.northeast.spec
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from mapping import NortheastMapFunction
from space import NortheastQuadrant
from specification import QuadrantVectorSpec


class NortheastQuadrantVectorSpec(QuadrantVectorSpec[NortheastQuadrant]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next NortheastQuadrant vector.

    Attributes:
        space: NortheastQuadrant
        mapping_function: Optional[NortheastMapFunction]

    Provides:

    Super Class:
        QuadrantVectorSequenceSpec
    """
    
    def __init__(
            self,
            space: NortheastQuadrant,
            mapping_function: Optional[NortheastMapFunction] | None = NortheastMapFunction()
    ):
        """
        Args:
            space: NortheastQuadrant
            mapping_function: Optional[NortheastMapFunction]
        """
        super().__init__(space=space, mapping_function=mapping_function)
        
    @property
    def space(self) -> NortheastQuadrant:
        return cast(NortheastQuadrant, super().space)
    
    @property
    def mapping_function(self) -> NortheastMapFunction:
        return cast(NortheastMapFunction, super().mapping_function)

