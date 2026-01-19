# src/chess/hostage/manifest.py

"""
Module: chess.hostage.manifest
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.square import Square
from chess.token import CombatantToken, Token


class HostageManifest:
    _id: int
    _victor: Token
    _prisoner: CombatantToken
    _capture_location: Square
    
    def __init__(self, id: int, victor: Token, prisoner: CombatantToken, capture_location: Square):
        self._id = id
        self._victor = victor
        self._prisoner = prisoner
        self._capture_location = capture_location
        
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
    def capture_location(self) -> Square:
        return self._capture_location
        
    