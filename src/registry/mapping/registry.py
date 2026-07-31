# src/mapping/stream/mapper.py

"""
Module: mapping.stream.mapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, Type, TypeVar

from geometry.mapper import SpaceMappingFunction

T = TypeVar("T", bound="SpaceReservoir")

class SpaceMapFunctionStream(ABC, Generic[T]):
    """
    Role:
        -   Data Holder
        -   Factory
        -   Switcher

    Responsibilities:
        1.  Produce the set of all mapping functions for with the correct downcast.
        2.  Dictionary for iterating through mapping functions by type.
        

    Attributes:
        space_reservoir: T

    Provides:
        -   @abstractmethod def stream_size() -> in
        -   @abstractmethod def streams_are_empty() -> bool
        -   @abstractmethod def streams_are_not_empty() -> bool
        -   @abstractmethod def type_mapper_dict() -> Dict[Type[T], SpaceMappingFunction[T]]

    Super Class:
    """
    _space_reservoir: T
    
    def __init__(self, space_reservoir: T):
        """
        Args:
            space_reservoir: T
        """
        self._space_reservoir = space_reservoir
    
    @property
    def space_reservoir(self) -> T:
        return self._space_reservoir
    
    @property
    @abstractmethod
    def stream_size(self) -> int:
        pass
    
    @property
    @abstractmethod
    def streams_are_empty(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def streams_are_not_empty(self) -> bool:
        pass

    @property
    @abstractmethod
    def type_mapper_dict(self) -> Dict[Type[T], SpaceMappingFunction[T]]:
        pass
