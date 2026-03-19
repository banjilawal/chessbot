# src/logic/token/service/operation/check/check.py

"""
Module: logic.token.service.operation.check.report
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations

from logic.square import Square
from logic.token import KingToken


class Check:
    
    _id: int
    _king: KingToken
    _checked_square: Square
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
        self._checked_square = checked_square
        self._attack_source = attack_source
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def king(self) -> KingToken:
        return self._king
    
    @property
    def checked_square(self) -> Square:
        return self._checked_square
    
    @property
    def attack_source(self) -> Square:
        return self._attack_source
    
    def __eq__(self, other):
        if other == self: return True
        if other is None: return False
        if isinstance(other, Check):
            return (
                    other.king == self.king and
                    other.attack_source == self._attack_source and
                    other.checked_square == self._checked_square
            )
        return False
    
    
    