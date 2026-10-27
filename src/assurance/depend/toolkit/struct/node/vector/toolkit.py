# src/assurance/depend/toolkit/struct/node/vector/toolkit.py

"""
Module: assurance.depend.toolkit.struct.node.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import NodeLayerToolkit, VectorNodeDependency
from domain import (
    VectorNode, VectorNodeManifest, VectorNodeNullWarningSet,
    VectorNodeLayer
)


class VectorNodeLayerToolkit(NodeLayerToolkit[VectorNode]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type manifest.

    Attributes:
            wrapper: VectorNodeDependency
            manifest: VectorNodeManifest

    Provides:

    Super Class:
       NodeLayerToolkit
    """
    
    def __init__(
            self,
            dependency: Optional[VectorNodeDependency] | None = None,
            manifest: Optional[VectorNodeManifest] | None = None,
    ):
        """
            wrapper: Optional[VectorNodeDependency]
            manifest: Optional[VectorNodeManifest]
        """
        super().__init__(
            dependency=dependency or VectorNodeDependency(),
            manifest=manifest or VectorNodeManifest(),
        )
    
    @property
    def dependency(self) -> VectorNodeDependency:
        return cast(VectorNodeDependency, super().dependency)
    
    @property
    def manifest(self) -> VectorNodeManifest:
        return cast(VectorNodeManifest, super().manifest)
    
    @property
    def nulls(self) -> VectorNodeNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> VectorNodeLayer:
        return self.manifest.types