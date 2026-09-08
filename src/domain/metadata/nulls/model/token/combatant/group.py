# src/domain/metadata/nulls/model/token/combatant/group.py

"""
Module: domain.metadata.nulls.model.token.combatant.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import TokenNullGroup
from err import CombatantBlueprintNullException, CombatantCarrierNullException, CombatantNullException


class CombatantNullGroup(TokenNullGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a CombatantToken's integrity cycle.

    Attributes:
        model: CombatantNullException
        carrier: CombatantCarrierNullException
        blueprint: CombatantBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[CombatantNullException] | None = None,
            carrier: Optional[CombatantCarrierNullException] | None = None,
            blueprint: Optional[CombatantBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[CombatantNullException]
            carrier: Optional[CombatantCarrierNullException]
            blueprint: Optional[CombatantBlueprintNullException]
        """
        super().__init__(
            model = model or CombatantNullException(),
            carrier = carrier or CombatantCarrierNullException(),
            blueprint = blueprint or CombatantBlueprintNullException(),
        )
        
    @property
    def model(self) -> CombatantNullException:
        return cast(CombatantNullException, super().model)
    
    @property
    def carrier(self) -> CombatantCarrierNullException:
        return cast(CombatantCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> CombatantBlueprintNullException:
        return cast(CombatantBlueprintNullException, super().blueprint)