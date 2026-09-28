# src/domain/metadata/unions/model/attack/combatant/types.py

"""
Module: domain.metadata.unions.attack.combatant.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Encounter, AttackTypeUnion, KillEncounter, CombatantAttackBlueprint
from transit import CombatantAttackCarrier


class CombatantAttackTypeUnion(AttackModelTypeUnion[Encounter]):
    """
    Role:
        - Metadata

    Responsibilities:
        1.  Catalog of types associated with building and validating a
            CombatantAttack.

    Attributes:
        model: Type[CombatantAttack]
        carrier: Type[CombatantAttackCarrier]
        blueprint: Type[CombatantAttackBlueprint]

    Provides:

    Super Class:
        AttackTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[KillEncounter]] | None = None,
            carrier: Optional[Type[CombatantAttackCarrier]] | None = None,
            blueprint: Optional[Type[CombatantBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[CombatantAttack]]
            carrier: Optional[Type[CombatantAttackCarrier]]
            blueprint: Optional[Type[CombatantAttackBlueprint]]
        """
        super().__init__(
            model=model or KillEncounter,
            carrier=carrier or CombatantAttackCarrier,
            blueprint=blueprint or CombatantAttackBlueprint
        )
    
    @property
    def model(self) -> Type[KillEncounter]:
        return cast(Type[KillEncounter], super().model)
    
    @property
    def carrier(self) -> Type[CombatantAttackCarrier]:
        return cast(Type[CombatantAttackCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[CombatantAttackBlueprint]:
        return cast(Type[CombatantAttackBlueprint], super().blueprint)