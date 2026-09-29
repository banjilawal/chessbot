# src/domain/metadata/blueprint/model/encounter/blueprint.py

"""
Module: domain.metadata.blueprint.model.encounter.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, Type, TypeVar, cast

from domain import Encounter, IdentifiableModelBlueprint, Maneuver, Square, Token
from err import EncounterNullException

T = TypeVar("T", bound="Encounter")


class EncounterBlueprint(IdentifiableModelBlueprint[T], Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
        1.  Provides values for hydrating an Encounter object.

     Attributes:
        victim: Token
        location: Square
        maneuver: Maneuver
        attacker_reward: int
        id: Optional[int]
        
        domain_class: Type[T]
        domain_null_exception: EncounterNullException

     Provides:

     Super Class:
        IdentifiableModelBlueprint
     """
    _victim: Token
    _location: Square
    _maneuver: Maneuver
    _attacker_reward: int
    
    def __init__(
            self,
            victim: Token,
            maneuver: Maneuver,
            domain_class: Type[T],
            domain_null_exception: EncounterNullException,
            attacker_reward: Optional[int] | None = None,
            location: Optional[Square] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            victim: Token
            location: Square
            maneuver: Maneuver
            domain_class: Type[T]
            domain_null_exception: EncounterNullException
            attacker_reward: Optional[int]
            location: Optional[Square]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            domain_class=domain_class,
            domain_null_exception=domain_null_exception,
        )
        self._victim = victim
        self._maneuver = maneuver
        self._location = location or maneuver.path.endpoints.destination
        self._attacker_reward = attacker_reward or victim.rank.ransom
    
    @property
    def victim(self) -> Token:
        return self._victim
    
    @property
    def maneuver(self) -> Maneuver:
        return self._maneuver
    
    @property
    def attacker_reward(self) -> int:
        return self._attacker_reward
    
    @property
    def location(self) -> Square:
        return self._location
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> EncounterNullException:
        return cast(EncounterNullException, super().domain_null_exception)

    






    
    

        
        