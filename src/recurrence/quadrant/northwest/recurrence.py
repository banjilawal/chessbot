# src/recurrence/quadrant/northwest/recurrence.py

"""
Module: recurrence.quadrant.northwest.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from mapper import NorthwestMapFunction
from recurrence import QuadrantRecurrence
from space import NorthwestQuadrant



class NorthwestQuadrantRecurrence(QuadrantRecurrence[NorthwestQuadrant]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next NorthwestQuadrant vector.

    Attributes:
        space: NorthwestQuadrant,
        space_mapping_function: Optional[NorthwestMapFunction]

    Provides:

    Super Class:
        QuadrantRecurrence
    """
    
    def __init__(
            self,
            space: NorthwestQuadrant,
            space_mapping_function: Optional[NorthwestMapFunction] | None = NorthwestMapFunction()
    ):
        """
        Args:
            space: NorthwestQuadrant,
            space_mapping_function: Optional[NorthwestMapFunction]
        """
        super().__init__(space=space, space_mapping_function=space_mapping_function)
        
    @property
    def space(self) -> NorthwestQuadrant:
        return cast(NorthwestQuadrant, super().space)
    
    @property
    def space_mapping_function(self) -> NorthwestMapFunction:
        return cast(
            NorthwestMapFunction,
            super().space_mapping_function
        )

