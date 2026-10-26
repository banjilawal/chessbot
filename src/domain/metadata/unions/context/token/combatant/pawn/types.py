# src/domain/metadata/unions/context/token/combatant/pawn/types.py

"""
Module: domain.metadata.unions.context.token.combatant.pawn.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import CombatantTokenContextTypeUnion, PawnTokenContextBlueprint, PawnToken
from transit import PawnTokenContextCarrier


class PawnTokenContextTypeUnion(CombatantTokenContextTypeUnion):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a PawnToken.

    Attributes:
        model: Type[PawnTokenContext]
        carrier: Type[PawnTokenContextCarrier]
        blueprint: Type[PawnTokenContextBlueprint]

    Provides:

    Super Class:
        ComabtantTokenUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[PawnTokenContext]] | None = None,
            carrier: Optional[Type[PawnTokenContextCarrier]] | None = None,
            blueprint: Optional[Type[PawnTokenContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[PawnTokenContext]]
            carrier: Optional[Type[PawnTokenContextCarrier]]
            blueprint: Optional[Type[PawnTokenContextBlueprint]]
        """
        super().__init__(
            model=model or PawnTokenContext, 
            carrier=carrier or PawnTokenContextCarrier,
            blueprint=blueprint or PawnTokenContextBlueprint
        )
    
    @property
    def model(self) -> Type[PawnTokenContext]:
        return cast(Type[PawnTokenContext], super().model)
    
    @property
    def carrier(self) -> Type[PawnTokenContextCarrier]:
        return cast(Type[PawnTokenContextCarrier], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[PawnTokenContextBlueprint]:
        return cast(Type[PawnTokenContextBlueprint], super().contextBlueprint)