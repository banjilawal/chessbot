# src/domain/metadata/blueprint/model/attack/mate/blueprint.py

"""
Module: domain.metadata.blueprint.model.attack.mate.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import AttackBlueprint, KingToken, Maneuver, CheckmateAttack, Token
from err import CheckmateAttackNullException


class CheckmateAttackBlueprint(AttackBlueprint[CheckmateAttack]):
    """
     Role:
        1.  Metadata

     Responsibilities:
        1.  Provides values for hydrating a CheckmateAttack object.

     Attributes:
        attacker: Token
        maneuver: Maneuver
        mated_king: KingToken
        attacker_reward: Optional[int]
        id: Optional[int]
        
        domain_class: Optional[Type[CheckmateAttack]]
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
            domain_class: Optional[Type[CheckmateAttack]] | None = None,
            domain_null_exception: Optional[CheckmateAttackNullException] | None = None,
            attacker_reward: Optional[int] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            attacker: Token
            maneuver: Maneuver
            mated_king: KingToken,
            domain_class: Optional[Type[CheckmateAttack]]
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
            domain_class=domain_class or CheckmateAttack,
            domain_null_exception=domain_null_exception or CheckmateAttackNullException(),
        )
    
    @property
    def mated_king(self) -> KingToken:
        return cast(KingToken, super().victim)
    
    @property
    def victim(self) -> KingToken:
        return self.mated_king
    
    
    @property
    def domain_class(self) -> Type[CheckmateAttack]:
        return cast(Type[CheckmateAttack], super().domain_class)
    
    
    @property
    def domain_null_exception(self) -> CheckmateAttackNullException:
        return cast(CheckmateAttackNullException, super().domain_null_exception)





    
    

        
        