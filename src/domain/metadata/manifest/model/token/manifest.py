# src/domain/metadata/manifest/model/token/manifest.py

"""
Module: domain.metadata.manifest.model.token.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ModelManifest, Token, TokenNullGroup, TokenTypeUnion



class TokenManifest(ModelManifest[Token]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Token's security lifecycle.

     Attributes:
        types: TokenTypeUnion
        nulls: TokenNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: Optional[TokenTypeUnion] | None = None,
            nulls: Optional[TokenNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[TokenTypeUnion]
            nulls: Optional[TokenNullGroup]
        """
        super().__init__(
            types=types or TokenTypeUnion(),
            nulls=nulls or TokenNullGroup(),
        )
        
    @property
    def types(self) -> TokenTypeUnion:
        return cast(TokenTypeUnion, super().types)
    
    @property
    def nulls(self) -> TokenNullGroup:
        return cast(TokenNullGroup, super().nulls)