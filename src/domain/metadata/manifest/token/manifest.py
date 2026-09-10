# src/domain/metadata/manifest/token/manifest.py

"""
Module: domain.metadata.manifest.token.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Token, TokenNullGroup, TokenTypeUnion, ObjectManifest


class TokenManifest(ObjectManifest[Token]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Token's security lifecycle.

     Attributes:
        type_union: TokenTypeUnion
        null_group: TokenNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            type_union: Optional[TokenTypeUnion] | None = None,
            null_group: Optional[TokenNullGroup] | None = None,
    ):
        """
        Args:
            type_union: Optional[TokenTypeUnion]
            null_group: Optional[TokenNullGroup]
        """
        super().__init__(
            type_union=type_union or TokenTypeUnion(),
            null_group=null_group or TokenNullGroup(),
        )
        
    @property
    def types(self) -> TokenTypeUnion:
        return cast(TokenTypeUnion, super().types)
    
    @property
    def nulls(self) -> TokenNullGroup:
        return cast(TokenNullGroup, super().nulls)