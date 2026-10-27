# src/assurance/depend/toolkit/model/scalar/toolkit.py

"""
Module: assurance.depend.toolkit.model.scalar.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelLayerToolkit, ScalarServiceDependency
from domain import Scalar, ScalarManifest, ScalarNullWarningSet, ScalarLayer


class ScalarLayerToolkit(ModelLayerToolkit[Scalar]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Scalar attribute validators and type manifest.

    Attributes:
        helper: ScalarManifest
        manifest: ScalarServiceDependency

    Provides:

    Super Class:
        ModelLayerToolkit
    """
    
    def __init__(
            self,
            manifest: Optional[ScalarManifest] | None = None,
            dependency: Optional[ScalarServiceDependency] | None = None,
    ):
        """
        Args:
            dependency: Optional[ScalarManifest]
            manifest: Optional[ScalarServiceDependency]
        """
        super().__init__(
            dependency=dependency or ScalarServiceDependency(),
            manifest=manifest or ScalarManifest(),
        )
    
    @property
    def dependency(self) -> ScalarServiceDependency:
        return cast(ScalarServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> ScalarManifest:
        return cast(ScalarManifest, super().manifest)
    
    @property
    def nulls(self) -> ScalarNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> ScalarLayer:
        return self.manifest.types