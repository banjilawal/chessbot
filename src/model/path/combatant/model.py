# src/model/path/model/combatant.py

"""
Module: model.path.model.combatant
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from model import CombatantToken, Path, Square


@dataclass
class CombatantPath(Path):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the origin and destination squares a token wants to travel between.

    Attributes:
        id: int
        combatant: combatantToken
        origin: Square
        destination: Square

    Provides:

    Super Class:
        Path
    """
    _combatant: CombatantToken
    
    def __init__(
            self,
            id: int,
            combatant: CombatantToken,
            origin: Square,
            destination: Square,
            cost: Optional[int] | None,
    ):
        super().__init__(
            id=id,
            origin=origin,
            destination=destination,
            cost=cost,
        )
        self._combatant = combatant
        
    @property
    def combatant(self) -> CombatantToken:
        return self._combatant
    
    def __eq__(self, other):
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, CombatantPath):
            return super.__eq__(other) and self.combatant == other.combatant
        return False
    
    def __hash__(self):
        return super.__hash__(self)
        
        
        
    