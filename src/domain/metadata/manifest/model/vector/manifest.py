# src/domain/metadata/manifest/model/vector/manifest.py

"""
Module: domain.metadata.manifest.model.vector.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ModelManifest, Vector, VectorNullGroup, VectorTypeUnion


class VectorManifest(ModelManifest[Vector]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for a Vector's security lifecycle.

     Attributes:
        types: VectorTypeUnion
        nulls: VectorNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: Optional[VectorTypeUnion] | None = None,
            nulls: Optional[VectorNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[VectorTypeUnion]
            nulls: Optional[VectorNullGroup]
        """
        super().__init__(
            types=types or VectorTypeUnion(),
            nulls=nulls or VectorNullGroup(),
        )
        
    @property
    def types(self) -> VectorTypeUnion:
        return cast(VectorTypeUnion, super().types)
    
    @property
    def nulls(self) -> VectorNullGroup:
        return cast(VectorNullGroup, super().nulls)