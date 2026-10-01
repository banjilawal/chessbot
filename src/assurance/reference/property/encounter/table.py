# src/assurance/reference/property/encounter/table.py

"""
Module: assurance.reference.property.encounter.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from assurance import EncounterParticipantChart, ReferencePropertyTable
from domain import Encounter, Maneuver


class EncounterReferencePropertyTable(ReferencePropertyTable[Encounter]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores Encounter super class properties that are reference.

    Attributes:
        id: int
        encounterParticipantChart: EncounterParticipantChart
        attacker_maneuver: Maneuver
        attacker_reward: int

    Provides:

    Super Class:
        ReferenceSuperClassPropertyTable
    """
    _id: int
    _attacker_reward: int
    _attacker_maneuver: Maneuver
    _participant_chart: EncounterParticipantChart


    
    def __init__(
            self,
            id: int,
            attacker_reward: int,
            attacker_maneuver: Maneuver,
            participant_chart: EncounterParticipantChart,
    ):
        """
            id: int
            attacker_reward: int
            attacker_maneuver: Maneuver
            participant_chart: EncounterParticipantChart
        """
        self._id = id
        self._maneuver = attacker_maneuver
        self._attacker_reward = attacker_reward
        self._participant_chart = participant_chart

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def maneuver(self) -> Maneuver:
        return self._maneuver
    
    @property
    def attacker_reward(self) -> int:
        return self._attacker_reward
    
    @property
    def participant_chart(self) -> EncounterParticipantChart:
        return self._participant_chart


    