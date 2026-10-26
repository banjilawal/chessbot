# src/domain/metadata/unions/context/token/combatant/types.py

"""
Module: domain.metadata.unions.context.token.combatant.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import CombatantTokenContextBlueprint, CombatantToken, TokenContextTypeUnion
from transit import CombatantTokenContextCarrier


class CombatantTokenContextTypeUnion(TokenContextTypeUnion[CombatantTokenContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a CombatantToken.

    Attributes:
        model: Type[CombatantTokenContext]
        carrier: Type[CombatantContextCarrier]
        blueprint: Type[CombatantContextBlueprint]

    Provides:

    Super Class:
        TokenContextTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[CombatantTokenContext]] | None = None,
            carrier: Optional[Type[CombatantTokenContextCarrier]] | None = None,
            blueprint: Optional[Type[CombatantTokenContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[CombatantTokenContext]]
            carrier: Optional[Type[CombatantContextCarrier]]
            blueprint: Optional[Type[CombatantContextBlueprint]]
        """
        super().__init__(
            model=model or CombatantTokenContext, 
            carrier=carrier or CombatantTokenContextCarrier,
            blueprint=blueprint or CombatantTokenContextBlueprint
        )
    
    @property
    def model(self) -> Type[CombatantTokenContext]:
        return cast(Type[CombatantTokenContext], super().model)
    
    @property
    def carrier(self) -> Type[CombatantTokenContextCarrier]:
        return cast(Type[CombatantTokenContextCarrier], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[CombatantTokenContextBlueprint]:
        return cast(Type[CombatantTokenContextBlueprint], super().contextBlueprint)