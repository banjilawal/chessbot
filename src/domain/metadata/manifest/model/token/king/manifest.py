# src/domain/metadata/manifest/model/token/king/manifest.py

"""
Module: domain.metadata.manifest.model.token.king.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    KingTokenNullGroup, KingToken, TokenManifest, KingTokenTypeUnion
)


class KingTokenManifest(TokenManifest[KingToken]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the KingToken
            security lifecycle.

     Attributes:
        types: KingTokenTypeUnion
        nulls: KingTokenNullGroup

     Provides:

     Super Class:
        TokenManifest
     """
    
    def __init__(
            self,
            types: Optional[KingTokenTypeUnion] | None = None,
            nulls: Optional[KingTokenNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[KingTokenTypeUnion]
            nulls: Optional[KingTokenNullGroup]
        """
        super().__init__(
            types=types or KingTokenTypeUnion(),
            nulls=nulls or KingTokenNullGroup(),
        )
    
    @property
    def types(self) -> KingTokenTypeUnion:
        return cast(KingTokenTypeUnion, super().types)
    
    @property
    def nulls(self) -> KingTokenNullGroup:
        return cast(KingTokenNullGroup, super().nulls)