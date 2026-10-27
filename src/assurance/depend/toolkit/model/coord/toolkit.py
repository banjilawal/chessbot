# src/assurance/depend/toolkit/model/coord/toolkit.py

"""
Module: assurance.depend.toolkit.model.coord.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelLayerToolkit, CoordServiceDependency
from domain import Coord, CoordManifest, CoordNullWarningSet, CoordLayer


class CoordLayerToolkit(ModelLayerToolkit[Coord]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Coord attribute validators and type manifest.

    Attributes:
        helper: CoordManifest
        manifest: CoordServiceDependency

    Provides:

    Super Class:
        ModelLayerToolkit
    """
    
    def __init__(
            self,
            manifest: Optional[CoordManifest] | None = None,
            dependency: Optional[CoordServiceDependency] | None = None,
    ):
        """
        Args:
            dependency: Optional[CoordManifest]
            manifest: Optional[CoordServiceDependency]
        """
        super().__init__(
            dependency=dependency or CoordServiceDependency(),
            manifest=manifest or CoordManifest(),
        )
    
    @property
    def dependency(self) -> CoordServiceDependency:
        return cast(CoordServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> CoordManifest:
        return cast(CoordManifest, super().manifest)
    
    @property
    def nulls(self) -> CoordNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> CoordLayer:
        return self.manifest.types