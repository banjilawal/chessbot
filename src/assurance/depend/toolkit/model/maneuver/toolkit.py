# src/assurance/depend/toolkit/model/maneuver/toolkit.py

"""
Module: assurance.depend.toolkit.model.maneuver.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelLayerToolkit, ManeuverServiceDependency
from domain import Maneuver, ManeuverManifest, ManeuverNullWarningSet, ManeuverLayer


class ManeuverLayerToolkit(ModelLayerToolkit[Maneuver]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Maneuver attribute validators and type manifest.

    Attributes:
        helper: ManeuverManifest
        manifest: ManeuverServiceDependency

    Provides:

    Super Class:
        ModelLayerToolkit
    """
    
    def __init__(
            self,
            manifest: Optional[ManeuverManifest] | None = None,
            dependency: Optional[ManeuverServiceDependency] | None = None,
    ):
        """
        Args:
            dependency: Optional[ManeuverManifest]
            manifest: Optional[ManeuverServiceDependency]
        """
        super().__init__(
            dependency=dependency or ManeuverServiceDependency(),
            manifest=manifest or ManeuverManifest(),
        )
    
    @property
    def dependency(self) -> ManeuverServiceDependency:
        return cast(ManeuverServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> ManeuverManifest:
        return cast(ManeuverManifest, super().manifest)
    
    @property
    def nulls(self) -> ManeuverNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> ManeuverLayer:
        return self.manifest.types