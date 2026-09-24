# src/domain/metadata/nulls/model/attack/mate/group.py

"""
Module: domain.metadata.nulls.model.attack.mate.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import AttackNullGroup
from err import (
    CheckmateAttackBlueprintNullException, CheckmateAttackCarrierNullException,
    CheckmateAttackNullException
)


class CheckmateAttackNullGroup(AttackNullGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a MateAttack's integrity cycle.

    Attributes:
        model: MateAttackNullException
        carrier: MateAttackCarrierNullException
        blueprint: MateAttackBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[CheckmateAttackNullException] | None = None,
            carrier: Optional[CheckmateAttackCarrierNullException] | None = None,
            blueprint: Optional[CheckmateAttackBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[MateAttackNullException]
            carrier: Optional[MateAttackCarrierNullException]
            blueprint: Optional[MateAttackBlueprintNullException]
        """
        super().__init__(
            model =model or CheckmateAttackNullException(),
            carrier =carrier or CheckmateAttackCarrierNullException(),
            blueprint =blueprint or CheckmateAttackBlueprintNullException(),
        )
        
    @property
    def model(self) -> CheckmateAttackNullException:
        return cast(CheckmateAttackNullException, super().model)
    
    @property
    def carrier(self) -> CheckmateAttackCarrierNullException:
        return cast(CheckmateAttackCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> CheckmateAttackBlueprintNullException:
        return cast(CheckmateAttackBlueprintNullException, super().blueprint)