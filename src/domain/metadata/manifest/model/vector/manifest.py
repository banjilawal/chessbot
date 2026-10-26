# src/domain/metadata/manifest/model/vector/manifest.py

"""
Module: domain.metadata.manifest.model.vector.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ModelManifest, Vector, VectorNullWarningSet, VectorLayer


class VectorManifest(ModelManifest[Vector]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the Vector security lifecycle.

     Attributes:
        types: VectorTypeUnion
        nulls: VectorNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: Optional[VectorLayer] | None = None,
            nulls: Optional[VectorNullWarningSet] | None = None,
    ):
        """
        Args:
            types: Optional[VectorTypeUnion]
            nulls: Optional[VectorNullGroup]
        """
        super().__init__(
            types=types or VectorLayer(),
            nulls=nulls or VectorNullWarningSet(),
        )
        
    @property
    def types(self) -> VectorLayer:
        return cast(VectorLayer, super().types)
    
    @property
    def nulls(self) -> VectorNullWarningSet:
        return cast(VectorNullWarningSet, super().nulls)