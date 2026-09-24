# src/domain/metadata/manifest/model/square/square/manifest.py

"""
Module: domain.metadata.manifest.model.square.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from domain import SquareNullGroup, ModelManifest, Square, SquareTypeUnion


class SquareManifest(ModelManifest[Square]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and SquareTypeUnions for the Square
            security lifecycle.

     Attributes:
        types: SquareTypeUnion
        nulls: SquareNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: SquareTypeUnion,
            nulls: SquareNullGroup
    ):
        """
        Args:
            types: SquareTypeUnion,
            nulls: SquareNullGroup
        """
        super().__init__(types=types, nulls=nulls)
    
    @property
    def types(self) -> SquareTypeUnion[T]:
        return cast(SquareTypeUnion[T], super().types)
    
    @property
    def nulls(self) -> SquareNullGroup[T]:
        return cast(SquareNullGroup[T], super().nulls)