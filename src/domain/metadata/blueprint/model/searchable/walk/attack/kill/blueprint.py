# src/domain/metadata/blueprint/model/searchable/walk/attack/kill/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.walk.attack.kill.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import AttackBlueprint, AttackEnemyCombatant, CombatantToken, Maneuver, Token
from err import KillAttackNullException


class KillEnemyBlueprint(AttackBlueprint):
    """
     Role:
        1.  Metadata

     Responsibilities:
        1.  Provides values for hydrating an AttackEnemyCombatant object.

     Attributes:
        attacker: Token
        maneuver: Maneuver
        victim: CombatantToken
        attacker_reward: Optional[int]
        id: Optional[int]
        
        domain_class: Optional[Type[AttackEnemyCombatant]]
        domain_null_exception: Optional[KillAttackNullException]

     Provides:

     Super Class:
        AttackBlueprint
     """
    
    def __init__(
            self,
            attacker: Token,
            maneuver: Maneuver,
            victim: CombatantToken,
            domain_class: Optional[Type[AttackEnemyCombatant]] | None = None,
            domain_null_exception: Optional[KillAttackNullException] | None = None,
            attacker_reward: Optional[int] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            attacker: Token
            maneuver: Maneuver
            victim: CombatantToken,
            domain_class: Optional[Type[AttackEnemyCombatant]]
            domain_null_exception: Optional[KillAttackNullException]
            attacker_reward: Optional[int]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            attacker=attacker,
            maneuver=maneuver,
            victim=victim,
            attacker_reward=attacker_reward,
            domain_class=domain_class or AttackEnemyCombatant,
            domain_null_exception=domain_null_exception or KillAttackNullException(),
        )
    
    @property
    def victim(self) -> CombatantToken:
        return cast(CombatantToken, super().victim)
    
    
    @property
    def domain_class(self) -> Type[AttackEnemyCombatant]:
        return cast(Type[AttackEnemyCombatant], super().domain_class)
    
    
    @property
    def domain_null_exception(self) -> KillAttackNullException:
        return cast(KillAttackNullException, super().domain_null_exception)





    
    

        
        