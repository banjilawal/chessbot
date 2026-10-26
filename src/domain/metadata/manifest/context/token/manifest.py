# src/domain/metadata/context/manifest/context/token/token/manifest.py

"""
Module: domain.metadata.manifest.context.token.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


class TokenContextManifest(ContextManifest[Token]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and ContextTypeUnions for the Token
            security lifecycle.

     Attributes:
        types: TokenContextTypeUnion[T]
        nulls: TokenContextNullGroup[T]

     Provides:

     Super Class:
        ContextManifest
     """

    def __init__(
            self,
            types: Optional[TokenContextTypeUnion[T]] | None = None,
            nulls: Optional[TokenContextNullGroup[T]] | None = None,
    ):
        """
        Args:
            types: TokenContextTypeUnion[T]
            nulls: TokenContextNullGroup[T]
        """
        super().__init__(
            types=types or TokenContextTypeUnion(),
            nulls=nulls or TokenContextNullGroup(),
        )

    @property
    def types(self) -> TokenContextTypeUnion[T]:
        return cast(TokenContextTypeUnion[T], super().types)

    @property
    def nulls(self) -> TokenContextNullGroup[T]:
        return cast(TokenContextNullGroup[T], super().nulls)