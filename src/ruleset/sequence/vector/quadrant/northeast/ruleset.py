# src/ruleset/ruleset/vector/quadrant/northeast/ruleset.py

"""
Module: ruleset.sequence.vector.quadrant.northeast.ruleset
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from mapping import NortheastQuadrantMapFunction
from ruleset import QuadrantVectorSpec
from space import NortheastQuadrant


class NortheastQuadrantVectorSpec(QuadrantVectorSpec[NortheastQuadrant]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next NortheastQuadrant vector.

    Attributes:
        space: NortheastQuadrant
        mapping_function: Optional[NortheastQuadrantMapFunction]

    Provides:

    Super Class:
        QuadrantVectorSpec
    """
    
    def __init__(
            self,
            space: NortheastQuadrant,
            mapping_function: Optional[NortheastQuadrantMapFunction] | None = NortheastQuadrantMapFunction()
    ):
        """
        Args:
            space: NortheastQuadrant
            mapping_function: Optional[NortheastQuadrantMapFunction]
        """
        super().__init__(space=space, mapping_function=mapping_function)
        
    @property
    def space(self) -> NortheastQuadrant:
        return cast(NortheastQuadrant, super().space)
    
    @property
    def mapping_function(self) -> NortheastQuadrantMapFunction:
        return cast(NortheastQuadrantMapFunction, super().mapping_function)

