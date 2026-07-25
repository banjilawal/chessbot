# src/spec/sequencevector/quadrant/southeast/spec.py

"""
Module: spec.sequence.vector.quadrant.southeast.spec
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from mapping import SoutheastMapFunction
from space import SoutheastQuadrant
from specification import QuadrantVectorSpec


class SoutheastQuadrantVectorSpec(QuadrantVectorSpec[SoutheastQuadrant]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next SoutheastQuadrant vector.

    Attributes:
        space: SoutheastQuadrant
        mapping_function: Optional[SoutheastMapFunction]

    Provides:

    Super Class:
        QuadrantVectorSequenceSpec
    """
    
    def __init__(
            self,
            space: SoutheastQuadrant,
            mapping_function: Optional[SoutheastMapFunction] | None = SoutheastMapFunction()
    ):
        """
        Args:
            space: SoutheastQuadrant
            mapping_function: Optional[SoutheastMapFunction]
        """
        super().__init__(space=space, mapping_function=mapping_function)
        
    @property
    def space(self) -> SoutheastQuadrant:
        return cast(SoutheastQuadrant, super().space)
    
    @property
    def mapping_function(self) -> SoutheastMapFunction:
        return cast(SoutheastMapFunction, super().mapping_function)

