# src/topology/recurrence/quadrant/southwest/recurrence.py

"""
Module: topology.recurrence.quadrant.southwest.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from mapping import SouthwestMapFunction
from topology.recurrence import QuadrantRecurrence
from topology.space import SouthwestQuadrant


class SouthwestQuadrantRecurrence(QuadrantRecurrence[SouthwestQuadrant]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next SouthwestQuadrant vector.

    Attributes:
        space: SouthwestQuadrant
        space_mapping_function: Optional[SouthwestMapFunction]

    Provides:

    Super Class:
        QuadrantRecurrence
    """
    
    def __init__(
            self,
            space: SouthwestQuadrant,
            space_mapping_function: Optional[SouthwestMapFunction] | None = SouthwestMapFunction()
    ):
        """
        Args:
            space: SouthwestQuadrant
            space_mapping_function: Optional[SouthwestMapFunction]
        """
        super().__init__(space=space, space_mapping_function=space_mapping_function)
        
    @property
    def space(self) -> SouthwestQuadrant:
        return cast(SouthwestQuadrant, super().space)
    
    @property
    def space_mapping_function(self) -> SouthwestMapFunction:
        return cast(SouthwestMapFunction, super().space_mapping_function)

