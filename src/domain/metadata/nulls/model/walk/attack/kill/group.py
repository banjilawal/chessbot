# src/domain/metadata/nulls/model/walk/attack/kill/group.py

"""
Module: domain.metadata.nulls.model.walk.attack.kill.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import KillCombatant, AttackNullGroup
from err import (
    KillAttackNullException, KillBlueprintNullException, KillCarrierNullException
)


class KillAttackNullGroup(AttackNullGroup[KillCombatant]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a KillEnemy's integrity cycle.

    Attributes:
        model: KillAttackNullException
        carrier: KillCarrierNullException
        blueprint: KillBlueprintNullException

    Provides:

    Super Class:
        KillNullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[KillAttackNullException] | None = None,
            carrier: Optional[KillCarrierNullException] | None = None,
            blueprint: Optional[KillBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[KillAttackNullException]
            carrier: Optional[KillCarrierNullException]
            blueprint: Optional[KillBlueprintNullException]
        """
        super().__init__(
            model = model or KillAttackNullException(),
            carrier =carrier or KillCarrierNullException(),
            blueprint =blueprint or KillBlueprintNullException(),
        )
        
    @property
    def model(self) -> KillAttackNullException:
        return cast(KillAttackNullException, super().model)
    
    @property
    def carrier(self) -> KillCarrierNullException:
        return cast(KillCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> KillBlueprintNullException:
        return cast(KillBlueprintNullException, super().blueprint)