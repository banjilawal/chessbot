# src/domain/metadata/blueprint/model/searchable/walk/attack/mate/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.walk.attack.mate.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import AttackBlueprint, KingToken, Maneuver, CheckmateKing, Token
from err import MateAttackNullException


class MateEnemyBlueprint(AttackBlueprint):
    """
     Role:
        1.  Metadata

     Responsibilities:
        1.  Provides values for hydrating a MateEnemyKing object.

     Attributes:
        attacker: Token
        maneuver: Maneuver
        mated_king: KingToken
        attacker_reward: Optional[int]
        id: Optional[int]
        
        domain_class: Optional[Type[MateEnemyKing]]
        domain_null_exception: Optional[MateAttackNullException]

     Provides:

     Super Class:
        AttackBlueprint
     """
    
    def __init__(
            self,
            attacker: Token,
            maneuver: Maneuver,
            mated_king: KingToken,
            domain_class: Optional[Type[CheckmateKing]] | None = None,
            domain_null_exception: Optional[MateAttackNullException] | None = None,
            attacker_reward: Optional[int] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            attacker: Token
            maneuver: Maneuver
            mated_king: KingToken,
            domain_class: Optional[Type[MateEnemyKing]]
            domain_null_exception: Optional[MateAttackNullException]
            attacker_reward: Optional[int]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            attacker=attacker,
            maneuver=maneuver,
            victim=mated_king,
            attacker_reward=attacker_reward,
            domain_class=domain_class or CheckmateKing,
            domain_null_exception=domain_null_exception or MateAttackNullException(),
        )
    
    @property
    def mated_king(self) -> KingToken:
        return cast(KingToken, super().victim)
    
    @property
    def victim(self) -> KingToken:
        return self.mated_king
    
    
    @property
    def domain_class(self) -> Type[CheckmateKing]:
        return cast(Type[CheckmateKing], super().domain_class)
    
    
    @property
    def domain_null_exception(self) -> MateAttackNullException:
        return cast(MateAttackNullException, super().domain_null_exception)





    
    

        
        