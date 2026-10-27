# src/assurance/depend/toolkit/model/path/toolkit.py

"""
Module: assurance.depend.toolkit.model.path.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelLayerToolkit, PathServiceDependency
from domain import Path, PathManifest, PathNullWarningSet, PathLayer


class PathLayerToolkit(ModelLayerToolkit[Path]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Path attribute validators and type manifest.

    Attributes:
        helper: PathManifest
        manifest: PathServiceDependency

    Provides:

    Super Class:
        ModelLayerToolkit
    """
    
    def __init__(
            self,
            manifest: Optional[PathManifest] | None = None,
            dependency: Optional[PathServiceDependency] | None = None,
    ):
        """
        Args:
            dependency: Optional[PathManifest]
            manifest: Optional[PathServiceDependency]
        """
        super().__init__(
            dependency=dependency or PathServiceDependency(),
            manifest=manifest or PathManifest(),
        )
    
    @property
    def dependency(self) -> PathServiceDependency:
        return cast(PathServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> PathManifest:
        return cast(PathManifest, super().manifest)
    
    @property
    def nulls(self) -> PathNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> PathLayer:
        return self.manifest.types