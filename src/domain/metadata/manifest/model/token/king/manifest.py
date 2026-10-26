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
    KingTokenNullWarningSet, KingToken, TokenManifest, KingTokenLayer
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
            types: Optional[KingTokenLayer] | None = None,
            nulls: Optional[KingTokenNullWarningSet] | None = None,
    ):
        """
        Args:
            types: Optional[KingTokenTypeUnion]
            nulls: Optional[KingTokenNullGroup]
        """
        super().__init__(
            types=types or KingTokenLayer(),
            nulls=nulls or KingTokenNullWarningSet(),
        )
    
    @property
    def types(self) -> KingTokenLayer:
        return cast(KingTokenLayer, super().types)
    
    @property
    def nulls(self) -> KingTokenNullWarningSet:
        return cast(KingTokenNullWarningSet, super().nulls)