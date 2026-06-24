# src/event/check/event.py

"""
Module: event.check.event
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from event import Event
from model import KingToken, Square, Token


class KingCheckEvent(Event):
    """
    Role:
        -   Reporter
        -   Messaging
        -   Data-Holder
        
    Responsibilities:
        1.  Provide information about a check an enemy issued to a king.

    Attributes:
        id: int
        issuer: Token
        issued_from: Square
        for_location: Square
        recipient_king: KingToken

    Provides:
    
    Super Class:
        Event
    """
    _issuer: Token
    _issued_from: Square
    _for_location: Square
    _recipient_king: KingToken
    _parent: Optional[Event] = None
    
    def __init__(
            self,
            id: int,
            issuer: Token,
            issued_from: Square,
            for_location: Square,
            recipient_king: KingToken,
            parent: Optional[Event] | None = None,
    ):
        super().__init__(id=id, parent=parent)
        self._issuer = issuer
        self._issued_from = issued_from
        self._for_location = for_location
        self._recipient_king = recipient_king
        
    @property
    def issuer(self) -> Token:
        return self._issuer
    
    @property
    def issued_from(self) -> Square:
        return self._issued_from
    
    @property
    def for_location(self) -> Square:
        return self._for_location
    
    @property
    def recipient_king(self) -> KingToken:
        return self._recipient_king
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, KingCheckEvent):
            return (
                super().__eq__(other) and
                self._issuer == other.issuer and
                self._issued_from == other.issued_from and
                self._for_location == other.for_location and
                self._recipient_king == other.recipient_king
            )
        return False
    
    