# src/recurrence/axis/east/recurrence.py

"""
Module: recurrence.axis.east.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from mapping import EastAxisMapFunction
from recurrence import AxisRecurrence
from space import EastAxis



class EastAxisRecurrence(AxisRecurrence[EastAxis]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next EastAxis vector.

    Attributes:
        space: EastAxis
        mapping_function: Optional[EastAxisMapFunction]

    Provides:

    Super Class:
        AxisRecurrence
    """
    
    def __init__(
            self,
            space: EastAxis,
            space_mapping_function: Optional[EastAxisMapFunction] | None = EastAxisMapFunction()
    ):
        """
        Args:
            space: EastAxis
            space_mapping_function: Optional[EastAxisMapFunction]
        """
        super().__init__(space=space, space_mapping_function=space_mapping_function)
        
    @property
    def space(self) -> EastAxis:
        return cast(EastAxis, super().space)
    
    @property
    def mapping_function(self) -> EastAxisMapFunction:
        return cast(EastAxisMapFunction, super().space_mapping_function)

