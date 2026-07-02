# src/model/path/model/king.py

"""
Module: model.path.model.king
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from model import KingToken, Path, Square


@dataclass
class KingPath(Path):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Provide information about a path a KingToken might follow.

    Attributes:
        id: int
        king: KingToken
        origin: Square
        destination: Square
        cost: Optional[int]

    Provides:

    Super Class:
        Path
    """
    _king: KingToken
    
    def __init__(
            self,
            id: int,
            king: KingToken,
            origin: Square,
            destination: Square,
            cost: Optional[int] | None,
    ):
        """
        Args:
            id: int
            king: KingToken
            origin: Square
            destination: Square
            cost: Optional[int]
        """
        super().__init__(
            id=id,
            origin=origin,
            destination=destination,
            cost=cost,
        )
        self._king = king
        
    @property
    def king(self) -> KingToken:
        return self._king
    
    def __eq__(self, other):
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, KingPath):
            return super.__eq__(other) and self.king == other.king
        return False
    
    def __hash__(self):
        return super.__hash__(self)
        
        
        
    