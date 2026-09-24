# src/domain/metadata/nulls/model/attack/combatant/group.py

"""
Module: domain.metadata.nulls.model.attack.combatant.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import AttackNullGroup
from err import (
    CombatantAttackNullException, CombatantAttackCarrierNullException,
    CombatantAttackBlueprintNullException
)


class CombatantAttackNullGroup(AttackNullGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a CombatantAttack's integrity cycle.

    Attributes:
        model: CombatantAttackNullException
        carrier: CombatantAttackCarrierNullException
        blueprint: CombatantAttackBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[CombatantAttackNullException] | None = None,
            carrier: Optional[CombatantAttackCarrierNullException] | None = None,
            blueprint: Optional[CombatantAttackBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[CombatantAttackNullException]
            carrier: Optional[CombatantAttackCarrierNullException]
            blueprint: Optional[CombatantAttackBlueprintNullException]
        """
        super().__init__(
            model =model or CombatantAttackNullException(),
            carrier =carrier or CombatantAttackCarrierNullException(),
            blueprint =blueprint or CombatantAttackBlueprintNullException(),
        )
        
    @property
    def model(self) -> CombatantAttackNullException:
        return cast(CombatantAttackNullException, super().model)
    
    @property
    def carrier(self) -> CombatantAttackCarrierNullException:
        return cast(CombatantAttackCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> CombatantAttackBlueprintNullException:
        return cast(CombatantAttackBlueprintNullException, super().blueprint)