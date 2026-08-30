# srcdomain/search/model/attack/context.py

"""
Module: domain.search.model.attack.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import Attack, KingToken, Maneuver, ModelContext, Token


class AttackContext(ModelContext[Attack]):
    """
     Role:
        1.  Metadata

     Responsibilities:
        1.  Supply AttackSearcher with targeting criteria.
         
     Attributes:
        victor: Optional[Token]
        attacker: Optional[Token]
        maneuver: Optional[Maneuver]
        attacker_reward: Optional[int]
        mated_king: Optional[KingToken]
        checked_king: Optional[KingToken]
        killed_enemy_combatant: Optional[Token]

     Provides:

     Super Class:
        ModelContext
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
            victor: Optional[Token] | None = None,
            attacker: Optional[Token] | None = None,
            maneuver: Optional[Maneuver] | None = None,
            attacker_reward: Optional[int] | None = None,
            mated_king: Optional[KingToken] | None = None,
            checked_king: Optional[KingToken] | None = None,
            killed_enemy_combatant: Optional[Token] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            victor: Optional[Token]
            attacker: Optional[Token]
            maneuver: Optional[Maneuver]
            attacker_reward: Optional[int]
            mated_king: Optional[KingToken]
            checked_king: Optional[KingToken]
            domain_class: Type[AttackContext]
            domain_null_exception: AttackContextNullException
            killed_enemy_combatant: Optional[Token]
        """
        super().__init__(id=id,)
        self._victor = victor
        self._attacker = attacker
        self._maneuver = maneuver
        self._mated_king = mated_king
        self._checked_king = checked_king
        self._attacker_reward = attacker_reward
        self._killed_enemy_combatant = killed_enemy_combatant
    
    
    @property
    def victor(self) -> Optional[Token]:
        return self._victor
    
    
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
            "victor": self._victor,
            "attacker": self._attacker,
            "maneuver": self._maneuver,
            "mated_king": self._mated_king,
            "checked_king": self._checked_king,
            "attacker_reward": self._attack_reward,
            "killed_enemy_combatant": self._killed_enemy_combatant,
        }
    
    
    
    
    


