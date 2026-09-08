# src/domain/metadata/nulls/model/walk/attack/mate/group.py

"""
Module: domain.metadata.nulls.model.walk.attack.mate.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import AttackNullGroup
from err import (
    MateAttackNullException, MateAttackBlueprintNullException, MateAttackCarrierNullException
)


class MateAttackNullGroup(AttackNullGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a MateEnemy's integrity cycle.

    Attributes:
        model: MateAttackNullException
        carrier: MateAttackCarrierNullException
        blueprint: MateAttackBlueprintNullException

    Provides:

    Super Class:
        MateNullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[MateAttackNullException] | None = None,
            carrier: Optional[MateAttackCarrierNullException] | None = None,
            blueprint: Optional[MateAttackBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[MateAttackNullException]
            carrier: Optional[MateAttackCarrierNullException]
            blueprint: Optional[MateAttackBlueprintNullException]
        """
        super().__init__(
            model = model or MateAttackNullException(),
            carrier =carrier or MateAttackCarrierNullException(),
            blueprint =blueprint or MateAttackBlueprintNullException(),
        )
        
    @property
    def model(self) -> MateAttackNullException:
        return cast(MateAttackNullException, super().model)
    
    @property
    def carrier(self) -> MateAttackCarrierNullException:
        return cast(MateAttackCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> MateAttackBlueprintNullException:
        return cast(MateAttackBlueprintNullException, super().blueprint)