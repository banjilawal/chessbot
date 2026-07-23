# src/ruleset/sequence/vector/spec.py

"""
Module: ruleset.sequence.vector.sequence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar

from mapping import SpaceMappingFunction


T = TypeVar("T", bound="Space")

class VectorSequenceSpec(SequenceSpec, Generic[T]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating to the next Vector in a Space..

    Attributes:
        space: T
        mapping_function: SpaceMappingFunction[T]
        
    Provides:

    Super Class:
        SequenceSpec
    """
    
    _space: T
    _mapping_function: SpaceMappingFunction[T]
    
    def __init__(self, space: T, mapping_function: SpaceMappingFunction[T],):
        """
        Args:
            space: T
            mapping_function: SpaceMappingFunction[T]
        """
        self._space = space
        self._mapping_function = mapping_function
        
    @property
    def space(self) -> T:
        return self._space
    
    @property
    def mapping_function(self) -> SpaceMappingFunction[T]:
        return self._mapping_function
