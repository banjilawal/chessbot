# src/spec/sequencevector/axis/east/spec.py

"""
Module: spec.sequence.vector.axis.east.spec
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from mapping import EastAxisMapFunction
from space import EastAxis
from specification import AxialVectorSequenceSpec


class EastAxisVectorSpec(AxialVectorSequenceSpec[EastAxis]):
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
        AxialVectorSequenceSpec
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

