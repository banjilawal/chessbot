# src/topology/recurrence/quadrant/recurrence.py

"""
Module: topology.recurrence.quadrant.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Generic, TypeVar, cast

from topology.mapper import QuadrantMappingFunction
from topology.recurrence import Recurrence

T = TypeVar("T", bound="Quadrant")


class QuadrantRecurrence(Recurrence, Generic[T]):
    """
    Role:
        - Computation
        -  Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next QuadrantSpace vector

    Attributes:
        space: T
        space_mapping_function: QuadrantMappingFunction[T]

    Provides:

    Super Class:
        Recurrence
    """
    
    def __init__(self, space: T, space_mapping_function: QuadrantMappingFunction[T]):
        """
        Args:
            space: T
            space_mapping_function: QuadrantMappingFunction[T]
        """
        super().__init__(space=space, space_mapping_function=space_mapping_function)
        
    @property
    def space(self) -> T:
        return cast(T, super().space)
    
    @property
    def space_mapping_function(self) -> QuadrantMappingFunction[T]:
        return cast(
            QuadrantMappingFunction[T],
            super().space_mapping_function
        )
