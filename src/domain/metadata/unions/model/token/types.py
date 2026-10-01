# src/domain/metadata/unions/model/token/types.py

"""
Module: domain.metadata.unions.token.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Type, TypeVar, cast

from domain import ModelTypeUnion, Token, TokenBlueprint
from transit import TokenCarrier

T = TypeVar("T", bound="Token")


class TokenTypeUnion(ModelTypeUnion[T], Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Token.

    Attributes:
        model: Type[Token]
        carrier: Type[TokenCarrier]
        blueprint: Type[TokenBlueprint]

    Provides:

    Super Class:
        ModelTypeUnion
    """
    
    def __init__(
            self,
            model: Optional[Type[T]] | None = None,
            carrier: Optional[Type[TokenCarrier[T]]] | None = None,
            blueprint: Optional[Type[TokenBlueprint[T]]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[T]]
            carrier: Optional[Type[TokenCarrier[T]]]
            blueprint: Optional[Type[TokenBlueprint[T]]]
        """
        super().__init__(
            model=model or Token,
            carrier=carrier or TokenCarrier,
            blueprint=blueprint or TokenBlueprint,
        )
    
    @property
    def model(self) -> Type[T]:
        return cast(Type[T], super().model)
    
    @property
    def carrier(self) -> Type[TokenCarrier[T]]:
        return cast(Type[TokenCarrier[T]], super().carrier)
    
    @property
    def blueprint(self) -> Type[TokenBlueprint[T]]:
        return cast(Type[TokenBlueprint[T]], super().blueprint)