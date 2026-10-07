# src/domain/metadata/manifest/strcture/chart/footstep/manifest.py

"""
Module: domain.metadata.manifest.struct.chart.footstep.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ChartManifest, Footstep, FootstepNullGroup, FootstepTypeUnion


class FootstepManifest(ChartManifest[Footstep]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the Footstep
            security lifecycle.

     Attributes:
        types: FootstepTypeUnion
        nulls: FootstepNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            types: Optional[FootstepTypeUnion] | None = None,
            nulls: Optional[FootstepNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[FootstepTypeUnion]
            nulls: Optional[FootstepNullGroup]
        """
        super().__init__(
            types=types or FootstepTypeUnion(),
            nulls=nulls or FootstepNullGroup(),
        )

        
    @property
    def types(self) -> FootstepTypeUnion:
        return cast(FootstepTypeUnion, super().types)
    
    @property
    def nulls(self) -> FootstepNullGroup:
        return cast(FootstepNullGroup, super().nulls)