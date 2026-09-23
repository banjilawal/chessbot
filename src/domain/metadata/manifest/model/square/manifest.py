# src/domain/metadata/manifest/model/square/manifest.py

"""
Module: domain.metadata.manifest.model.square.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Square, SquareNullGroup, SquareTypeUnion, ModelManifest


class SquareManifest(ModelManifest[Square]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Square's security lifecycle.

     Attributes:
        types: SquareTypeUnion
        nulls: SquareNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: Optional[SquareTypeUnion] | None = None,
            nulls: Optional[SquareNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[SquareTypeUnion]
            nulls: Optional[SquareNullGroup]
        """
        super().__init__(
            types=types or SquareTypeUnion(),
            nulls=nulls or SquareNullGroup(),
        )
        
    @property
    def types(self) -> SquareTypeUnion:
        return cast(SquareTypeUnion, super().types)
    
    @property
    def nulls(self) -> SquareNullGroup:
        return cast(SquareNullGroup, super().nulls)