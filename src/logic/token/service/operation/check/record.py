# src/logic/token/service/operation/check/record.py

"""
Module: logic.token.service.operation.check.record
Author: Banji Lawal
Created: 2026-03-19
version: 1.0.0
"""

from __future__ import annotations

from logic.square import Square
from logic.token import KingToken, Token


class KingCheckRecord:
    """
    Role:
        -   Reporter
        -   Messaging
        -   Data-Holder
        
    Responsibilities:
        1.  Record details about a check issued to a king.

    Attributes:
        id: int
        issuer: Token
        for_location: Square
        recipient_king: KingToken

    Provides:
    Super Class:
    """
    _id: int
    _issuer: Token
    _for_location: Square
    _recipient_king: KingToken
    
    def __init__(
            self,
            id: int,
            issuer: Token,
            for_location: Square,
            recipient_king: KingToken,
    ):
        """
        Args:
            id: int
            issuer: Token
            for_location: Square
            recipient_king: KingToken
        """
        self._id = id
        self._issuer = issuer
        self._for_location = for_location
        self._recipient_king = recipient_king
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def issuer(self) -> Token:
        return self._issuer
    
    @property
    def for_location(self) -> Square:
        return self._for_location
    
    @property
    def recipient_king(self) -> KingToken:
        return self._recipient_king
    
    def __eq__(self, other):
        if other == self: return True
        if other is None: return False
        if isinstance(other, KingCheckRecord):
            return (
                    other.recipient_king == self.recipient_king and
                    other.for_location == self._for_location and
                    other.issuer == self._issuer
            )
        return False
    
    
    