# src/domain/metadata/context/manifest/context/vector/manifest.py

"""
Module: domain.metadata.manifest.context.vector.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ContextManifest, Vector, VectorContextNullGroup, VectorContextLayer


class VectorContextManifest(ContextManifest[Vector]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and ContextTypeUnions for the Vector security lifecycle.

     Attributes:
        types: VectorContextTypeUnion
        nulls: VectorContextNullGroup

     Provides:

     Super Class:
        ContextManifest
     """
    
    def __init__(
            self,
            types: Optional[VectorContextLayer] | None = None,
            nulls: Optional[VectorContextNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[VectorContextTypeUnion]
            nulls: Optional[VectorContextNullGroup]
        """
        super().__init__(
            types=types or VectorContextLayer(),
            nulls=nulls or VectorContextNullGroup(),
        )
        
    @property
    def types(self) -> VectorContextLayer:
        return cast(VectorContextLayer, super().types)
    
    @property
    def nulls(self) -> VectorContextNullGroup:
        return cast(VectorContextNullGroup, super().nulls)