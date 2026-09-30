# src/domain/metadata/blueprint/model/state/encounter/checkmate/blueprint.py

"""
Module: domain.metadata.blueprint.model.state.encounter.checkmate.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import EncounterBlueprint, KingToken, Maneuver, CheckmateEncounter, Square
from err import CheckmateEncounterNullException


class CheckmateEncounterBlueprint(EncounterBlueprint[CheckmateEncounter]):
    """
     Role:
        1.  Metadata

     Responsibilities:
        1.  Provides values for hydrating a CheckmateEncounter object.

     Attributes:
        id: int
        victim: KingToken
        maneuver: Maneuver
        location: Square
        attacker_reward: int
        
        domain_class: Optional[Type[CheckmateEncounter]]
        domain_null_exception: Optional[MateEncounterNullException]

     Provides:

     Super Class:
        EncounterBlueprint
     """
    
    def __init__(
            self,
            victim: KingToken,
            attacker_maneuver: Maneuver,
            domain_class: Optional[Type[CheckmateEncounter]] | None = None,
            domain_null_exception: Optional[CheckmateEncounterNullException] | None = None,
            location: Optional[Square] | None = None,
            attacker_reward: Optional[int] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            victim: KingToken
            attacker_maneuver: Maneuver
            domain_class: Optional[Type[CheckmateEncounter]]
            domain_null_exception: Optional[MateEncounterNullException]
            location: Optional[Square]
            attacker_reward: Optional[int]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            victim=victim,
            attacker_maneuver=attacker_maneuver,
            location=location,
            attacker_reward=attacker_reward,
            domain_class=domain_class or CheckmateEncounter,
            domain_null_exception=domain_null_exception or CheckmateEncounterNullException(),
        )
    
    @property
    def looser(self) -> KingToken:
        return cast(KingToken, super().victim)
    
    @property
    def victim(self) -> KingToken:
        return self.looser
    
    
    @property
    def domain_class(self) -> Type[CheckmateEncounter]:
        return cast(Type[CheckmateEncounter], super().domain_class)
    
    @property
    def domain_null_exception(self) -> CheckmateEncounterNullException:
        return cast(CheckmateEncounterNullException, super().domain_null_exception)






    
    

        
        