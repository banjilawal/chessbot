# src/domain/metadata/context/manifest/context/square/square/manifest.py

"""
Module: domain.metadata.manifest.context.square.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from domain import SquareContextNullWarningSet, ContextManifest, Square, SquareContextLayer


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
            types: SquareContextLayer,
            nulls: SquareContextNullWarningSet
    ):
        """
        Args:
            types: SquareContextTypeUnion,
            nulls: SquareContextNullGroup
        """
        super().__init__(types=types, nulls=nulls)
    
    @property
    def types(self) -> SquareContextLayer[T]:
        return cast(SquareContextLayer[T], super().types)
    
    @property
    def nulls(self) -> SquareContextNullWarningSet[T]:
        return cast(SquareContextNullWarningSet[T], super().nulls)