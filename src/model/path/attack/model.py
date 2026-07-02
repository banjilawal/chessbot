# src/model/path/model/attack.py

"""
Module: model.path.model.attack
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model import CombatantToken, Path, Square, Token


class AttackPath(Path):
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
    _attacker: Token
    _enemy_combatant: CombatantToken
    _benefit: Optional[int]
    
    def __init__(
            self,
            id: int,
            attacker: Token,
            enemy_combatant: CombatantToken,
            attack_origin: Square,
            target_square: Square,
            cost: Optional[int] | None,
            benefit: Optional[int] | None,
    ):
        super().__init__(
            id=id,
            origin=attack_origin,
            destination=target_square,
            cost=cost,
        )
        self._attacker = attacker
        self._enemy_combatant = enemy_combatant
        self._benefit = benefit
        
    @property
    def attacker(self) -> Token:
        return self._attacker
        
    @property
    def enemy_combatant(self) -> CombatantToken:
        return self._enemy_combatant
    
    @property
    def attack_origin(self) -> Square:
        return self.origin
    
    @property
    def target_square(self) -> Square:
        return self.destination
    
    @property
    def benefit(self) -> Optional[int]:
        return self._benefit
    
    @benefit.setter
    def benefit(self, benefit: Optional[int]):
        self._benefit = benefit
    
    def __eq__(self, other):
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, AttackPath):
            return (
                    super.__eq__(other) and
                    self.benefit == other.benefit and
                    self.attacker == other.attacker and
                    self.enemy_combatant == other.enemy_combatant
            )
        return False
    
    def __hash__(self):
        return super.__hash__(self)
        
        
        
    