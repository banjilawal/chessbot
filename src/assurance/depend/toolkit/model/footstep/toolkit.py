# src/assurance/depend/toolkit/model/footstep/toolkit.py

"""
Module: assurance.depend.toolkit.model.footstep.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelLayerToolkit, FootstepServiceDependency
from domain import Footstep, FootstepManifest, FootstepNullWarningSet, FootstepLayer


class FootstepLayerToolkit(ModelLayerToolkit[Footstep]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type manifest.

    Attributes:
            wrapper: FootstepDependency
            manifest: FootstepManifest

    Provides:

    Super Class:
       ModelLayerToolkit
    """
    
    def __init__(
            self,
            dependency: Optional[FootstepServiceDependency] | None = None,
            manifest: Optional[FootstepManifest] | None = None,
    ):
        """
            wrapper: Optional[FootstepDependency]
            manifest: Optional[FootstepManifest]
        """
        super().__init__(
            dependency=dependency or FootstepServiceDependency(),
            manifest=manifest or FootstepManifest(),
        )
    
    @property
    def dependency(self) -> FootstepServiceDependency:
        return cast(FootstepServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> FootstepManifest:
        return cast(FootstepManifest, super().manifest)
    
    @property
    def nulls(self) -> FootstepNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> FootstepLayer:
        return self.manifest.types