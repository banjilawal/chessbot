# src/domain/metadata/manifest/strcture/chart/walk/manifest.py

"""
Module: domain.metadata.manifest.struct.chart.walk.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ChartManifest, Walk, WalkNullGroup, WalkTypeUnion


class WalkManifest(ChartManifest[Walk]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the Walk
            security lifecycle.

     Attributes:
        types: WalkTypeUnion
        nulls: WalkNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            types: Optional[WalkTypeUnion] | None = None,
            nulls: Optional[WalkNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[WalkTypeUnion]
            nulls: Optional[WalkNullGroup]
        """
        super().__init__(
            types=types or WalkTypeUnion(),
            nulls=nulls or WalkNullGroup(),
        )

        
    @property
    def types(self) -> WalkTypeUnion:
        return cast(WalkTypeUnion, super().types)
    
    @property
    def nulls(self) -> WalkNullGroup:
        return cast(WalkNullGroup, super().nulls)