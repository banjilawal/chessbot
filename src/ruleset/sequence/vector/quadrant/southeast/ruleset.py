# src/ruleset/ruleset/vector/quadrant/southeast/ruleset.py

"""
Module: ruleset.sequence.vector.quadrant.southeast.ruleset
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from mapping import SoutheastQuadrantMapFunction
from ruleset import QuadrantVectorSpec

from space import SoutheastQuadrant


class SoutheastQuadrantVectorSpec(QuadrantVectorSpec[SoutheastQuadrant]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next SoutheastQuadrant vector.

    Attributes:
        space: SoutheastQuadrant
        mapping_function: Optional[SoutheastQuadrantMapFunction]

    Provides:

    Super Class:
        QuadrantVectorSpec
    """
    
    def __init__(
            self,
            space: SoutheastQuadrant,
            mapping_function: Optional[SoutheastQuadrantMapFunction] | None = SoutheastQuadrantMapFunction()
    ):
        """
        Args:
            space: SoutheastQuadrant
            mapping_function: Optional[SoutheastQuadrantMapFunction]
        """
        super().__init__(space=space, mapping_function=mapping_function)
        
    @property
    def space(self) -> SoutheastQuadrant:
        return cast(SoutheastQuadrant, super().space)
    
    @property
    def mapping_function(self) -> SoutheastQuadrantMapFunction:
        return cast(SoutheastQuadrantMapFunction, super().mapping_function)

