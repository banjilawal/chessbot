# src/model/path/model.py

"""
Module: model.path.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model.square import Square


class Path:
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Provide information about path which might be taken during a turn

    Attributes:
        id: int
        origin: Square
        destination: Square
        cost: Optional[int]

    Provides:

    Super Class:
    """
    _id: int
    _origin: Square
    _destination: Square
    _cost: Optional[int]
    
    def __init__(
            self,
            id: int,
            origin: Square,
            destination: Square,
            cost: Optional[int] | None = None,
    ):
        """
        Args:
            id: int
            origin: Square
            destination: Square
            cost: Optional[int]
        """
        self._id = id
        self._origin = origin
        self._destination = destination
        self._cost = cost
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def origin(self) -> Square:
        return self._origin
    
    @property
    def destination(self) -> Square:
        return self._destination
    
    @property
    def cost(self) -> Optional[int]:
        return self._cost
    
    @cost.setter
    def cost(self, cost: Optional[int]):
        self._cost = cost

    def __eq__(self, other):
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, Path):
            return (
                    self.id == other.id and
                    self.cost == other.cost and
                    self.origin == other.origin and
                    self.destination == other.destination
            )
        return False
    
    def __hash__(self):
        return hash(self.id)
        
        
        
    