# src/logic/token/service/operation/check/check.py

"""
Module: logic.token.service.operation.check.report
Author: Banji Lawal
Created: 2026-03-19
version: 1.0.0
"""

from __future__ import annotations

from logic.square import Square
from logic.token import KingToken


class CheckSquare:
    """
    Role:
        -   Reporter
        -   Messaging
        -   Data holder
        
    Responsibilities:
        1.  Record that a king will be placed in check from the
            direction of the attacking square.

    Attributes:
        king: KingToken
        square: Square
        attack_square: Square

    Provides:
    Super Class:
    """
    _id: int
    _king: KingToken
    _square: Square
    _attack_source: Square
    
    def __init__(
            self,
            id: int,
            king: KingToken,
            checked_square: Square,
            attack_source: Square,
    ):
        self._id = id
        self._king = king
        self._square = checked_square
        self._attack_source = attack_source
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def king(self) -> KingToken:
        return self._king
    
    @property
    def checked_square(self) -> Square:
        return self._square
    
    @property
    def attack_source(self) -> Square:
        return self._attack_source
    
    def __eq__(self, other):
        if other == self: return True
        if other is None: return False
        if isinstance(other, CheckSquare):
            return (
                    other.king == self.king and
                    other.attack_source == self._attack_source and
                    other.checked_square == self._square
            )
        return False
    
    
    