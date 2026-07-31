# src/geometry/recurrence/quadrant/northeast/recurrence.py

"""
Module: geometry.recurrence.quadrant.northeast.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from geometry.mapper import NortheastQuadrantMapFunction
from geometry.recurrence import QuadrantRecurrence
from geometry.space import NortheastQuadrant



class NortheastQuadrantRecurrence(QuadrantRecurrence[NortheastQuadrant]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next NortheastQuadrant vector.

    Attributes:
        space: NortheastQuadrant,
        space_mapping_function: Optional[NortheastMapFunction]

    Provides:

    Super Class:
        QuadrantRecurrence
    """
    
    def __init__(
            self,
            space: NortheastQuadrant,
            space_mapping_function: Optional[NortheastQuadrantMapFunction] | None = NortheastQuadrantMapFunction()
    ):
        """
        Args:
            space: NortheastQuadrant,
            space_mapping_function: Optional[NortheastMapFunction]
        """
        super().__init__(space=space, space_mapping_function=space_mapping_function)
        
    @property
    def space(self) -> NortheastQuadrant:
        return cast(NortheastQuadrant, super().space)
    
    @property
    def space_mapping_function(self) -> NortheastQuadrantMapFunction:
        return cast(
            NortheastQuadrantMapFunction,
            super().space_mapping_function
        )

