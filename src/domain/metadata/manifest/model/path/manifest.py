# src/domain/metadata/manifest/model/path/manifest.py

"""
Module: domain.metadata.manifest.model.path.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Path, PathNullGroup, PathTypeUnion, ModelManifest


class PathManifest(ModelManifest[Path]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the Path
            security lifecycle.

     Attributes:
        types: PathTypeUnion
        nulls: PathNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: Optional[PathTypeUnion] | None = None,
            nulls: Optional[PathNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[PathTypeUnion]
            nulls: Optional[PathNullGroup]
        """
        super().__init__(
            types=types or PathTypeUnion(),
            nulls=nulls or PathNullGroup(),
        )
        
    @property
    def types(self) -> PathTypeUnion:
        return cast(PathTypeUnion, super().types)
    
    @property
    def nulls(self) -> PathNullGroup:
        return cast(PathNullGroup, super().nulls)