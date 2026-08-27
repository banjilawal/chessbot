# src/topology/recurrence/quadrant/southeast/recurrence.py

"""
Module: topology.recurrence.quadrant.southeast.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from mapping import SoutheastMapFunction
from topology.recurrence import QuadrantRecurrence
from topology.space import SoutheastQuadrant



class SoutheastQuadrantRecurrence(QuadrantRecurrence[SoutheastQuadrant]):
    """
    Role:
        - Computation
        -  Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next SoutheastQuadrant vector.

    Attributes:
        space: SoutheastQuadrant
        mapping_function: Optional[SoutheastMapFunction]

    Provides:

    Super Class:
        QuadrantRecurrence
    """
    
    def __init__(
            self,
            space: SoutheastQuadrant,
            space_mapping_function: Optional[SoutheastMapFunction] | None = SoutheastMapFunction()
    ):
        """
        Args:
            space: SoutheastQuadrant
            space_mapping_function: Optional[SoutheastMapFunction]
        """
        super().__init__(space=space, space_mapping_function=space_mapping_function)
        
    @property
    def space(self) -> SoutheastQuadrant:
        return cast(SoutheastQuadrant, super().space)
    
    @property
    def space_mapping_function(self) -> SoutheastMapFunction:
        return cast(SoutheastMapFunction, super().space_mapping_function)

