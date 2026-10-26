# src/domain/metadata/nulls/context/token/combatant/group.py

"""
Module: domain.metadata.nulls.context.token.combatant.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CombatantToken, TokenContextNullGroup
from err import (
    CombatantContextBlueprintNullException, CombatantContextCarrierNullException, CombatantTokenContextNullException
)


class CombatantTokenContextNullGroup(TokenContextNullGroup[CombatantTokenContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a CombatantToken's integrity cycle.

    Attributes:
        context: CombatantContextNullException
        carrier: CombatantContextCarrierNullException
        blueprint: CombatantContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[CombatantTokenContextNullException] | None = None,
            carrier: Optional[CombatantContextCarrierNullException] | None = None,
            blueprint: Optional[CombatantContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[CombatantContextNullException]
            carrier: Optional[CombatantContextCarrierNullException]
            blueprint: Optional[CombatantContextBlueprintNullException]
        """
        super().__init__(
            context =context or CombatantTokenContextNullException(),
            carrier = carrier or CombatantContextCarrierNullException(),
            blueprint = blueprint or CombatantContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> CombatantTokenContextNullException:
        return cast(CombatantTokenContextNullException, super().context)
    
    @property
    def carrier(self) -> CombatantContextCarrierNullException:
        return cast(CombatantContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> CombatantContextBlueprintNullException:
        return cast(CombatantContextBlueprintNullException, super().blueprint)