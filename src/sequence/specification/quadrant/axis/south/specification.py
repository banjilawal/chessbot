# src/sequence/specification/vector/axis/south/specification.py

"""
Module: sequence.specification.vector.axis.south.specification
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from mapping import SouthAxisMapFunction
from sequence import QuadrantVectorSequenceSpec
from space import SouthAxis


class SouthAxisVectorSequenceSpec(QuadrantVectorSequenceSpec[SouthAxis]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next SouthAxis vector.

    Attributes:
        space: SouthAxis
        mapping_function: Optional[SouthAxisMapFunction]

    Provides:

    Super Class:
        QuadrantVectorSequenceSpec
    """
    
    def __init__(
            self,
            space: SouthAxis,
            mapping_function: Optional[SouthAxisMapFunction] | None = SouthAxisMapFunction()
    ):
        """
        Args:
            space: SouthAxis
            mapping_function: Optional[SouthAxisMapFunction]
        """
        super().__init__(space=space, mapping_function=mapping_function)
        
    @property
    def space(self) -> SouthAxis:
        return cast(SouthAxis, super().space)
    
    @property
    def mapping_function(self) -> SouthAxisMapFunction:
        return cast(SouthAxisMapFunction, super().mapping_function)

