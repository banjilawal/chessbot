# src/math/sequence/specification/math.py

"""
Module: math.sequence.specification.math
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from mapping import SpaceMappingFunction
from space import Space


T = TypeVar("T", bound="Space")

class VectorSequenceSpecification(ABC, Generic[T]):
    _space: Space
    _mapping_function: SpaceMappingFunction
    
    def __init__(self, space: Space, mapping_function: SpaceMappingFunction):
        self._space = space
        self._mapping_function = mapping_function
        
    @property
    def space(self) -> T:
        return self._space
    
    @property
    def mapping_function(self) -> SpaceMappingFunction[T]:
        return self._mapping_function
