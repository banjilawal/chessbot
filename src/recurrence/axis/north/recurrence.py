# src/recurrence/axis/north/recurrence.py

"""
Module: recurrence.axis.north.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from mapper import NorthAxisMapFunction
from recurrence import AxisRecurrence
from space import NorthAxis



class NorthAxisRecurrence(AxisRecurrence[NorthAxis]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next NorthAxis vector.

    Attributes:
        space: NorthAxis
        mapping_function: Optional[NorthAxisMapFunction]

    Provides:

    Super Class:
        AxisRecurrence
    """
    
    def __init__(
            self,
            space: NorthAxis,
            space_mapping_function: Optional[NorthAxisMapFunction] | None = NorthAxisMapFunction(),
    ):
        """
        Args:
            space: NorthAxis
            space_mapping_function: Optional[NorthAxisMapFunction]
        """
        super().__init__(space=space, space_mapping_function=space_mapping_function)
        
    @property
    def space(self) -> NorthAxis:
        return cast(NorthAxis, super().space)
    
    @property
    def space_mapping_function(self) -> NorthAxisMapFunction:
        return cast(
            NorthAxisMapFunction,
            super().space_mapping_function
        )

