# src/domain/metadata/manifest/struct/model/footstep/manifest.py

"""
Module: domain.metadata.manifest.model.footstep.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ModelManifest, Footstep, FootstepNullWarningSet, FootstepLayer


class FootstepManifest(ModelManifest[Footstep]):
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
        DomainManifest
     """
    
    def __init__(
            self,
            types: Optional[FootstepLayer] | None = None,
            nulls: Optional[FootstepNullWarningSet] | None = None,
    ):
        """
        Args:
            types: Optional[FootstepTypeUnion]
            nulls: Optional[FootstepNullGroup]
        """
        super().__init__(
            types=types or FootstepLayer(),
            nulls=nulls or FootstepNullWarningSet(),
        )
  
    @property
    def types(self) -> FootstepLayer:
        return cast(FootstepLayer, super().types)
    
    @property
    def nulls(self) -> FootstepNullWarningSet:
        return cast(FootstepNullWarningSet, super().nulls)