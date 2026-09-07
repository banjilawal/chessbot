# src/domain/metadata/unions/token/types.py

"""
Module: domain.metadata.unions.token.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Token, TokenBlueprint, TypeUnion
from transit import TokenCarrier


class TokenTypeUnion(TypeUnion[Token]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an Token.

    Attributes:
        model: Type[Token]
        carrier: Type[TokenCarrier]
        blueprint: Type[TokenBlueprint]

    Provides:

    Super Class:
        TypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Token]] | None = None,
            carrier: Optional[Type[TokenCarrier]] | None = None, 
            blueprint: Optional[Type[TokenBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Token]]
            carrier: Optional[Type[TokenCarrier]
            blueprint: Optional[Type[TokenBlueprint] 
        """
        super().__init__(
            model=model or Token, 
            carrier=carrier or TokenCarrier, 
            blueprint=blueprint or TokenBlueprint
        )
    
    @property
    def model(self) -> Type[Token]:
        return cast(Type[Token], super().model)
    
    @property
    def carrier(self) -> Type[TokenCarrier]:
        return cast(Type[TokenCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[TokenBlueprint]:
        return cast(Type[TokenBlueprint], super().blueprint)