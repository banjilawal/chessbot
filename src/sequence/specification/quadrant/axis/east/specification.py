# src/sequence/specification/vector/axis/east/specification.py

"""
Module: sequence.specification.vector.axis.east.specification
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from mapping import EastAxisMapFunction
from sequence import QuadrantVectorSequenceSpec
from space import EastAxis


class EastAxisVectorSequenceSpec(QuadrantVectorSequenceSpec[EastAxis]):
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
        QuadrantVectorSequenceSpec
    """
    
    def __init__(
            self,
            space: EastAxis,
            mapping_function: Optional[EastAxisMapFunction] | None = EastAxisMapFunction()
    ):
        """
        Args:
            space: EastAxis
            mapping_function: Optional[EastAxisMapFunction]
        """
        super().__init__(space=space, mapping_function=mapping_function)
        
    @property
    def space(self) -> EastAxis:
        return cast(EastAxis, super().space)
    
    @property
    def mapping_function(self) -> EastAxisMapFunction:
        return cast(EastAxisMapFunction, super().mapping_function)

