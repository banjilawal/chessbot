# src/domain/metadata/blueprint/model/searchable/walk/attack/check/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.walk.attack.check.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import AttackBlueprint, CheckWarning, KingToken, Maneuver, Token
from err import CheckAttackNullException


class CheckEnemyBlueprint(AttackBlueprint):
    """
     Role:
        1.  Metadata

     Responsibilities:
        1.  Provides values for hydrating a CheckEnemyKing object.

     Attributes:
        attacker: Token
        maneuver: Maneuver
        checked_king: KingToken
        attacker_reward: Optional[int]
        id: Optional[int]
        
        domain_class: Optional[Type[CheckEnemyKing]]
        domain_null_exception: Optional[CheckAttackNullException]

     Provides:

     Super Class:
        AttackBlueprint
     """
    
    def __init__(
            self,
            attacker: Token,
            maneuver: Maneuver,
            checked_king: KingToken,
            domain_class: Optional[Type[CheckWarning]] | None = None,
            domain_null_exception: Optional[CheckAttackNullException] | None = None,
            attacker_reward: Optional[int] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            attacker: Token
            maneuver: Maneuver
            checked_king: KingToken,
            domain_class: Optional[Type[CheckEnemyKing]]
            domain_null_exception: Optional[CheckAttackNullException]
            attacker_reward: Optional[int]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            attacker=attacker,
            maneuver=maneuver,
            victim=checked_king,
            attacker_reward=attacker_reward,
            domain_class=domain_class or CheckWarning,
            domain_null_exception=domain_null_exception or CheckAttackNullException(),
        )
    
    @property
    def checked_king(self) -> KingToken:
        return cast(KingToken, super().victim)
    
    @property
    def victim(self) -> KingToken:
        return self.checked_king
    
    
    @property
    def domain_class(self) -> Type[CheckWarning]:
        return cast(Type[CheckWarning], super().domain_class)
    
    
    @property
    def domain_null_exception(self) -> CheckAttackNullException:
        return cast(CheckAttackNullException, super().domain_null_exception)





    
    

        
        