# src/assurance/depend/toolkit/model/vector/toolkit.py

"""
Module: assurance.depend.toolkit.model.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelLayerToolkit, VectorServiceDependency
from domain import Vector, VectorManifest, VectorNullWarningSet, VectorLayer


class VectorLayerToolkit(ModelLayerToolkit[Vector]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Vector attribute validators and type manifest.

    Attributes:
        helper: VectorManifest
        manifest: VectorServiceDependency

    Provides:

    Super Class:
        ModelLayerToolkit
    """
    
    def __init__(
            self,
            manifest: Optional[VectorManifest] | None = None,
            dependency: Optional[VectorServiceDependency] | None = None,
    ):
        """
        Args:
            dependency: Optional[VectorManifest]
            manifest: Optional[VectorServiceDependency]
        """
        super().__init__(
            dependency=dependency or VectorServiceDependency(),
            manifest=manifest or VectorManifest(),
        )
    
    @property
    def dependency(self) -> VectorServiceDependency:
        return cast(VectorServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> VectorManifest:
        return cast(VectorManifest, super().manifest)
    
    @property
    def nulls(self) -> VectorNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> VectorLayer:
        return self.manifest.types