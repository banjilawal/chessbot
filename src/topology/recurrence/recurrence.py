# src/topology/recurrence/recurrence.py

"""
Module: topology.recurrence.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from topology import SpaceMappingFunction

T = TypeVar("T", bound="Space")

class Recurrence(ABC, Generic[T]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next Vector in a Space.

    Attributes:
        space: T
        space_mapping_function: SpaceMappingFunction[T]
        
    Provides:

    Super Class:
    """
    _space: T
    _space_mapping_function: SpaceMappingFunction[T]
    
    def __init__(self, space: T, space_mapping_function: SpaceMappingFunction[T],):
        """
        Args:
            space: T
            space_mapping_function: SpaceMappingFunction[T]
        """
        self._space = space
        self._space_mapping_function = space_mapping_function
        
    @property
    def space(self) -> T:
        return self._space
    
    @property
    def space_mapping_function(self) -> SpaceMappingFunction[T]:
        return self._space_mapping_function
