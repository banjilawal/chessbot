# src/domain/metadata/context/manifest/context/maneuver/manifest.py

"""
Module: domain.metadata.manifest.context.maneuver.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    Maneuver, ManeuverContextNullGroup, ManeuverContextTypeUnion, ContextManifest
)

class ManeuverContextManifest(ContextManifest[Maneuver]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and ContextTypeUnions for the Maneuver
            security lifecycle.

     Attributes:
        types: ManeuverContextTypeUnion
        nulls: ManeuverContextNullGroup

     Provides:

     Super Class:
        ContextManifest
     """
    
    def __init__(
            self,
            types: Optional[ManeuverContextTypeUnion] | None = None,
            nulls: Optional[ManeuverContextNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[ManeuverContextTypeUnion]
            nulls: Optional[ManeuverContextNullGroup]
        """
        super().__init__(
            types=types or ManeuverContextTypeUnion(),
            nulls=nulls or ManeuverContextNullGroup(),
        )
        
    @property
    def types(self) -> ManeuverContextTypeUnion:
        return cast(ManeuverContextTypeUnion, super().types)
    
    @property
    def nulls(self) -> ManeuverContextNullGroup:
        return cast(ManeuverContextNullGroup, super().nulls)