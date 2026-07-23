# src/ruleset/ruleset/vector/quadrant/southwest/ruleset.py

"""
Module: ruleset.sequence.vector.quadrant.southwest.ruleset
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from mapping import SouthwestQuadrantMapFunction
from ruleset import QuadrantVectorSpec

from space import SouthwestQuadrant


class SouthwestQuadrantVectorSpec(QuadrantVectorSpec[SouthwestQuadrant]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next SouthwestQuadrant vector.

    Attributes:
        space: SouthwestQuadrant
        mapping_function: Optional[SouthwestQuadrantMapFunction]

    Provides:

    Super Class:
        QuadrantVectorSpec
    """
    
    def __init__(
            self,
            space: SouthwestQuadrant,
            mapping_function: Optional[SouthwestQuadrantMapFunction] | None = SouthwestQuadrantMapFunction()
    ):
        """
        Args:
            space: SouthwestQuadrant
            mapping_function: Optional[SouthwestQuadrantMapFunction]
        """
        super().__init__(space=space, mapping_function=mapping_function)
        
    @property
    def space(self) -> SouthwestQuadrant:
        return cast(SouthwestQuadrant, super().space)
    
    @property
    def mapping_function(self) -> SouthwestQuadrantMapFunction:
        return cast(SouthwestQuadrantMapFunction, super().mapping_function)

