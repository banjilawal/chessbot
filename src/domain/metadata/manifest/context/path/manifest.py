# src/domain/metadata/context/manifest/context/path/manifest.py

"""
Module: domain.metadata.manifest.context.path.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Path, PathContextNullGroup, PathContextTypeUnion, ContextManifest


class PathContextManifest(ContextManifest[Path]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and ContextTypeUnions for the Path
            security lifecycle.

     Attributes:
        types: PathContextTypeUnion
        nulls: PathContextNullGroup

     Provides:

     Super Class:
        ContextManifest
     """
    
    def __init__(
            self,
            types: Optional[PathContextTypeUnion] | None = None,
            nulls: Optional[PathContextNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[PathContextTypeUnion]
            nulls: Optional[PathContextNullGroup]
        """
        super().__init__(
            types=types or PathContextTypeUnion(),
            nulls=nulls or PathContextNullGroup(),
        )
        
    @property
    def types(self) -> PathContextTypeUnion:
        return cast(PathContextTypeUnion, super().types)
    
    @property
    def nulls(self) -> PathContextNullGroup:
        return cast(PathContextNullGroup, super().nulls)