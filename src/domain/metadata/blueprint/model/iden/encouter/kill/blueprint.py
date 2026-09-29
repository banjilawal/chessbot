# src/domain/metadata/blueprint/model/iden/encounter/kill/blueprint.py

"""
Module: domain.metadata.blueprint.model.iden.encounter.kill.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import (
    CombatantToken, EncounterBlueprint, KillEncounter, Maneuver, Square
)
from err import KillEncounterNullException


class KillEncounterBlueprint(EncounterBlueprint[KillEncounter]):
    """
     Role:
        1.  Metadata

     Responsibilities:
        1.  Provides values for hydrating a KillEncounter object.

     Attributes:
        victim: CombatantToken
        maneuver: Maneuver
        location: Square
        attacker_reward: int
        id: Optional[int]
        
        domain_class: Optional[Type[KillEncounter]]
        domain_null_exception: Optional[KillEncounterNullException]

     Provides:

     Super Class:
        EncounterBlueprint
     """
    
    def __init__(
            self,
            victim: CombatantToken,
            maneuver: Maneuver,
            domain_class: Optional[Type[KillEncounter]] | None = None,
            domain_null_exception: Optional[KillEncounterNullException] | None = None,
            location: Optional[Square] | None = None,
            attacker_reward: Optional[int] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            victim: CombatantToken
            maneuver: Maneuver
            domain_class: Optional[Type[KillEncounter]]
            domain_null_exception: Optional[KillEncounterNullException]
            location: Optional[Square]
            attacker_reward: Optional[int]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            victim=victim,
            maneuver=maneuver,
            location=location,
            attacker_reward=attacker_reward,
            domain_class=domain_class or KillEncounter,
            domain_null_exception=domain_null_exception or KillEncounterNullException(),
        )
    
    @property
    def victim(self) -> CombatantToken:
        return cast(CombatantToken, super().victim)
    
    
    @property
    def domain_class(self) -> Type[KillEncounter]:
        return cast(Type[KillEncounter], super().domain_class)
    
    
    @property
    def domain_null_exception(self) -> KillEncounterNullException:
        return cast(KillEncounterNullException, super().domain_null_exception)