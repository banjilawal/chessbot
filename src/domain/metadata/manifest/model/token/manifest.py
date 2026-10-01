# src/domain/metadata/manifest/model/token/token/manifest.py

"""
Module: domain.metadata.manifest.model.token.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import ModelManifest, Token, TokenNullGroup, TokenTypeUnion

T = TypeVar("T", bound="Token")

class TokenManifest(ModelManifest[T], Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the Token
            security lifecycle.

     Attributes:
        types: TokenTypeUnion[T]
        nulls: TokenNullGroup[T]

     Provides:

     Super Class:
        ModelManifest
     """

    def __init__(
            self,
            types: Optional[TokenTypeUnion[T]] | None = None,
            nulls: Optional[TokenNullGroup[T]] | None = None,
    ):
        """
        Args:
            types: TokenTypeUnion[T]
            nulls: TokenNullGroup[T]
        """
        super().__init__(
            types=types or TokenTypeUnion(),
            nulls=nulls or TokenNullGroup(),
        )

    @property
    def types(self) -> TokenTypeUnion[T]:
        return cast(TokenTypeUnion[T], super().types)

    @property
    def nulls(self) -> TokenNullGroup[T]:
        return cast(TokenNullGroup[T], super().nulls)