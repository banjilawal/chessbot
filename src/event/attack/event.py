# src/event/attack/event.py

"""
Module: event.attack.event
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

from event import Event
from model import CombatantToken, Square, Token



class AttackEvent(Event):
    _attacker: Token
    _attack_origin: Square
    _target_square: Square
    _enemy_combatant: CombatantToken
    
    def __init__(
            self,
            id: int,
            attacker: Token,
            attack_origin: Square,
            target_square: Square,
            enemy_combatant: CombatantToken,
            parent: Optional[Event] | None = None,
    ):
        super().__init__(id=id, parent=parent)
        self._attacker = attacker
        self._attack_origin = attack_origin
        self._target_square = target_square
        self._enemy_combatant = enemy_combatant
        
    @property
    def attacker(self) -> Token:
        return self._attacker
    
    @property
    def attack_origin(self) -> Square:
        return self._attack_origin
    
    @property
    def target_square(self) -> Square:
        return self._target_square
    
    @property
    def enemy_combatant(self) -> CombatantToken:
        return self._enemy_combatant
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, AttackEvent):
            return (
                    super().__eq__(other) and
                    self._attacker == other.attacker and
                    self._attack_origin == other.attack_origin and
                    self._target_square == other.target_square and
                    self._enemy_combatant == other.enemy_combatant
            )
        return False