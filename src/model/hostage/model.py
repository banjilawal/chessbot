# src/model/hostage/model.py

"""
Module: model.hostage.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from model.square import Square
from model.token import CombatantToken, Token


@dataclass
class Hostage:
    _victor: Token
    _prisoner: CombatantToken
    _captured_square: Square
    
    def __init__(
            self,
            id: int,
            victor: Token,
            prisoner: CombatantToken,
            captured_square: Square,
    ):
        self._id = id
        self._victor = victor
        self._prisoner = prisoner
        self._captured_square = captured_square
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def victor(self) -> Token:
        return self._victor
    
    @property
    def prisoner(self) -> CombatantToken:
        return self._prisoner
    
    @property
    def captured_square(self) -> Square:
        return self._captured_square
        
    