# src/domain/metadata/nulls/model/walk/attack/group.py

"""
Module: domain.metadata.nulls.model.walk.attack.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import NullExceptionGroup
from err import AttackBlueprintNullException, AttackCarrierNullException, AttackNullException


class AttackNullGroup(NullExceptionGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Attack's integrity cycle.

    Attributes:
        model: AttackNullException
        carrier: AttackCarrierNullException
        blueprint: AttackBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[AttackNullException] | None = None,
            carrier: Optional[AttackCarrierNullException] | None = None,
            blueprint: Optional[AttackBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[AttackNullException]
            carrier: Optional[AttackCarrierNullException]
            blueprint: Optional[AttackBlueprintNullException]
        """
        super().__init__(
            model = model or AttackNullException(),
            carrier = carrier or AttackCarrierNullException(),
            blueprint = blueprint or AttackBlueprintNullException(),
        )
        
    @property
    def model(self) -> AttackNullException:
        return cast(AttackNullException, super().model)
    
    @property
    def carrier(self) -> AttackCarrierNullException:
        return cast(AttackCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> AttackBlueprintNullException:
        return cast(AttackBlueprintNullException, super().blueprint)