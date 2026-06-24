# src/event/attack/event.py

"""
Module: event.attack.event
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional, cast

from event import Event
from model import CombatantToken, Square, Token
from report import AttackApproval


class AttackEvent(Event):
    _attacker: Token
    _location: Square
    _captive: CombatantToken
    
    def __init__(
            self,
            id: int,
            attacker: Token,
            captive: CombatantToken,
            approval: AttackApproval,
            location: Square,
            parent: Optional[Event] | None = None,
    ):
        super().__init__(id=id, parent=parent, approval=approval)
        self._attacker = attacker
        self._location = location
        self._captive = captive
        
    @property
    def approval(self) -> AttackApproval:
        return cast(AttackApproval, self._approval)
        
    @property
    def attacker(self) -> Token:
        return self._attacker
    
    @property
    def location(self) -> Square:
        return self._location
    
    @property
    def captive(self) -> CombatantToken:
        return self._captive
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, AttackEvent):
            return (
                    super().__eq__(other) and
                    self._attacker == other.attacker and
                    self._location == other.location and
                    self._captive == other.captive
            )
        return False
    
    def __hash__(self):
        return super().__hash__(id)