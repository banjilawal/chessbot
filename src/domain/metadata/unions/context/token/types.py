# src/domain/metadata/unions/context/token/types.py

"""
Module: domain.metadata.unions.context.token.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Type, TypeVar, cast

from domain import ContextTypeUnion, Token, TokenContextBlueprint
from transit import TokenContextCarrier

T = TypeVar("T", bound="Token")


class TokenContextTypeUnion(ContextTypeUnion[TContext], Generic[TContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Token.

    Attributes:
        model: Type[TokenContext]
        carrier: Type[TokenContextCarrier]
        blueprint: Type[TokenContextBlueprint]

    Provides:

    Super Class:
        ContextTypeUnion
    """
    
    def __init__(
            self,
            model: Optional[Type[TContext]] | None = None,
            carrier: Optional[Type[TokenContextCarrier[TContext]]Context] | None = None,
            blueprint: Optional[Type[TokenContextBlueprint[TContext]]Context] | None = None,
    ):
        """
        Args:
            model: Optional[Type[TContext]]
            carrier: Optional[Type[TokenContextCarrier[TContext]]Context]
            blueprint: Optional[Type[TokenContextBlueprint[TContext]]Context]
        """
        super().__init__(
            model=model or TokenContext, 
            carrier=carrier or TokenContextCarrier,
            blueprint=blueprint or TokenContextBlueprint,
        )
    
    @property
    def model(self) -> Type[TContext]:
        return cast(Type[TContext], super().model)
    
    @property
    def carrier(self) -> Type[TokenContextCarrier[TContext]]:
        return cast(Type[TokenContextCarrier[TContext]], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[TokenContextBlueprint[TContext]]:
        return cast(Type[TokenContextBlueprint[TContext]], super().contextBlueprint)