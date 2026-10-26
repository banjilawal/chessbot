# src/domain/metadata/unions/context/token/king/types.py

"""
Module: domain.metadata.unions.context.token.king.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import KingTokenContextBlueprint, KingToken, TokenContextTypeUnion
from transit import KingTokenContextCarrier


class KingTokenContextTypeUnion(TokenContextTypeUnion[KingTokenContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a KingToken.

    Attributes:
        model: Type[KingTokenContext]
        carrier: Type[KingTokenContextCarrier]
        blueprint: Type[KingTokenContextBlueprint]

    Provides:

    Super Class:
        TokenContextTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[KingTokenContext]] | None = None,
            carrier: Optional[Type[KingTokenContextCarrier]] | None = None,
            blueprint: Optional[Type[KingTokenContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[KingTokenContext]]
            carrier: Optional[Type[KingTokenContextCarrier]]
            blueprint: Optional[Type[KingTokenContextBlueprint]]
        """
        super().__init__(
            model=model or KingTokenContext, 
            carrier=carrier or KingTokenContextCarrier,
            blueprint=blueprint or KingTokenContextBlueprint
        )
    
    @property
    def model(self) -> Type[KingTokenContext]:
        return cast(Type[KingTokenContext], super().model)
    
    @property
    def carrier(self) -> Type[KingTokenContextCarrier]:
        return cast(Type[KingTokenContextCarrier], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[KingTokenContextBlueprint]:
        return cast(Type[KingTokenContextBlueprint], super().contextBlueprint)