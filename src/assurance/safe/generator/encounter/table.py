# src/assurance/safe/generator/encounter/table.py

"""
Module: assurance.safe.generator.encounter.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from assurance import SafeSuperClassGeneratorTable
from domain import Encounter, Maneuver, Token


class SafeSuperEncounterGeneratorTable(SafeSuperClassGeneratorTable[Encounter]):
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
        SafeSuperClassGeneratorTable
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
        
    @generator
    def id(self) -> int:
        return self._id
    
    @generator
    def victim(self) -> Token:
        return self._victim
    
    @generator
    def maneuver(self) -> Maneuver:
        return self._maneuver
    
    @generator
    def attacker_reward(self) -> int:
        return self._attacker_reward

    