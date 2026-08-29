# src/domain/model/searchable/walk/model/searchable/maneuver.py

"""
Module: domain.model.searchable.walk.model.maneuver
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from domain import Attack, Path, SearchableModel, Token


class Maneuver(SearchableModel):
    """
    Role:
        - Model
        -  Data Holder

    Responsibilities:
        1.  Gives details about a Token's journey along a path.

    Attributes:
        path: Path
        benefit: int
        traveller: Token
        attack: Optional[Attack]

    Provides:

    Super Class:
        SearchableModel
    """
    _path: Path
    _benefit: int
    _traveller: Token
    _attack: Optional[Attack]

    
    def __init__(
            self,
            path: Path,
            traveller: Token,
            benefit: Optional[int] | None = 0,
            attack: Optional[Attack] | None = None,
    ):
        """
        Args:
            path: Path
            traveller: Token
        """
        self._path = path
        self._benefit = benefit
        self._traveller = traveller
        self._attack = attack

    
    @property
    def traveller(self) -> Token:
        return self._traveller
    
    @property
    def path(self) -> Path:
        return self._path
    
    @property
    def benefit(self) -> int:
        return self._benefit
        
    @property
    def attack(self) -> Optional[Attack]:
        return self._attack
    
    def __eq__(self, other):
        if other == self: return True
        if other is None: return False
        if isinstance(other, Maneuver):
            return self._traveller == other.traveller and self._path == other.path
        return False
        
    