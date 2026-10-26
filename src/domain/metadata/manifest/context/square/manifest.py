# src/domain/metadata/context/manifest/context/square/square/manifest.py

"""
Module: domain.metadata.manifest.context.square.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from domain import SquareContextNullGroup, ContextManifest, Square, SquareContextTypeUnion


class SquareContextManifest(ContextManifest[Square]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and SquareContextTypeUnions for the Square
            security lifecycle.

     Attributes:
        types: SquareContextTypeUnion
        nulls: SquareContextNullGroup

     Provides:

     Super Class:
        ContextManifest
     """
    
    def __init__(
            self,
            types: SquareContextTypeUnion,
            nulls: SquareContextNullGroup
    ):
        """
        Args:
            types: SquareContextTypeUnion,
            nulls: SquareContextNullGroup
        """
        super().__init__(types=types, nulls=nulls)
    
    @property
    def types(self) -> SquareContextTypeUnion[T]:
        return cast(SquareContextTypeUnion[T], super().types)
    
    @property
    def nulls(self) -> SquareContextNullGroup[T]:
        return cast(SquareContextNullGroup[T], super().nulls)