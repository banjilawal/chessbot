# src/topology/recurrence/axis/south/recurrence.py

"""
Module: topology.recurrence.axis.south.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from topology.mapper import SouthAxisMapFunction
from topology.recurrence import AxisRecurrence

from topology.space import SouthAxis



class SouthAxisRecurrence(AxisRecurrence[SouthAxis]):
    """
    Role:
        -  Computation
        -  Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next SouthAxis vector.

    Attributes:
        space: SouthAxis
        mapping_function: Optional[SouthAxisMapFunction]

    Provides:

    Super Class:
        AxisRecurrence
    """
    
    def __init__(
            self,
            space: SouthAxis,
            space_mapping_function: Optional[SouthAxisMapFunction] | None = SouthAxisMapFunction()
    ):
        """
        Args:
            space: SouthAxis
            space_mapping_function: Optional[SouthAxisMapFunction]
        """
        super().__init__(space=space, space_mapping_function=space_mapping_function)
        
    @property
    def space(self) -> SouthAxis:
        return cast(SouthAxis, super().space)
    
    @property
    def space_mapping_function(self) -> SouthAxisMapFunction:
        return cast(
            SouthAxisMapFunction,
            super().space_mapping_function,
        )

