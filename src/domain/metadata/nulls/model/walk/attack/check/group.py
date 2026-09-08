# src/domain/metadata/nulls/model/walk/attack/check/group.py

"""
Module: domain.metadata.nulls.model.walk.attack.check.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import AttackNullGroup, CheckKing
from err import (
    CheckAttackNullException, CheckAttackBlueprintNullException, CheckAttackCarrierNullException
)


class CheckAttackNullGroup(AttackNullGroup[CheckKing]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a CheckEnemy's integrity cycle.

    Attributes:
        model: CheckAttackNullException
        carrier: CheckAttackCarrierNullException
        blueprint: CheckAttackBlueprintNullException

    Provides:

    Super Class:
        CheckNullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[CheckAttackNullException] | None = None,
            carrier: Optional[CheckAttackCarrierNullException] | None = None,
            blueprint: Optional[CheckAttackBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[CheckAttackNullException]
            carrier: Optional[CheckAttackCarrierNullException]
            blueprint: Optional[CheckAttackBlueprintNullException]
        """
        super().__init__(
            model = model or CheckAttackNullException(),
            carrier =carrier or CheckAttackCarrierNullException(),
            blueprint =blueprint or CheckAttackBlueprintNullException(),
        )
        
    @property
    def model(self) -> CheckAttackNullException:
        return cast(CheckAttackNullException, super().model)
    
    @property
    def carrier(self) -> CheckAttackCarrierNullException:
        return cast(CheckAttackCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> CheckAttackBlueprintNullException:
        return cast(CheckAttackBlueprintNullException, super().blueprint)