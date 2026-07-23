# src/spec/sequencevector/axis/west/spec.py

"""
Module: spec.sequence.vector.axis.westt.spec
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from mapping import WestAxisMapFunction
from space import WestAxis
from specification import AxialVectorSequenceSpec


class WestAxisVectorSpec(AxialVectorSequenceSpec[WestAxis]):
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
        AxialVectorSequenceSpec
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

