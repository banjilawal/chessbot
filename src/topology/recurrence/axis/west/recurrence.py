# src/topology/recurrence/axis/west/recurrence.py

"""
Module: topology.recurrence.axis.west.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from topology.mapper import WestAxisMapFunction
from topology.recurrence import AxisRecurrence
from topology.space import WestAxis



class WestAxisRecurrence(AxisRecurrence[WestAxis]):
    """
    Role:
        -  Computation
        -  Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next WestAxis vector.

    Attributes:
        space: WestAxis
        mapping_function: Optional[WestAxisMapFunction]

    Provides:

    Super Class:
        AxisRecurrence
    """
    
    def __init__(
            self,
            space: WestAxis,
            space_mapping_function: Optional[WestAxisMapFunction] | None = WestAxisMapFunction()
    ):
        """
        Args:
            space: WestAxis
            space_mapping_function: Optional[WestAxisMapFunction]
        """
        super().__init__(space=space, space_mapping_function=space_mapping_function)
        
    @property
    def space(self) -> WestAxis:
        return cast(WestAxis, super().space)
    
    @property
    def space_mapping_function(self) -> WestAxisMapFunction:
        return cast(WestAxisMapFunction, super().space_mapping_function)

