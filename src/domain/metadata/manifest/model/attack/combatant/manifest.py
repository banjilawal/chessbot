# src/domain/metadata/manifest/model/attack/combatant/manifest.py

"""
Module: domain.metadata.manifest.model.attack.combatant.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    CombatantAttackNullGroup, CombatantAttack, AttackManifest, CombatantAttackTypeUnion
)


class CombatantAttackManifest(AttackManifest[CombatantAttack]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the CombatantAttack
            security lifecycle.

     Attributes:
        types: CombatantAttackTypeUnion
        nulls: CombatantAttackNullGroup

     Provides:

     Super Class:
        AttackManifest
     """
    
    def __init__(
            self,
            types: Optional[CombatantAttackTypeUnion] | None = None,
            nulls: Optional[CombatantAttackNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[CombatantAttackTypeUnion]
            nulls: Optional[CombatantAttackNullGroup]
        """
        super().__init__(
            types=types or CombatantAttackTypeUnion(),
            nulls=nulls or CombatantAttackNullGroup(),
        )
    
    @property
    def types(self) -> CombatantAttackTypeUnion:
        return cast(CombatantAttackTypeUnion, super().types)
    
    @property
    def nulls(self) -> CombatantAttackNullGroup:
        return cast(CombatantAttackNullGroup, super().nulls)