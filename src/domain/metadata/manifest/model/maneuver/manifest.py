# src/domain/metadata/manifest/model/maneuver/manifest.py

"""
Module: domain.metadata.manifest.model.maneuver.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    Maneuver, ManeuverNullGroup, ManeuverTypeUnion, ModelManifest
)

class ManeuverManifest(ModelManifest[Maneuver]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the Maneuver
            security lifecycle.

     Attributes:
        types: ManeuverTypeUnion
        nulls: ManeuverNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: Optional[ManeuverTypeUnion] | None = None,
            nulls: Optional[ManeuverNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[ManeuverTypeUnion]
            nulls: Optional[ManeuverNullGroup]
        """
        super().__init__(
            types=types or ManeuverTypeUnion(),
            nulls=nulls or ManeuverNullGroup(),
        )
        
    @property
    def types(self) -> ManeuverTypeUnion:
        return cast(ManeuverTypeUnion, super().types)
    
    @property
    def nulls(self) -> ManeuverNullGroup:
        return cast(ManeuverNullGroup, super().nulls)