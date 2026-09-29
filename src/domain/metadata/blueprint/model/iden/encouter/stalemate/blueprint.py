# src/domain/metadata/blueprint/model/iden/encounter/stalemate/blueprint.py

"""
Module: domain.metadata.blueprint.model.iden.encounter.stalemate.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import EncounterBlueprint, Maneuver, StalemateEncounter, Square
from err import StalemateEncounterNullException


class StalemateEncounterBlueprint(EncounterBlueprint[StalemateEncounter]):
    """
     Role:
        1.  Metadata

     Responsibilities:
        1.  Provides values for hydrating a StalemateEncounter object.

     Attributes:
        id: int
        victim: KingToken
        maneuver: Maneuver
        location: Square
        attacker_reward: int
        
        domain_class: Optional[Type[StalemateEncounter]]
        domain_null_exception: Optional[MateEncounterNullException]

     Provides:

     Super Class:
        EncounterBlueprint
     """
    _counter_maneuver: Maneuver
    
    def __init__(
            self,
            maneuver: Maneuver,
            counter_maneuver: Maneuver,
            domain_class: Optional[Type[StalemateEncounter]] | None = None,
            domain_null_exception: Optional[StalemateEncounterNullException] | None = None,
            location: Optional[Square] | None = None,
            attacker_reward: Optional[int] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            maneuver: Maneuver
            counter_maneuver: Maneuver
            domain_class: Optional[Type[StalemateEncounter]]
            domain_null_exception: Optional[MateEncounterNullException]
            location: Optional[Square]
            attacker_reward: Optional[int]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            victim=counter_maneuver.traveler,
            maneuver=maneuver,
            location=location,
            attacker_reward=attacker_reward,
            domain_class=domain_class or StalemateEncounter,
            domain_null_exception=domain_null_exception or StalemateEncounterNullException(),
        )
        self._counter_maneuver = counter_maneuver
        
    @property
    def counter_maneuver(self) -> Maneuver:
        return self._counter_maneuver

    @property
    def domain_class(self) -> Type[StalemateEncounter]:
        return cast(Type[StalemateEncounter], super().domain_class)
    
    @property
    def domain_null_exception(self) -> StalemateEncounterNullException:
        return cast(StalemateEncounterNullException, super().domain_null_exception)







    
    

        
        