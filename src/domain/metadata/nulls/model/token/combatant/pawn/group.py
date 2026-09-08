# src/domain/metadata/nulls/model/token/combatant/pawn/group.py

"""
Module: domain.metadata.nulls.model.token.combatant.pawn.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CombatantNullGroup
from err import PawnTokenBlueprintNullException, PawnTokenCarrierNullException, PawnTokenNullException


class PawnTokenNullGroup(CombatantNullGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a PawnToken's integrity cycle.

    Attributes:
        model: PawnTokenNullException
        carrier: PawnTokenCarrierNullException
        blueprint: PawnTokenBlueprintNullException

    Provides:

    Super Class:
        PawnTokenNullGroup
    """
    
    def __init__(
            self,
            model: Optional[PawnTokenNullException] | None = None,
            carrier: Optional[PawnTokenCarrierNullException] | None = None,
            blueprint: Optional[PawnTokenBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[PawnTokenNullException]
            carrier: Optional[PawnTokenCarrierNullException]
            blueprint: Optional[PawnTokenBlueprintNullException]
        """
        super().__init__(
            model = model or PawnTokenNullException(),
            carrier = carrier or PawnTokenCarrierNullException(),
            blueprint = blueprint or PawnTokenBlueprintNullException(),
        )
        
    @property
    def model(self) -> PawnTokenNullException:
        return cast(PawnTokenNullException, super().model)
    
    @property
    def carrier(self) -> PawnTokenCarrierNullException:
        return cast(PawnTokenCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> PawnTokenBlueprintNullException:
        return cast(PawnTokenBlueprintNullException, super().blueprint)