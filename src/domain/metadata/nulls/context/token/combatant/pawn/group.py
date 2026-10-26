# src/domain/metadata/nulls/context/token/combatant/pawn/group.py

"""
Module: domain.metadata.nulls.context.token.combatant.pawn.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CombatantTokenContextNullGroup
from err import PawnTokenContextBlueprintNullException, PawnTokenContextCarrierNullException, PawnTokenContextNullException


class PawnTokenTokenContextNullGroup(CombatantTokenContextNullGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a PawnToken's integrity cycle.

    Attributes:
        context: PawnTokenContextNullException
        carrier: PawnTokenContextCarrierNullException
        blueprint: PawnTokenContextBlueprintNullException

    Provides:

    Super Class:
        PawnTokenContextNullGroup
    """
    
    def __init__(
            self,
            context: Optional[PawnTokenContextNullException] | None = None,
            carrier: Optional[PawnTokenContextCarrierNullException] | None = None,
            blueprint: Optional[PawnTokenContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[PawnTokenContextNullException]
            carrier: Optional[PawnTokenContextCarrierNullException]
            blueprint: Optional[PawnTokenContextBlueprintNullException]
        """
        super().__init__(
            context = context or PawnTokenContextNullException(),
            carrier = carrier or PawnTokenContextCarrierNullException(),
            blueprint = blueprint or PawnTokenContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> PawnTokenContextNullException:
        return cast(PawnTokenContextNullException, super().context)
    
    @property
    def carrier(self) -> PawnTokenContextCarrierNullException:
        return cast(PawnTokenContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> PawnTokenContextBlueprintNullException:
        return cast(PawnTokenContextBlueprintNullException, super().blueprint)