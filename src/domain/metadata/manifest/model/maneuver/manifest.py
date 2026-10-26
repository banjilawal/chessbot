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
    Maneuver, ManeuverNullWarningSet, ManeuverLayer, ModelManifest
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
            types: Optional[ManeuverLayer] | None = None,
            nulls: Optional[ManeuverNullWarningSet] | None = None,
    ):
        """
        Args:
            types: Optional[ManeuverTypeUnion]
            nulls: Optional[ManeuverNullGroup]
        """
        super().__init__(
            types=types or ManeuverLayer(),
            nulls=nulls or ManeuverNullWarningSet(),
        )
        
    @property
    def types(self) -> ManeuverLayer:
        return cast(ManeuverLayer, super().types)
    
    @property
    def nulls(self) -> ManeuverNullWarningSet:
        return cast(ManeuverNullWarningSet, super().nulls)