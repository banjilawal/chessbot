# src/recurrence/axis/recurrence.py

"""
Module: recurrence.axis.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from typing import Generic, TypeVar, cast

from mapper import AxisMappingFunction
from recurrence import Recurrence

T = TypeVar("T", bound="Axis")


class AxisRecurrence(Recurrence, Generic[T]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next AxisSpace vector

    Attributes:
        space: T
        space_mapping_function: AxisMappingFunction[T]

    Provides:

    Super Class:
        Recurrence
    """
    
    def __init__(
            self, space: T, space_mapping_function: AxisMappingFunction[T],
    ):
        """
        Args:
            space: T
            space_mapping_function: AxisMappingFunction[T]
        """
        super().__init__(
            space=space,
            space_mapping_function=space_mapping_function
        )
        
    @property
    def space(self) -> T:
        return cast(T, super().space)
    
    @property
    def space_mapping_function(self) -> AxisMappingFunction[T]:
        return cast(
            AxisMappingFunction[T],
            super().space_mapping_function
        )
