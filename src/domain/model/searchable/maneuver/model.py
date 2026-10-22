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
from domain import Attackable, Path, SearchableModel, Square, Token


class Maneuver(SearchableModel, Attackable):
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
    
    @property
    def is_attack_maneuver(self) -> bool:
        if self.is_not_consistent:
            return False
        destination_occupant = self.destination.occupant
        if (
                destination_occupant is None or
                self._traveler.is_friend(destination_occupant)
        ):
            return False
        return self._traveler.is_enemy(destination_occupant)
    
    @property
    def is_blocked_maneuver(self) -> bool:
        if self.is_not_consistent:
            return False
        destination_occupant = self.destination.occupant
        if (
                destination_occupant is None or
                self._traveler.is_enemy(destination_occupant)
        ):
            return False
        return self._traveler.is_friend(destination_occupant)
    
    @property
    def consistency_exists(self) -> bool:
        return (
            self._path.endpoints.consistency_exists and
            self.origin_is_consistent and
            self.destination_is_consistent
        )
    
    @property
    def is_not_consistent(self) -> bool:
        return not self.consistency_exists
    
    @property
    def origin_is_consistent(self) -> bool:
        if self.origin.is_not_consistent:
            return False
        if (
            self.origin.occupant != self._traveler or
            self.origin.coord != self._traveler.footstep.position
        ):
            return False
        return self.origin.occupant == self._traveler
    
    @property
    def origin_not_consistent(self):
        return not self.origin_is_consistent
    
    @property
    def destination_is_consistent(self) -> bool:
        if (
                self.destination.is_not_consistent or
                self.destination.coord in self._traveler.footstep.to_list
        ):
            return False
        return self.destination.occupant != self._traveler
    
    @property
    def destination_not_consistent(self) -> bool:
        return not self.destination_is_consistent
    
    def __eq__(self, other):
        if other == self: return True
        if other is None: return False
        if isinstance(other, Maneuver):
            return self._traveler == other.traveler and self._path == other.path
        return False
        
    