# src/spec/sequencevector/quadrant/southwest/spec.py

"""
Module: spec.sequence.vector.quadrant.southwestt.spec
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from mapping import SouthwestMapFunction
from space import SouthwestQuadrant
from specification import QuadrantVectorSpec


class SouthwestQuadrantVectorSpec(QuadrantVectorSpec[SouthwestQuadrant]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next SouthwestQuadrant vector.

    Attributes:
        space: SouthwestQuadrant
        mapping_function: Optional[SouthwestMapFunction]

    Provides:

    Super Class:
        QuadrantVectorSequenceSpec
    """
    
    def __init__(
            self,
            space: SouthwestQuadrant,
            mapping_function: Optional[SouthwestMapFunction] | None = SouthwestMapFunction()
    ):
        """
        Args:
            space: SouthwestQuadrant
            mapping_function: Optional[SouthwestMapFunction]
        """
        super().__init__(space=space, mapping_function=mapping_function)
        
    @property
    def space(self) -> SouthwestQuadrant:
        return cast(SouthwestQuadrant, super().space)
    
    @property
    def mapping_function(self) -> SouthwestMapFunction:
        return cast(SouthwestMapFunction, super().mapping_function)

