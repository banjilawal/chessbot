# src/domain/metadata/blueprint/model/searchable/walk/attack/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.walk.attack.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Attack, Maneuver, SearchableModelBlueprint, Token


class AttackBlueprint(SearchableModelBlueprint[Attack]):
    """
     Role:
        1.  Metadata

     Responsibilities:
        1.  Provides values for hydrating an Attack object.

     Attributes:
        victim: Token
        attacker: Token
        maneuver: Maneuver
        attacker_reward: Optional[int]
        id: Optional[int]
        
        domain_class: Type[Attack]
        domain_null_exception: AttackNullException

     Provides:

     Super Class:
        SearchableModelBlueprint
     """
    _victim: Token
    _attacker: Token
    _maneuver: Maneuver
    _attacker_reward: Optional[int]
    _id: Optional[int]
    
    def __init__(
            self,
            victim: Token,
            attacker: Token,
            maneuver: Maneuver,
            domain_class: Type[Attack],
            domain_null_exception: AttackNullException,
            attacker_reward: Optional[int] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            victim: Token
            attacker: Token
            maneuver: Maneuver
            domain_class: Type[Attack]
            domain_null_exception: AttackNullException
            attacker_reward: Optional[int]
            id: Optional[int]
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception,
        )
        self._id = id
        self._victim = victim
        self._attacker = attacker
        self._maneuver = maneuver
        self._attacker_reward = attacker_reward

    
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
    def attacker_reward(self) -> Optional[int]:
        return self._attacker_reward
    
    
    @property
    def domain_class(self) -> Type[Attack]:
        return cast(Type[Attack], super().domain_class)
    
    
    @property
    def domain_null_exception(self) -> AttackNullException:
        return cast(AttackNullException, super().domain_null_exception)





    
    

        
        