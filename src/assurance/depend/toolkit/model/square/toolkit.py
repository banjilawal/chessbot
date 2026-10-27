# src/assurance/depend/toolkit/model/square/toolkit.py

"""
Module: assurance.depend.toolkit.model.square.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelLayerToolkit, SquareServiceDependency
from domain import Square, SquareManifest, SquareNullWarningSet, SquareLayer


class SquareLayerToolkit(ModelLayerToolkit[Square]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Square attribute validators and type manifest.

    Attributes:
        helper: SquareManifest
        manifest: SquareServiceDependency

    Provides:

    Super Class:
        ModelLayerToolkit
    """
    
    def __init__(
            self,
            manifest: Optional[SquareManifest] | None = None,
            dependency: Optional[SquareServiceDependency] | None = None,
    ):
        """
        Args:
            dependency: Optional[SquareManifest]
            manifest: Optional[SquareServiceDependency]
        """
        super().__init__(
            dependency=dependency or SquareServiceDependency(),
            manifest=manifest or SquareManifest(),
        )
    
    @property
    def dependency(self) -> SquareServiceDependency:
        return cast(SquareServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> SquareManifest:
        return cast(SquareManifest, super().manifest)
    
    @property
    def nulls(self) -> SquareNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> SquareLayer:
        return self.manifest.types