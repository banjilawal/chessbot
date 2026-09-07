# src/domain/metadata/unions/token/king/types.py

"""
Module: domain.metadata.unions.token.king.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import KingTokenBlueprint, KingToken, TokenTypeUnion
from transit import KingTokenCarrier


class KingTokenUnion(TokenTypeUnion):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a KingToken.

    Attributes:
        model: Type[KingToken]
        carrier: Type[KingTokenCarrier]
        blueprint: Type[KingTokenBlueprint]

    Provides:

    Super Class:
        TokenTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[KingToken]] | None = None,
            carrier: Optional[Type[KingTokenCarrier]] | None = None, 
            blueprint: Optional[Type[KingTokenBlueprint]] | None = None,
    ):
        """
        Args:
            odel: Optional[Type[KingToken]]
            carrier: Optional[Type[KingTokenCarrier]]
            blueprint: Optional[Type[KingTokenBlueprint]]
        """
        super().__init__(
            model=model or KingToken,
            carrier=carrier or KingTokenCarrier,
            blueprint=blueprint or KingTokenBlueprint
        )
    
    @property
    def model(self) -> Type[KingToken]:
        return cast(Type[KingToken], super().model)
    
    @property
    def carrier(self) -> Type[KingTokenCarrier]:
        return cast(Type[KingTokenCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[KingTokenBlueprint]:
        return cast(Type[KingTokenBlueprint], super().blueprint)