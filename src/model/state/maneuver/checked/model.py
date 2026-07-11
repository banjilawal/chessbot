# src/model/state/path/model/state/checked.py

"""
Module: model.state.path.model.checked
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model import KingToken, Path, Square, Token


class CheckedManeuver(Maneuver):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Provide information about a check made to a king.

    Attributes:
        id: int
        issuer: Token
        recipient_king: KingToken
        issued_from: Square
        for_location: Square
        cost: Optional[int]

    Provides:

    Super Class:
        Path
    """
    _issuer: Token
    _recipient_king: KingToken
    
    def __init__(
            self,
            id: int,
            issuer: Token,
            recipient_king: KingToken,
            issued_from: Square,
            for_location: Square,
            cost: Optional[int] | None,
    ):
        """
        Args:
            id: int
            issuer: Token
            recipient_king: KingToken
            issued_from: Square
            for_location: Square
            cost: Optional[int]
        """
        super().__init__(
            id=id,
            origin=issued_from,
            destination=for_location,
            cost=cost,
        )
        self._issuer = issuer
        self._recipient_king = recipient_king
        
    @property
    def issuer(self) -> Token:
        return self._issuer
        
    @property
    def recipient_king(self) -> KingToken:
        return self._recipient_king
    
    @property
    def issued_from(self) -> Square:
        return self.origin
    
    @property
    def for_location(self) -> Square:
        return self.destination
    
    def __eq__(self, other):
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, CheckedPath):
            return (
                    super().__eq__(other) and
                    self.issuer == other.issuer and
                    self.recipient_king == other.recipient_king
            )
        return False
    
    def __hash__(self):
        return super.__hash__(self)
        
        
        
    