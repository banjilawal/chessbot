# src/sequence/specification/vector/axis/west/specification.py

"""
Module: sequence.specification.vector.axis.west.specification
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from mapping import WestAxisMapFunction
from sequence import QuadrantVectorSequenceSpec
from space import WestAxis


class WestAxisVectorSequenceSpec(QuadrantVectorSequenceSpec[WestAxis]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next WestAxis vector.

    Attributes:
        space: WestAxis
        mapping_function: Optional[WestAxisMapFunction]

    Provides:

    Super Class:
        QuadrantVectorSequenceSpec
    """
    
    def __init__(
            self,
            space: WestAxis,
            mapping_function: Optional[WestAxisMapFunction] | None = WestAxisMapFunction()
    ):
        """
        Args:
            space: WestAxis
            mapping_function: Optional[WestAxisMapFunction]
        """
        super().__init__(space=space, mapping_function=mapping_function)
        
    @property
    def space(self) -> WestAxis:
        return cast(WestAxis, super().space)
    
    @property
    def mapping_function(self) -> WestAxisMapFunction:
        return cast(WestAxisMapFunction, super().mapping_function)

