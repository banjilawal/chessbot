# src/event/check/event.py

"""
Module: event.check.event
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from event import Event
from model import KingToken, Square, Token


@dataclass
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
    id: int
    issuer: Token
    issued_from: Square
    for_location: Square
    recipient_king: KingToken
    
    def __eq__(self, other):
        if other == self: return True
        if other is None: return False
        if isinstance(other, KingCheckEvent):
            return (
                    self.issuer == other.issuer and
                    self.for_location == other.for_location and
                    self.recipient_king == self.recipient_king
            )
        return False
    
    
    