# src/domain/metadata/blueprint/model/encounter/kill/blueprint.py

"""
Module: domain.metadata.blueprint.model.encounter.kill.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import EncounterBlueprint, KillEncounter, CombatantToken, Maneuver, Token
from err import CombatantEncounterNullException


class CombatantEncounterBlueprint(EncounterBlueprint[KillEncounter]):
    """
     Role:
        1.  Metadata

     Responsibilities:
        1.  Provides values for hydrating a CombatantEncounter object.

     Attributes:
        encounterer: Token
        maneuver: Maneuver
        victim: CombatantToken
        encounterer_reward: Optional[int]
        id: Optional[int]
        
        domain_class: Optional[Type[CombatantEncounter]]
        domain_null_exception: Optional[KillEncounterNullException]

     Provides:

     Super Class:
        EncounterBlueprint
     """
    
    def __init__(
            self,
            encounterer: Token,
            maneuver: Maneuver,
            victim: CombatantToken,
            domain_class: Optional[Type[KillEncounter]] | None = None,
            domain_null_exception: Optional[CombatantEncounterNullException] | None = None,
            encounterer_reward: Optional[int] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            encounterer: Token
            maneuver: Maneuver
            victim: CombatantToken,
            domain_class: Optional[Type[CombatantEncounter]]
            domain_null_exception: Optional[KillEncounterNullException]
            encounterer_reward: Optional[int]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            encounterer=encounterer,
            maneuver=maneuver,
            victim=victim,
            encounterer_reward=encounterer_reward,
            domain_class=domain_class or KillEncounter,
            domain_null_exception=domain_null_exception or CombatantEncounterNullException(),
        )
    
    @property
    def victim(self) -> CombatantToken:
        return cast(CombatantToken, super().victim)
    
    
    @property
    def domain_class(self) -> Type[KillEncounter]:
        return cast(Type[KillEncounter], super().domain_class)
    
    
    @property
    def domain_null_exception(self) -> CombatantEncounterNullException:
        return cast(CombatantEncounterNullException, super().domain_null_exception)





    
    

        
        