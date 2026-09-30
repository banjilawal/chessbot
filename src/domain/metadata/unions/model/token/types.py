# src/domain/metadata/unions/model/token/types.py

"""
Module: domain.metadata.unions.token.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import ModelTypeUnion, Token, TokenBlueprint
from transit import TokenCarrier

T = TypeVar("T", bound="Token")

class TokenTypeUnion(ModelTypeUnion[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Token.

    Attributes:
        model: Type[T]
        carrier: Type[TokenCarrier[T]]
        blueprint: Type[TokenBlueprint]
        
    Provides:

    Super Class:
        ModelTypeUnion
    """
    
    def __init__(
            self,
            model: Type[T],
            carrier: Type[TokenCarrier[T]],
            blueprint: Type[TokenBlueprint[T]],
    ):
        """
        Args:
            model: Type[T]
            carrier: Type[TokenCarrier[T]]
            blueprint: Type[TokenBlueprint]
        """
        super().__init__(
            model=model or Type[T],
            carrier=carrier or Type[TokenCarrier[T]],
            blueprint=blueprint or TokenBlueprint,
        )
    
    @property
    def model(self) -> Type[T]:
        return cast(Type[T], super().model)
    
    @property
    def carrier(self) -> Type[TokenCarrier[T]]:
        return cast(Type[TokenCarrier[T]], super().carrier)
    
    @property
    def blueprint(self) -> Type[TokenBlueprint]:
        return cast(Type[TokenBlueprint], super().blueprint)