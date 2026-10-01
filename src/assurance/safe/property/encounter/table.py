# src/assurance/safe/property/encounter/table.py

"""
Module: assurance.safe.property.encounter.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from assurance import SafePropertyTable
from domain import Encounter, Maneuver, Token


class EncounterSafePropertyTable(SafePropertyTable[Encounter]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores Encounter super class properties that are safe.

    Attributes:
        id: int
        token: Token
        attacker_maneuver: Maneuver
        attacker_reward: int

    Provides:

    Super Class:
        SafeSuperClassPropertyTable
    """
    _id: int
    _victim: Token
    _attacker_maneuver: Maneuver
    _attacker_reward: int
    
    def __init__(
            self,
            id: int,
            victim: Token,
            attacker_maneuver: Maneuver,
            attacker_reward: int,
    ):
        """
            id: int
            token: Token
            attacker_maneuver: Maneuver
            attacker_reward: int
        """
        self._id = id
        self._victim = victim
        self._maneuver = attacker_maneuver
        self._attacker_reward = attacker_reward
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def victim(self) -> Token:
        return self._victim
    
    @property
    def maneuver(self) -> Maneuver:
        return self._maneuver
    
    @property
    def attacker_reward(self) -> int:
        return self._attacker_reward

    