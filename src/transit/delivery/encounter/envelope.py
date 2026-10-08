# src/transit/delivery/encounter/envelope.py

"""
Module: transit.delivery.encounter.envelope
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import Encounter, EncounterPrimeExtract, Maneuver, Square, Participation, Token
from transit import (
    CheckmateEncounterCarrier, EncounterWarningCarrier, KillEncounterCarrier, ProductEnvelope,
    StalemateEncounterCarrier
)


class RootEncounterEnvelope(ProductEnvelope[Encounter]):
    """
    Role
        -   Data Transfer

    Responsibilities:
        1.  Data from a RootEncounterValidator forwarded to client validators.

    Attributes:
        id: int
        victim: Token
        location: Square
        attacker_reward: int
        attacker_maneuver: Maneuver
        prime_extract: EncounterPrimeExtract

    Provides:
        for_kill_encounter_consumer: bool
        for_checkmate_encounter_consumer: bool
        for_encounter_warning_consumer: bool
        for_stalemate_encounter_consumer: bool

    Super Class:
        ProductEnvelope
    """
    
    _id: int
    _victim: Token
    _location: Square
    _attacker_reward: int
    _attacker_maneuver: Maneuver
    
    def __init__(
            self,
            id: int,
            victim: Token,
            location: Square,
            attacker_reward: int,
            attacker_maneuver: Maneuver,
            prime_extract: EncounterPrimeExtract,
    ):
        """
            id: int
            victim: Token
            location: Square
            attacker_reward: int
            attacker_maneuver: Maneuver
            prime_extract: EncounterPrimeExtract
        """
        super().__init__(prime_extract=prime_extract)
        self._id = id
        self._victim = victim
        self._location = location
        self._attacker_reward = attacker_reward
        self._attacker_maneuver =attacker_maneuver
  
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def victim(self) -> Token:
        return self._victim
    
    @property
    def location(self) -> Square:
        return self._location
    
    @property
    def attacker_reward(self) -> int:
        return self._attacker_reward
    
    @property
    def attacker_maneuver(self) -> Maneuver:
        return self._attacker_maneuver
        
    @property
    def prime_extract(self) -> EncounterPrimeExtract:
        return cast(EncounterPrimeExtract, super().prime_extract)
    
    @property
    def for_kill_encounter_consumer(self) -> bool:
        return isinstance(self._prime_extract.reference, KillEncounterCarrier)
    
    @property
    def for_checkmate_encounter_consumer(self) -> bool:
        return isinstance(self._prime_extract.reference, CheckmateEncounterCarrier)
    
    @property
    def for_encounter_warning_consumer(self) -> bool:
        return isinstance(self._prime_extract.reference, EncounterWarningCarrier)
    
    @property
    def for_stalemate_encounter_consumer(self) -> bool:
        return isinstance(self._prime_extract.reference, StalemateEncounterCarrier)
    

    