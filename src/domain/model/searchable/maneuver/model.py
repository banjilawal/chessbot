# src/domain/model/searchable/model/searchable/maneuver.py

"""
Module: domain.model.searchable.model.maneuver
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from config import NumericSetting
from domain import Path, SearchableModel, Square, Token


class Maneuver(SearchableModel):
    """
    Role:
        - Model
        - Data Holder

    Responsibilities:
        1.  Gives details about a Token's journey along a path.

    Attributes:
        path: Path
        benefit: int
        traveler: Token

    Provides:

    Super Class:
        SearchableModel
    """
    _path: Path
    _benefit: int
    _traveler: Token
    
    def __init__(
            self,
            path: Path,
            traveler: Token,
            benefit: Optional[int] | None = None,
    ):
        """
        Args:
            path: Path
            traveler: Token
            benefit: Optional[int]
        """
        self._path = path
        self._traveler = traveler
        self._benefit = benefit or NumericSetting.negative_infinity()
    
    @property
    def traveler(self) -> Token:
        return self._traveler
    
    @property
    def path(self) -> Path:
        return self._path
    
    @property
    def origin(self) -> Square:
        return self._path.endpoints.origin
    
    @property
    def destination(self) -> Square:
        return self._path.endpoints.destination
        
        
    
    @property
    def benefit(self) -> int:
        return self._benefit
    
    def __eq__(self, other):
        if other == self: return True
        if other is None: return False
        if isinstance(other, Maneuver):
            return self._traveler == other.traveler and self._path == other.path
        return False
        
    