# src/recurrence/quadrant/recurrence.py

"""
Module: recurrence.quadrant.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from typing import Generic, TypeVar, cast

from mapping import SpaceMappingFunction
from recurrence import Recurrence

T = TypeVar("T", bound="QuadrantSpace")


class QuadrantRecurrence(Recurrence, Generic[T]):
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
        VectorSequenceRecurrence
    """
    
    def __init__(self, space: T, space_mapping_function: SpaceMappingFunction[T]):
        super().__init__(space=space, space_mapping_function=space_mapping_function)
        
    @property
    def space(self) -> T:
        return cast(T, super().space)
    
    @property
    def space_mapping_function(self) -> SpaceMappingFunction[T]:
        return cast(SpaceMappingFunction[T], super().space_mapping_function)
