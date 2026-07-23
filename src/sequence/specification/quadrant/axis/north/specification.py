# src/sequence/specification/vector/axis/north/specification.py

"""
Module: sequence.specification.vector.axis.north.specification
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from mapping import NorthAxisMapFunction
from sequence import QuadrantVectorSequenceSpec
from space import NorthAxis


class NorthAxisVectorSequenceSpec(QuadrantVectorSequenceSpec[NorthAxis]):
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
        QuadrantVectorSequenceSpec
    """
    
    def __init__(
            self,
            space: NorthAxis,
            mapping_function: Optional[NorthAxisMapFunction] | None = NorthAxisMapFunction()
    ):
        """
        Args:
            space: NorthAxis
            mapping_function: Optional[NorthAxisMapFunction]
        """
        super().__init__(space=space, mapping_function=mapping_function)
        
    @property
    def space(self) -> NorthAxis:
        return cast(NorthAxis, super().space)
    
    @property
    def mapping_function(self) -> NorthAxisMapFunction:
        return cast(NorthAxisMapFunction, super().mapping_function)

