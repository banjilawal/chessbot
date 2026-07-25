# src/spec/sequence/vector/axis/spec.py

"""
Module: spec.sequence.vector.axis.specification
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from typing import Generic, TypeVar, cast

from mapping import AxisMapFunction
from sequence import VectorSequenceSpec

T = TypeVar("T", bound="Axis")


class AxisVectorSequenceSpec(VectorSequenceSpec, Generic[T]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next AxisSpace vector

    Attributes:
        space: T
        mapping_function: AxisMapFunction[T]

    Provides:

    Super Class:
        VectorSequenceSpec
    """
    
    def __init__(self, space: T, mapping_function: AxisMapFunction[T]):
        super().__init__(space=space, mapping_function=mapping_function)
        
    @property
    def space(self) -> T:
        return cast(T, super().space)
    
    @property
    def mapping_function(self) -> AxisMapFunction[T]:
        return cast(AxisMapFunction[T], super().mapping_function)
