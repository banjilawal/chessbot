# src/spec/sequencevector/quadrant/spec.py

"""
Module: spec.sequence.vector.quadrant.spec
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from typing import Generic, TypeVar, cast

from mapping import SpaceMappingFunction
from specification import VectorSequenceSpec

T = TypeVar("T", bound="QuadrantSpace")


class QuadrantVectorSpec(VectorSequenceSpec, Generic[T]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next QuadrantSpace vector

    Attributes:
        space: T
        mapping_function: SpaceMappingFunction[T]

    Provides:

    Super Class:
        VectorSequenceSpec
    """
    
    def __init__(self, space: T, mapping_function: SpaceMappingFunction[T]):
        super().__init__(space=space, mapping_function=mapping_function)
        
    @property
    def space(self) -> T:
        return cast(T, super().space)
    
    @property
    def mapping_function(self) -> SpaceMappingFunction[T]:
        return cast(SpaceMappingFunction[T], super().mapping_function)
