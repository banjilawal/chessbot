# src/domain/metadata/blueprint/context/model/attack/blueprint.py

"""
Module: domain.metadata.blueprint.context.model.attack.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type, cast

from domain import KingToken, Maneuver, ModelContextBlueprint, Token


class AttackContextBlueprint(ModelContextBlueprint[AttackContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating an AttackContext.
         
     Attributes:
        attacker: Optional[Token]
        maneuver: Optional[Maneuver]
        attacker_reward: Optional[int]
        mated_king: Optional[KingToken]
        checked_king: Optional[KingToken]
        killed_enemy_combatant: Optional[Token]
        
        domain_class: Type[AttackContext]
        domain_null_exception: AttackContextNullException

     Provides:

     Super Class:
        ModelContextBlueprint
     """

    _attacker: Optional[Token]
    _maneuver: Optional[Maneuver]
    _attacker_reward: Optional[int]
    _mated_king: Optional[KingToken]
    _checked_king: Optional[KingToken]
    _killed_enemy_combatant: Optional[Token]
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            attacker: Optional[Token] | None = None,
            maneuver: Optional[Maneuver] | None = None,
            attacker_reward: Optional[int] | None = None,
            mated_king: Optional[KingToken] | None = None,
            checked_king: Optional[KingToken] | None = None,
            killed_enemy_combatant: Optional[Token] | None = None,
            domain_class: Optional[Type[AttackContext]] | None = None,
            domain_null_exception: Optional[AttackContextNullException] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            attacker: Optional[Token]
            maneuver: Optional[Maneuver]
            attacker_reward: Optional[int]
            mated_king: Optional[KingToken]
            checked_king: Optional[KingToken]
            domain_class: Type[AttackContext]
            domain_null_exception: AttackContextNullException
            killed_enemy_combatant: Optional[Token]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[AttackContext],
            domain_null_exception=domain_null_exception or AttackContextNullException(),
        )
        self._attacker = attacker
        self._maneuver = maneuver
        self._mated_king = mated_king
        self._checked_king = checked_king
        self._attacker_reward = attacker_reward
        self._killed_enemy_combatant = killed_enemy_combatant
    
    @property
    def domain_class(self) -> Type[AttackContext]:
        return cast(Type[AttackContext], super().domain_class)
    
    @property
    def domain_null_exception(self) -> AttackContextNullException:
        return  cast(AttackContextNullException, super().domain_null_exception)
    
    
    @property
    def attacker(self) -> Optional[Token]:
        return self._attacker
    
    
    @property
    def maneuver(self) -> Optional[Maneuver]:
        return self._maneuver
    
    
    @property
    def attacker_reward(self) -> Optional[int]:
        return self._attacker_reward
    
    
    @property
    def mated_king(self) -> Optional[KingToken]:
        return self._mated_king
    
    
    @property
    def checked_king(self) -> Optional[KingToken]:
        return self._checked_king
    
    
    @property
    def attacker_reward(self) -> Optional[int]:
        return self._attacker_reward
    
    
    @property
    def killed_enemy_combatant(self) -> Optional[Token]:
        return self._killed_enemy_combatant
    
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "attacker": self._attacker,
            "maneuver": self._maneuver,
            "mated_king": self._mated_king,
            "checked_king": self._checked_king,
            "attacker_reward": self._attack_reward,
            "killed_enemy_combatant": self._killed_enemy_combatant,
        }
    
    
    
    
    


