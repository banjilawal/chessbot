# src/transit/delivery/table.py

"""
Module: transit.delivery.encounter.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import Encounter, EncounterPrimeExtract, Maneuver, Square, TokenChart
from transit import ProductEnvelope


class RootEncounterEnvelope(ProductEnvelope[Encounter]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores Encounter super class properties that are reference.

    Attributes:
        id: int
        location: Square
        attacker_reward: int
        participants: TokenChart
        attacker_maneuver: Maneuver
        prime_extract: EncounterPrimeExtract

    Provides:

    Super Class:
        ProductEnvelopeTable
    """
    _id: int
    _location: Square
    _attacker_reward: int
    _participants: TokenChart
    _attacker_maneuver: Maneuver
    
    def __init__(
            self,
            id: int,
            location: Square,
            attacker_reward: int,
            participants: TokenChart,
            attacker_maneuver: Maneuver,
            prime_extract: EncounterPrimeExtract,
    ):
        """
            id: int
            location: Square
            attacker_reward: int
            participants: TokenChart
            attacker_maneuver: Maneuver
            prime_extract: EncounterPrimeExtract
        """
        super().__init__(prime_extract=prime_extract)
        self._id = id
        self._location = location
        self._attacker_reward = attacker_reward
        self._participants = participants
        self._attacker_maneuver =attacker_maneuver
  
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def location(self) -> Square:
        return self._location
    
    @property
    def participants(self) -> TokenChart:
        return self._participants
    
    @property
    def attacker_reward(self) -> int:
        return self._attacker_reward
    
    @property
    def attacker_maneuver(self) -> Maneuver:
        return self._attacker_maneuver
        
    @property
    def prime_extract(self) -> EncounterPrimeExtract:
        return cast(EncounterPrimeExtract, super().prime_extract)
    

    