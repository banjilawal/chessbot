# src/assurance/validator/model/attack/common/safe/table.py

"""
Module: assurance.validator.model.attack.common.table.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from domain import AttackPrimeExtract, Maneuver, Token


class SafeSuperAttackPropertyTable:
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores Attack super class properties that are safe.

    Attributes:
        id: int
        victim: Token
        attacker: Token
        maneuver: Maneuver
        attacker_reward: int

    Provides:

    Super Class:
    """
    _id: int
    _victim: Token
    _attacker: Token
    _maneuver: Maneuver
    _attacker_reward: int

    def __init__(
            self,
            id: int,
            victim: Token,
            attacker: Token,
            maneuver: Maneuver,
            attacker_reward: Optional[int] | None = None,
    ):
        """
            id: int,
            victim: Token,
            attacker: Token,
            maneuver: Maneuver,
            prime_extract: AttackPrimeExtract
            attacker_reward: Optional[int]
        """
        self._id = id
        self._victim = victim
        self._attacker = attacker
        self._maneuver = maneuver
        self._attacker_reward = attacker_reward or victim.rank.ransom
        self._prime_extract = prime_extract
    
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def victim(self) -> Token:
        return self._victim
    
    @property
    def attacker(self) -> Token:
        return self._attacker
    
    @property
    def maneuver(self) -> Maneuver:
        return self._maneuver
    
    @property
    def attacker_reward(self) -> int:
        return self._attacker_reward
        self._prime_extract = prime_extract
    
    @property
    def prime_extract(self) -> AttackPrimeExtract:
        return self._prime_extract


