# src/space/destination/space.py

"""
Module: space.destination.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from container import VectorSet
from model import Vector


class DestinationVectorSet:
    """
    Role:
        -   Data Holder
        
    Responsibilities:
        1.  Stores vectors that can be journeyed to from the root.

    Attributes:
        root: Vector
        destinations: VectorSet

    Provides:

    Super Class:
    """
    _root: Vector
    _destinations: VectorSet
    
    def __init__(
            self,
            root: Vector,
            destinations: Optional[VectorSet] | None = None,
    ):
        """
        Args:
            root: Vector
            destinations: Optional[VectorSet]
        """
        self._root = root
        self._destinations = destinations or VectorSet()
        
    @property
    def root(self) -> Vector:
        return self._root
    
    @property
    def destinations(self) -> VectorSet:
        return self.destinations
    
    @property
    def has_root_in_destinations(self) -> bool:
        return self._root in self._destinations
    
    @property
    def root_is_not_destination(self) -> bool:
        return not self.has_root_in_destinations
    
    @property
    def destination_count(self) -> int:
        return self._destinations.size
    
    @property
    def destinations_are_null(self) -> bool:
        return self._destinations is None
    
    @property
    def has_destinations(self) -> bool:
        return self._destinations.is_not_empty
    
    @property
    def has_no_destinations(self) -> bool:
        return not self.has_destinations
    
    def remove_root_from_destinations(self) -> DestinationVectorSet:
        if self.root_is_not_destination:
            return self
        temp = []
        for destination in self._destinations.to_list:
            if destination != self.root:
                temp.append(destination)
        return DestinationVectorSet(
            root=self._root,
            destinations=VectorSet(tuple(temp))
        )
        
