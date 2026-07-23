# src/ruleset/ruleset/vector/quadrant/northwestwest/ruleset.py

"""
Module: ruleset.sequence.vector.quadrant.northwest.ruleset
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast


from ruleset import QuadrantVectorSpec

from space import NorthwestQuadrant


class NorthwestQuadrantVectorSpec(QuadrantVectorSpec[NorthwestQuadrant]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next NorthwestQuadrant vector.

    Attributes:
        space: NorthwestQuadrant
        mapping_function: Optional[NorthwestQuadrantMapFunction]

    Provides:

    Super Class:
        QuadrantVectorSpec
    """
    
    def __init__(
            self,
            space: NorthwestQuadrant,
            mapping_function: Optional[NorthwestQuadrantMapFunction] | None = NorthwestQuadrantMapFunction()
    ):
        """
        Args:
            space: NorthwestQuadrant
            mapping_function: Optional[NorthwestQuadrantMapFunction]
        """
        super().__init__(space=space, mapping_function=mapping_function)
        
    @property
    def space(self) -> NorthwestQuadrant:
        return cast(NorthwestQuadrant, super().space)
    
    @property
    def mapping_function(self) -> NorthwestQuadrantMapFunction:
        return cast(NorthwestQuadrantMapFunction, super().mapping_function)

