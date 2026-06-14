# src/event/attack/event.py

"""
Module: event.attack.event
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from event import Event
from model import CombatantToken, Square, Token


@dataclass
class AttackEvent(Event):
    attack_origin: Square
    attacker: Token
    target_square: Square
    enemy_combatant: CombatantToken
    child: Optional[Event] | None = None
    