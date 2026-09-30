# src/domain/metadata/blueprint/model/encounter/blueprint.py

"""
Module: domain.metadata.blueprint.model.encounter.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, Type, TypeVar, cast

from domain import Encounter, StateModelBlueprint, Maneuver, Square, Token
from err import EncounterNullException

T = TypeVar("T", bound="Encounter")


class EncounterBlueprint(StateModelBlueprint[T], Generic[T]):
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
        StateModelBlueprint
     """
    _victim: Token
    _location: Square
    _attacker_maneuver: Maneuver
    _attacker_reward: int
    
    def __init__(
            self,
            victim: Token,
            attacker_maneuver: Maneuver,
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
            attacker_maneuver: Maneuver
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
        self._attacker_maneuver = attacker_maneuver
        self._location = location or attacker_maneuver.path.endpoints.destination
        self._attacker_reward = attacker_reward or victim.rank.ransom
    
    @property
    def victim(self) -> Token:
        return self._victim
    
    @property
    def attacker_maneuver(self) -> Maneuver:
        return self._attacker_maneuver
    
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

    






    
    

        
        