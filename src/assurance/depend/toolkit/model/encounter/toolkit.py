# src/assurance/depend/toolkit/model/encounter/toolkit.py

"""
Module: assurance.depend.toolkit.model.encounter.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelLayerToolkit, EncounterServiceDependency
from domain import (
    Encounter, EncounterManifest, EncounterNullWarningSet, EncounterLayer
)

class EncounterLayerToolkit(ModelLayerToolkit[Encounter]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Encounter attribute validators and type manifest.

    Attributes:
        helper: EncounterManifest
        manifest: EncounterServiceDependency

    Provides:

    Super Class:
        ModelLayerToolkit
    """
    
    def __init__(
            self,
            manifest: Optional[EncounterManifest] | None = None,
            dependency: Optional[EncounterServiceDependency] | None = None,
    ):
        """
        Args:
            dependency: Optional[EncounterManifest]
            manifest: Optional[EncounterServiceDependency]
        """
        super().__init__(
            dependency=dependency or EncounterServiceDependency(),
            manifest=manifest or EncounterManifest(),
        )
    
    @property
    def dependency(self) -> EncounterServiceDependency:
        return cast(EncounterServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> EncounterManifest:
        return cast(EncounterManifest, super().manifest)
    
    @property
    def nulls(self) -> EncounterNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> EncounterLayer:
        return self.manifest.types