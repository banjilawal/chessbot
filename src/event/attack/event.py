# src/event/attack/event.py

"""
Module: event.attack.event
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations
from dataclasses import dataclass

from event import Event
from model import CombatantToken, Square, Token


@dataclass
class AttackEvent(Event):
    attack_origin: Square
    attacker: Token
    target_square: Square
    enemy_combatant: CombatantToken
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, AttackEvent):
            return (
                    super().__eq__(other) and
                    self.attacker == other.attacker and
                    self.attack_origin == other.attack_origin and
                    self.target_square == other.target_square and
                    self.enemy_combatant == other.enemy_combatant
            )
        return False
    