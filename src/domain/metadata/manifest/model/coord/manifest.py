# src/domain/metadata/manifest/model/coord/manifest.py

"""
Module: domain.metadata.manifest.model.coord.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Coord, CoordNullGroup, CoordLayer, ModelManifest


class CoordManifest(ModelManifest[Coord]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the Coord security lifecycle.

     Attributes:
        types: CoordTypeUnion
        nulls: CoordNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: Optional[CoordLayer] | None = None,
            nulls: Optional[CoordNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[CoordTypeUnion]
            nulls: Optional[CoordNullGroup]
        """
        super().__init__(
            types=types or CoordLayer(),
            nulls=nulls or CoordNullGroup(),
        )
        
    @property
    def types(self) -> CoordLayer:
        return cast(CoordLayer, super().types)
    
    @property
    def nulls(self) -> CoordNullGroup:
        return cast(CoordNullGroup, super().nulls)