# src/domain/metadata/context/manifest/context/coord/manifest.py

"""
Module: domain.metadata.manifest.context.coord.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Coord, CoordContextNullGroup, CoordContextTypeUnion, ContextManifest


class CoordContextManifest(ContextManifest[Coord]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and ContextTypeUnions for the Coord security lifecycle.

     Attributes:
        types: CoordContextTypeUnion
        nulls: CoordContextNullGroup

     Provides:

     Super Class:
        ContextManifest
     """
    
    def __init__(
            self,
            types: Optional[CoordContextTypeUnion] | None = None,
            nulls: Optional[CoordContextNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[CoordContextTypeUnion]
            nulls: Optional[CoordContextNullGroup]
        """
        super().__init__(
            types=types or CoordContextTypeUnion(),
            nulls=nulls or CoordContextNullGroup(),
        )
        
    @property
    def types(self) -> CoordContextTypeUnion:
        return cast(CoordContextTypeUnion, super().types)
    
    @property
    def nulls(self) -> CoordContextNullGroup:
        return cast(CoordContextNullGroup, super().nulls)